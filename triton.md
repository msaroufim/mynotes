It has a debugger now https://github.com/openai/triton/pull/2321


## Phil keynote

Had to do many rewrites
A100 performance is good especially in memory bandwidth bound workloads
H100 performance matches cublas for square matrices and other shapes aware of this problem
Interpreter mode: To debug added an interpreter mode.. can now use breakpoints which are now in beta version
New backends will be AMD and intel, most of the community explosion happened in 2022
Improve vectorization, pipelining, extra layout conversion
todo H100 attention w/ fp8 support
Triton will give best out of the box performance and w/ more effort CUDA and SASS will give you better upper bounds but with a lot more work
Performance problems are higher priority than compiler crashes which means better tests and not more tests. Limit integration testing in favor of unit testing, bette error messages

See env variable `TRITON_INTERPRETER`

## NVIDIA talk

Hopper is cost efficient and has new features like
* TMA
* WGMMA
* Distributed shared memory
* Warp serialization
* Heuristics might be outdated

TMA multicast and async transaction barrier 

Block pointer API 

took some screenshots


## AMD backend

Full support with torch.compile using `device_type="hip"`

AMD already invested a lot in LLM and MLIR, tritoin gpu IR moslty reused
same swizzling patterns 
Port PTX usage with amdgcn assembly and MLIR

support empty kernel and base set of triton ops
enable matrix core support: softmax, dot and fslash
max occupancy and efficeincy: pipelining, swizzling, increased wavefronts per CU

MI250x/flops/clock/cu

## Intel XPU backend

Showcased fusions with pytorch profiler, was mostly easy to integrate

## Qualcomm backend

2 approaches
1. Triton IR vectorized llvm-ir
2. Triton to linalg approach by Microsoft

Too many technical isues couldn't hear

## Triton MTIA

Meta Training and Inference Accelerator

SPMD programming model and need to build a community but 

MSFT linalg did not exist a year ago so implemented their own prototype using python

DMA, MLU, SFU, DPE and Vector - and current Triton prototype makes use of all major HW fixed function units

Open questions about non GPU acceleators: 
1. Suport for DMA friendly memory access, wider use of block pointers is preferred
2. additional support for custom levels of memory hierarchy
3. DMA broadcat and inter-PE reduction

## XLA compiler

Convert from HLO to triton IR

Hero instruction?

Incompatible tiling: blocking fusion to decide when fusions are possible or not


If same tiling on both sides then fuse otherwise don't, can do lots of tricks to fuse complex benchmarks 

Triton features: triton fusions, better triton tiling, fix split_k, transpose fix and tiling fixes

Cost model for fusion intellignence choices 
Cutlass able to achieve better perf on some fusions

github.com/openxla

## Triton 4 all

How to scale triton on many hw targets

HW agnostic: common analysi, optimizations and transformations

Language agnostic: bring existing MLIR backends

Value semantics of lnalg match BLOCK SIMD 

do further transformations and loop fusion adn tiling

triton code -> triton IR -> linalg dialect that can target machine dependent code - triton IR is modeling a block of computation

Check out PR 1797 and discussions 1842

Look at TOSA 

Linalg_ext (IREE) and tensorRT (torch-mlir)

A lot of excitement about block pointers in general

## PT 2.0

Was in a meeting

## Jax

Both Pallas and Jax call - Pallas is higher level but slightly easier to reason about indexing code, also has support for a step debugger

This composes with vmap and grad 

`triton_call` lets you cal vanilla triton kernels from jax

Pallas is an extension to JAX for writing kernels: numpy style indexing instead of pointers, allows use of jax numpy, add blocksepcs, can 

Future work: Pallas on TPU, built Mosaic whic his Triton for TPUs, adding block pointer support and integrating kernels with jax more closely run into problems with AD, distributed computation and rematerialization

## Grover writing grouped GEMM in Triton

goal was to showcase how to use features available in cutlass and match most of its performance 
