References
https://www.nvidia.com/content/PDF/nvidia-ampere-ga-102-gpu-architecture-whitepaper-v2.pdf
https://arxiv.org/pdf/1804.06826.pdf


GPU architecture history
https://en.wikipedia.org/wiki/Hopper_(microarchitecture)
Hopper -> Multi chip modules
Lovelace -> 144 SM and rumors of High Bandwith Memory like CPUs
Ampere -> Tensor cores (bfloat, tfloat), sparsity, high bandwith memory, NVLink (mesh communication instead of central), jpeg decode (image processing), video decode (streaming), GDDR6 (fast ram)
Tensor cores is a unit that multiplies 2 4x4 fp16 matrices then adds the result to its own fp16 or fp32 matrix
They use TSMC transistors - Ampere uses the 7nm one
Pascal -> intrusction level premtpion, dynamic load balancing, more registers, unified memory wti the CPU (page migration engine)

A "Streaming Multiprocessor" corresponds to AMD's Compute Unit. An SMP encompasses 128 single-precision ALUs ("CUDA cores") on GP104 chips and 64 single-precision ALUs on GP100 chips.


Each Streaming Multiprocessor has 4 processor blocks each processor block can execute its own instructions with WARP and dispatch scheduler. Can multiply 2 16 elements fp32 matrices in one instruction. Wheras can only multiply 2 8 element f64 matrices at once .
 
fp32 units are cuda cores that can't execute individual instructions (SIMD). 

There are also 2 tensor cores each tensor cores each has 4x16 blocks. There's also 4 fuse multiply add blocks

1 operation per clock cycle per tensor core needs pipelining - fuse multiply add block

CMA block has Mul Add Add Round But need to only apply round in final cycle and then can pipeline operations and then can do one operation per cycle

PCIe vs VLink: PCIE and NVlink are two completely different technologies. NVlink is a bridge intended for graphics cards to communicate with each other and increase the power of your machine. PCIE is an interface intended to house any expansion card like graphics cards, sound cards, more USB, etc.

How does NVIDA do sparsity: Fine-Grained Structured Sparsity which sparsifies trained weights in a fixed manner to make inference faster

Micron Technology produced RAM for GPUs uses PAM4 signaling to transmit 2 bits of data with each signal change

GPUs can load data quickly with NVDIA RTX IO which uses the Microsoft DirectStorage API to compress in a lossless manner game assets (also should work for games) by directly talking to the GPU without going through the CPU

GPUs also support hardware accelerated video decoding and image encoding for fast read writes

GPUs have automatic error detection when overclocking