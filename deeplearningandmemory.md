## Memory Access patterns
https://en.wikipedia.org/wiki/Memory_access_pattern

Has impact on shared memory, locality of reference and cache performance

VTune and vectorization advisor let you detect GPU memory access patterns

### Patterns
* Sequential: amenable to prefetching
* Strided: skip in sequence
* Linear: linear combination of index, can be parallelized easily
* Nearest neighbor: popular in physical simulations
* 2d spatially coherent: spatial locality like textures, frame buffers, tile based deferred rendering
* Scatter: sequential reads with random writes
* Gather: random reads with sequential writes
* Gather-scatter: combined gather scatter
* Random: data structures with pointer chasing will be slow

One solution to all of the above is data oriented design


## Compute Intensity (FLOPs per memory access)
Arithmetic intensity  = FLOP/ MEMORY TRAFFIC

Find a way to calculate both of these in Tensorflow and memory to accelerator for GPU or IPU

## Static vs dynamic



## Branching vs predictable
https://en.wikipedia.org/wiki/Branch_predictor

## CPU vs GPU
GPU: wide SIMD/T, high memory bandwidth, low memory 
CPU: narrow SIMD, low meomory bandwidth, high memory

## Parallelism vs synchronization
* https://stackoverflow.com/questions/4844637/what-is-the-difference-between-concurrency-parallelism-and-asynchronous-methods#:~:text=Parallelism%20is%20a%20specific%20kind,Synchronous%20vs.&text=In%20sync%2C%20you%20write%20code,order%2C%20from%20top%20to%20bottom.

* https://indico.fnal.gov/event/23974/contributions/74722/attachments/46621/55992/Farrell_ExaTrkX_scaling.pdf

## How to map to MIMD
?