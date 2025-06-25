| Piece                                                | What it really is / does                                                                                                                                                                                                                                                                                                                                                                                              | Why it exists                                                                                                                                                                              |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`compile_kernel()` + NVRTC**                       | Python helper that **compiles CUDA *source strings* to PTX on the fly**, then launches via the driver API. Every *new* string triggers 10-100 ms of compile latency and must stick to NVRTC’s restricted CUDA/C++ subset.                                                                                                                                                                                             | Perfect for quick prototyping or tiny,   few-times-per-run kernels.                                                                                                                        |
| **Traditional “just use `nvcc` and ship a `.so`”**   | nvcc embeds each fatbin inside a host object, generates a per-kernel stub, and you load that `.so`. Fast at runtime, but every extra kernel means another `.so`, another link step, more ABI baggage, and larger wheels.                                                                                                                                                                                              | Fine for the *finite* set of ATen kernels that ship with PyTorch. Not scalable to the thousands of shape-specialised kernels Inductor emits.                                               |
| **`StaticCudaLauncher` (in `torch/csrc/inductor` )** | A tiny C++ **loader/dispatcher** already built into `libtorch_cuda.so`. At compile time Inductor/Triton runs **nvcc --cubin** once per new kernel → a 4-8 kB `.cubin` file **plus** a one-line `REGISTER_STATIC_CUDA_KERNEL(hash,"…cubin")` stub. The launcher’s global map learns that hash on `dlopen`; at runtime it lazy-loads the cubin and calls `cuLaunchKernelEx()`—no Python, no NVRTC, no per-kernel `.so`. | Keeps **nvcc-level code-generation quality** (full C++17, CUB, Thrust, etc.) while avoiding both NVRTC latency *and* the file-size / link-time pain of thousands of tiny shared libraries. |


> “Is the cubin created dynamically?”

Yes. Inductor generates the .cu, then calls nvcc/clang –cubin during the graph-compile phase. That happens once per unique kernel variant.

> “Does StaticCudaLauncher get built at runtime?”

No. The launcher is already inside the shipped PyTorch .so. Only the tiny *_reg.cpp stubs are compiled/linked (quickly) to tell the launcher about new hashes.

> “What happens during execution?”

The first time a kernel is invoked, the launcher loads its cubin (cuModuleLoad) and caches the CUfunction; subsequent calls are just cuLaunchKernelEx—μs-level overhead.

> “Why not just many .sos?”

Each extra .so would add link + dlopen latency (~3 ms) and 50-80 kB of ELF bloat. With thousands of kernels that explodes runtime and wheel size. Cubins are 4-8 kB blobs with no host ABI baggage.

> “So StaticCudaLauncher is like NVRTC?”

Not a compiler at all, it's a dynamic loader for prebuilt cubins, complementary to nvcc rather than an alternative to NVRTC.

Inductor compiles each new kernel to a lightweight .cubin once; StaticCudaLauncher—already in PyTorch—simply hot-loads those cubins and fires them, giving you nvcc-quality kernels with NVRTC-like flexibility but near-zero launch overhead.









