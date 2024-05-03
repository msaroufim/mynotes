# Glossary

Terminology I keep running into and forgetting

* Tensor cores: 15x flops for matmuls
* Async loads: Load directly from Global to shared memory without writing to registers first
* Thread Block cluster: On H100 SMs are organized hierarchically into groups. Thread Block clusters can cooperate across SMs in the same group
* Persistent Kernel: Imagine the whole network is a single kernel that streams in batches that way we don't have to launch multiple kernels
* TMA: Tensor Memory Accelerator (This just sounds like async loads to me?)
* Warp specialization: useful for reducing thread divergence. In particular look for primitives like `__shfl_down`, `__ballot`, or `__match_any_sync`


Cool identity: `a @ b = (a.unsqueeze(-1) * b).sum(dim=1)`
