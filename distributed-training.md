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

1 bit ADAM
1 cycle learning rate scheduling - increase schedule and then eventually drop it
learning rate range test -

## Fairscale

## Gshard

## Zero
https://arxiv.org/abs/1910.02054

Tricks
* Optimizer state and gradient partitioning by partitioning states across data parallel process instead of replicating them
* Activation partitioning 
* Constant buffer optimization - memory and network bound operations such as normalization and allreduce - fuse operands
* Contiguous memory optimization: activation checkpoint and parameter gradients to contiguous buffers to avoid memory fragmentation

Zero-offload - also splits data between CPU and GPU

## Pipedream

## Megatron-LM
https://github.com/NVIDIA/Megatron-LM

Model parallelism MegatronLM style - looks like it splits single layers into multiple machines and pipelines them? Most techniques are towards keeping GPUs compute bound and reducing communication overhead