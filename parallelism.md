# Notes from Chris parallel programming class
https://www.youtube.com/watch?v=EP5VWwPIews&ab_channel=ParallelComputingandScientificMachineLearning

Great summary here

## Useful reference

Things I want to learn more about
Chris’ Julia parallelism class
Lithography
Material sciences - find a book, ask Sohini
Chip manufacturing - Linus has nice videos on AMD pins and 7nm Intel processor issues which goes into  https://www.youtube.com/watch?v=xPlLQkKyhOU&t=73s&ab_channel=Techquickie 
EUV lithography where you can use light and mirror to etch thinner circuits https://www.youtube.com/watch?v=ttbaaI5xUcg&frags=wn&ab_channel=ASML
Really enjoying the techquikie YT channel by linus https://www.youtube.com/channel/UC0vBXGSyV14uvJ4hECDOl0Q 

## Cool julia tricks

Goes over scope the different kinds of parallelism
Explains how to create new Julia environments, test cases, activate environment and create new packages with the PkgTemplated package
Backslash lets you use Unicode characters for math easily \approx for inexact inequalities and just add a @test macro for asserts and it’ll tell you whether something is true or false
Then can run test Packagename to see if all the tests pass
Dev to create a new package and activate to activate a new environment
Export the functions you want your users to export so they don’t need to call your libraryname.functionname
Has a whole separate tutorial on this stuff https://www.youtube.com/watch?v=QVmU29rCjaA&ab_channel=TheJuliaProgrammingLanguage
cd(@__DIR__) using Pkg Pkg.activate(.)

## Threading

Threads share a heap but don’t share a stack so need to think about when operation is thread safe or not and have branching if on task id or memory so that nothing gets shared and you can actually do concurrent computation
Most languages also have task management @thread.spawn() and then fetch
Julia has both dynamic and static scheduling - dynamic scheduling is usually slower but it’ll batch slow and fast computations together so all threads finish roughly together
Unevenly distributing work will make everything slow

## SIMD

There are levels starting from SIMD parallelism within same process to multithreading where you have multiple vcpus with their own stacks in a single process. To manage shared memory in heap can use spinlocks or mutex either observer or observing pattern
Threadripper has 32 cores - NVIDIA 2080TI has 4532 cores - clock speed on GPU is much smaller ~1GHz GPU vs 2-3GHz on CPU
SIMD is vectorization at the instruction level - each CPU instruction processes multiple data elements.


## GPU

SPMD is a much higher level abstraction where processes or programs are split across multiple processors and operate on different subsets of the data.
Also sending data to GPU is slow
But even with all downsides having 10K cores is great
CPU memory is 16-32GB of RAM on personal all the way to 1TB in HPC 
GPU memory 

GPUs severely slower on fp64 vs fp32
IN SPMD you also just use an index similar to threads index = blodID.x * blockdim.x + threadId.x

Array based computing model -> Cuda(A) * Cuda(B) which is what end users actually do in languages like Pytorch or Julia via Multiple dispatch

Don't bother doing GPU unless operation takes at least 50-100 microseconds

Xeon Phi Accelerator - another SPIMD archtecture. OpenCL is the language for it, TPUs and GPUs

TPUs use bfloat16, dynamic range is same as 32 bit float but the significant bits is dramatically lowered - wikipedia for details. Fast and accurate and specialized in only linear algebra. Check out catostrophic cancelation which has loads of examples of how TPUS can get 0 everywhere

## Multiprocessing

Message passing
Use multiple processes
use Distributed and addprocs and define on all processes something then do remote call to another processes - similar to thread.spawn
I'm going to send you data, please do this operation and this gives the sender a future - it's a guarantee that when you access you'll get the data

2 ways
1. Task based parallelism -> computational graph like tensorflow, DAG for computation
2. Master worker model

## Distributed array parallelism
Similar to how arrays are multiplied on GPU. DistributedArrays

## MapReduce
Do same function on every value of an array then reduce at a master machine


## Random note
Neural architecture search is already performed by ML engineers when they look at Github, Twitter, Arxiv for good ideas around best algorithms
Maybe some way we can specify a task and a compiler will generate best model, hyperparams and parallelization strategy but this seems unlikely given you can't do any of this stuff purely statically. You need to run loads of algorithms which is time consuming and expensive.

ML engineers now basically need to be expert dev ops that can try out lots of experiments really quickly