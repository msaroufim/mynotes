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

TMA transforms - tile your input

You've worked on a lot of languages DEX, IIC Hopper is your lowest level one yet

Presumably you wrote a new DSL for peoplee to write more new kindds of kernels and not just FA3 so what do you think people should be writing

What about blackwell?

Take a step back what did you feel existing languages for GPUs were missing?


# Flash Infer
