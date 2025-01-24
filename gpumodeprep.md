## Mosaic GPU

https://www.youtube.com/watch?v=tnADC2XuAr0&ab_channel=Triton

C++ metaprogramming is too hard (what do you mean by its not great?)

Compilers are hard to work and adapt

New pallas backend for hopper and onward

MLIR based tracing DSL

Small hackable python core (only 3.5K LOC)

1 wargroup (1 SM) = 1 mosaic thread and provides lots of warpgroup level helpers

You need to specify what kind of layout to choose and write to

as_strided()

Mosaic is intended to be a language that machines write and not humans, curious how you think about the ergonomics

Async copy (TMA) -all of the arguments stya the same except for an argument that sets shared memory requirements

How do you go about supporting new features in GPUs, how much time do you spend

Why MLIR?

TMA transforms - tile your input once and share it everywhere

You've worked on a lot of languages DEX, IIC Hopper is your lowest level one yet

Presumably you wrote a new DSL for peoplee to write more new kindds of kernels and not just FA3 so what do you think people should be writing

What about blackwell?

Take a step back what did you feel existing languages for GPUs were missing?

Why expose striding, seems like you also loved this pattern in pytorch


# Flash Infer

Sparse and dense attention kernels
Cascade attention for hierarchitcal kv cache
Bring your own attention variations
customizable attention
Have a flag to to aot compile kernels
codebase is 60% cuda

Cascade inference decouples attention of shared prefix and unique suffixes , dispatch attention on different kv subsets (still dont fully understand the trick)

Fused kernels for sampling

Cascade and activation implemented in Triton
* Fused silu and multiplication
* Merge state (cascade for dividing and conquering kv cache)

Fp8 support

What's next? Mx support

Rest in CUDA

A lot of functions are compiled

Quantization sueus numpy packed bit array

Sets which args are mutated and each arg has its own unique name

I noticed for example in your aot_build_utils you have a lot of utilities that manipulate strings, could you talk a bit more about this.

Can you talk more about your JIT vs AOT machinery?  nvcc vs nvrtc

FLexible attention patterns, is the idea to metaprogram again?

Header only libraries are more convenient since don't need to build and link and you can uses One Definition Rule (ODR) as a heuristics when authoring such a library


```
// can be header only:
class Calculator {
    inline static int callCount = 0;

    public:
        inline int add(int a, int b) {
            callCount++;
            return a + b;
        }
};

// cannot be header only:
class Database {
    static int connections;  // needs definition in .cpp
    void connect();         // needs implementation in .cpp
    FILE* file;            // requires linking against stdio
};
```
