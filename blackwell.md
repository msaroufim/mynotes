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

