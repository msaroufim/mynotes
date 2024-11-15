# Glossary

Terminology I keep running into and forgetting

* Tensor cores: 15x flops for matmuls. Layout is funky but it helps to think of the reads being sequential from the perspective of the tited matmul algorithm
* Async loads: Load directly from Global to shared memory without writing to registers first
* Thread Block cluster: On H100 SMs are organized hierarchically into groups. Thread Block clusters can cooperate across SMs in the same group and effectively share shared memory otherwise each warp will 
* Persistent Kernel: Imagine the whole network is a single kernel that streams in batches that way we don't have to launch multiple kernels
* TMA: Tensor Memory Accelerator (This just sounds like async loads to me?)
* Warp specialization: useful for reducing thread divergence. In particular look for primitives like `__shfl_down`, `__ballot`, or `__match_any_sync`
* Ping-pong schedule: NVIDIA has a scheduler that will schedule warpgroups automatically  but we can have 1 warpgroup do a gemm and another do a softmax in parallel. Anything that's not a matmul on modern GPUs will be slow and throughput on things like softmax will be very slow
* Epilogue fusion: Very common examplee is a scale or softmax after a matmul, this necessitates creating a lot of custom kernels but cutlass has a way to templatize this and make it easier
* wgmma: operates at warp group level with 4 contiguous warps (128 threads) performs a matmul C = A * B. B must be in shared memory, B must be in shared or register and C in register. It enables async matmul across tensor cores with different layouts
* [Epilogue Visitor Tree](https://dl.acm.org/doi/10.1145/3620666.3651369): Fuse custom epilogues by adding more epilogues to the same class (visitor design pattern) and represent the whole epilogue as a tree
* CuTE layout: layouts are mapping from memory locations to indexes. Since it's a function you can compose them, multiply them or divide them
    * Product: Think of the product as a way to "tile" one layout with another. It's like creating a grid where each cell is filled with a copy of one layout, and the arrangement of these cells follows the structure of another layout. (this can probably be nested as well)
    * Division: split(A,B) would split into buckets the first one containing all memory locations in A pointed at by B and the second the memory locations in B not pointed at by A

Cool identity: `a @ b = (a.unsqueeze(-1) * b).sum(dim=1)`