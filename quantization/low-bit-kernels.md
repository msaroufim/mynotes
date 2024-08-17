## Gemlite and related work

https://mobiusml.github.io/gemlite_blogpost/

Library for GEMV (General Matrix Vector Multiplication)

This has a nice explanation of an optimized GEMV algorithm https://github.com/Bruce-Lee-LY/cuda_hgemv#optimization-method

Samea author has more work that shows up here https://github.com/Bruce-Lee-LY/cuda_hgemm with common optimizations that matter

`gemv_A16fWnO16f_int32packing`  fp16 x n-bit as 32-bit packed, mixed fp16 accumulation. Main optimizations seem to be warp reductions, caching
## Marlin

https://github.com/IST-DASLab/marlin

Fp14xInt4 LLM inference kernel for small batch sizes (16-32 tokens)

Some cool notes is this kernel isn't as drastically affected by 

Extension to the above work is https://github.com/IST-DASLab/Sparse-Marlin which supports 4 bit quantized weights now with 2:4 sparsity

It leverages: global memory, l2 cache, shared memory, tensor cores and vector cores

Both sparse and main marlin repo do not package binaries and instead rely on from source development builds

Need to invite these guys to speak at CUDA MODE. It's the same lab that invented GPTQ.



## tinygemm

As a torch op, this has no seperate repo

## CUTLASS

SOme people are building their own low bit kernels on top of https://github.com/NVIDIA/cutlass/issues/1549 

CUTLASS has an int4 dtype here `cutlass::int4b_t`

CUTLASS team does not seem to be responsive on github issues but they have a Universal Gemm operator that seems to just handle everything down to int4 but not lower

Other interesting PRs by Alex https://github.com/NVIDIA/cutlass/pull/1413 for signed and unsigned int4/8 support 

## Gemmlowp

https://github.com/google/gemmlowp

These are optimizeed for ARM and Intel X86

## Flash infer

Flash Infer (everyone else is citing this work) https://github.com/flashinfer-ai/flashinfer a kernel library for inference. 

features include
* bs=1 and n kernels for prefill, decode and append kernels on different kv cache formats including pagged, ragged and page table. compressed and quantized kv cahe. We need to do more systems work.


## Other papers
* LUT-GEMM https://arxiv.org/abs/2206.09557
* Atom low bit quantization for efficient and accurate LLM serving https://arxiv.org/abs/2310.19102 - in particular they implemented their own kernels for W8A8 and W4A16 but since we already have tinygemm this is not super relevant
* Flash Infer (everyone else is citing this work) https://github.com/flashinfer-ai/flashinfer a kernel library for inference. 
* DeepGEMM: https://arxiv.org/abs/2304.09049 - lol 2 bit matrix multiplication is represented as a lookup table and then 4 of these values are packed into an 8 bit vector register. Their benchmarks are on x86 and they benchmark vs QNNPACK


## FAQ

> Q: Why does everyone talk about header only libraries

The main benefit is that you just include header files without a seperate compilation this means you have a reduced build complexity

> Q: Does int8 have hardware support?

Yes, NVIDIA supports them in A100s, not sure about H100 . Multiplication is done in int8 but typically typically dequantized and accumulated into an fp16 unit. All these operations need to be fused.

