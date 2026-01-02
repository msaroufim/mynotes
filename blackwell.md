## Dissecting blackwell

https://arxiv.org/abs/2507.10789

Interesting paper but strange choice to benchmark 5080 vs H100

Gaming cards are SM_120 whereas Blackwell cards are SM_100. Spark is SM_121 lol


## Compat guide

Nothing surprising https://docs.nvidia.com/cuda/blackwell-compatibility-guide/


## Blackwell tuning guide 

https://docs.nvidia.com/cuda/blackwell-tuning-guide/index.html

Uses HBM3e which is a new fancy DRAM technology with larger capacity and bandwidth https://newsletter.semianalysis.com/p/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm

Thread Block Cluster still important, remember a warp is 32 threads (how the hardware executes) and a thread block (i.e a block) is what the programmer decides. TBC allow distributed shared memory and cooperation between thread blocks. So TBC are a new layer of the hierarchy

L2 capacity is much larger at 126MB

CUDA reservers 1KB of shared memory per thread block

Also includes 5th generation NVLink (should read the dissecting NVLink paper by Stas to learn more)
* Read the NCCLX paper: https://x.com/StasBekman/status/1982861472024932409?s=20
* Demystifying NCCL: https://arxiv.org/abs/2507.04786

Code needs to be die aware since there's 2 of them. Do you shard computation or not? pipeline? how do you deal with consistency. It basically makes even a single GPU be about multi GPU programming

## Blackwell GEMM guide 
https://docs.nvidia.com/cutlass/media/docs/cpp/blackwell_functionality.html

Introduces tcgen05 which works over all legacy dtypes mostly offering 2-4x speedups with low bit dtypes and block scaling

There's a bunch of tables that specify alignment requirements. The dispatch policy as in given a spceific layout and shapes which specific kernel is called

TN → A is row-major, B is column-major
NN → A is column-major, B is column-major
NT → A is column-major, B is row-major
TT → A is row-major, B is row-major

Blas assumes column major by defualt so T is transpose and N is normal

(TODO: I wonder if there's a forced layout for the output as well, granted thats not as big a deal since there's no dynamic conversion cost we need to eat)

For the most part CUTLASS will just pick the fastest thing it can so we don't have to think about these choics too much

SM120 also had some added support but there are some more restrictions with no cluster support, only TN layout is supported

## Profiling

Probably becomes more importnat since it becames hard to visualize bottlenecks, today most of the instrumentation happens via CUPTI with UIs built on top like nsys or ncu. Libraries like kineto will just wrap cupti (set ranges, register callbacks) and create an exportable perfetto trace

## Application

There is interest in dropless MoE which are MoE that don't drop any tokens so there's not as much stability problems but the workload is more dynamic

But can reformulate MoE computation in terms of block-sparse operations and develop new GPU kernels https://arxiv.org/pdf/2211.15841 (TODO: look into this more deeply the high level  point is that this seems more efficient than padding)


## Notes

Why does blackwell have higher overhead? Did anyone get to the bottom of this?

Can always just use cuda graphs as a solution but this seems unsatisfying

As fasr as quantization goes which layers do people typically quantize and what's the lowst dtype people have done, presumably router is more numerically sensitive

With NVL72 just make sure parallelism dimension is less than 72, this machine seems really nice and i should get my hands on one

Within batch overlap is important otherwise gating -> dispatch -> expert compute -> combine is a serial operation. so we can overlap within the same microbatch to get better end to end latency. Big thing is it helps us better hide the all to all latench (and i wonder if there's a profiler that shows this nicely)

The above kind of overlap happens purely with cuda streams and chunked dispatch 

Pipeline parallelism would be an additional kind of hiding where you pipeline across batches

Packed activations: After gating we can choose to pad everything up to max_e n_e where n_e is the number of tokens for expert e - so we can instead choose to pack

Need kernels for EP - need to keep some SMs for comms and others for communication using symmetric memory

