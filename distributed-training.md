# Distributed Training libraries

## DeepSpeed
https://github.com/microsoft/DeepSpeed
https://www.deepspeed.ai/features/#simplified-data-loader
https://github.com/NVIDIA/Megatron-LM

10x larger models faster training, no code change

Distributed training, mixed precision, gradient accumulation, checkpointing

Uses torch JIT c++ extension loader to dynamically build at runtime

Zero redundancy optimizer
Zero offload

Smart gradient accumulation - gradients averaged locally and a single allreduce is done at the end of teh sequence - especially important when number of microbatchers per effective batch is large

Communication overlapping

Lamb optimizer (Layer adaptive)
Automatic gradient clipping and 16 bit optimization

1 bit ADAM - look into this in a bit more detail. Error compensation techniques applies to non linear optimizer like ADAM. Main idea is to keep the error around from the compression and use it for the updates. Compressed gradients help communication costs of distributed SGD
1 cycle learning rate scheduling - increase schedule and then eventually drop it
learning rate range test -

## Fairscale
https://github.com/facebookresearch/fairscale

Pipeline parallelism, Ampnet, model parallelism, sharded training, checkpointing wrapper and automatic mixed precision - all in Pytorch

Seems to be using a lot of code for core ops like gather or scatter from Pytorch Distributed 

Could use a model parallel example in the repo

## Gshard
https://arxiv.org/abs/2006.16668

Annotation API and extension to XLA compiler and provide an elegeant way to express parallel communication patterns without changing model code

Sparsely Gated mixture of experts, trained on 2048 TPU in 4 days

Talk a lot about communication overhead in model parallel

 
Compiler tricks are important here - see page. Dense paper I need to read this more carefully

Core ops
* Collective permute used for shard changes
* allgather: change sharded tensor to replicated one
* allreduce: summation over inputs
* alltoall: reshard one tensor from one dimension to another

They also talk quite a bit about the differences between SPMD and making some layers embarassingly parallel without having the compilation time explode

## Zero
https://arxiv.org/abs/1910.02054

Tricks
* Optimizer state and gradient partitioning by partitioning states across data parallel process instead of replicating them
* Activation partitioning 
* Constant buffer optimization - memory and network bound operations such as normalization and allreduce - fuse operands
* Contiguous memory optimization: activation checkpoint and parameter gradients to contiguous buffers to avoid memory fragmentation

Zero-offload - also splits data between CPU and GPU

## Pipedream
Profiling for auto model, data, pipeline parallelism. See the survey in local updates paper for more reminders

## Megatron-LM
https://github.com/NVIDIA/Megatron-LM

Model parallelism MegatronLM style - looks like it splits single layers into multiple machines and pipelines them? Most techniques are towards keeping GPUs compute bound and reducing communication overhead