## The reduction is a matmul trick

https://www.twosigma.com/articles/a-workaround-for-non-determinism-in-tensorflow/

```python
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
a = input.reshape(1, -1)
b = torch.ones_like(a)
deterministic_sum = torch.matmul(a, b.T)
print(deterministic_sum)
print(torch.sum(input))
```
This is actually not an issue with PyTorch but seems to have been an issue with TF1

## Misc ideas

Found this trick from this NVIDIA talk https://developer.download.nvidia.com/video/gputechconf/gtc/2019/presentation/s9911-determinism-in-deep-learning.pdf

This blog also describes how both reductions and additions in TF were non deterministic because they used atomics

Atomics force "correctness" but they don't have any guarantees on ordering

Some cool ideas in the above blog like having a determinism debug tool that adds monitor at important parts of the code and sees how they differ based on commit hashes

## Floating point non associativity 

https://arxiv.org/pdf/2408.05148

A paper that studies that atomic operations cause non determinism in pytorch 

They mostly study that the impact of floating point non associativty can cause unacceptably large losses when training models and when doing inferences

There is no evidence that that variability follows gaussian distribution and there not enough details from NVIDIA to know for sure

OpenMP has a concept of ordered reductions

Reductions naively use atomics but can be made deterministic using different strategies
* Two passes with final reduction on CPU: Transfer partial results to CPU and then CPU performs final sum in conssitent order. You could also do it on GPU but the con is you need to launch another kernel because you need to do a global synchronization barrier
* Counter based approach: Use a counter to track completed thread blocks and then then enforce an order for accumulating partial sums based on block ID instead of completion time

## Sources of non determinism 
https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/RML18-nagarajan.pdf

There are many causes
1. GPU algorithms
2. Environment like RL that has some probabiliic changes
3. Policy can be stochastic
4. Network initialization
5. Data loading

All of these need to be deterministic for training

## Deterministic atomic buffering
https://microarch.org/micro53/papers/738300a981.pdf

## Non determinism of determinisic llm settings
https://arxiv.org/html/2408.04667v5

INtroduce their own metric TARn@N. for total agreement rate at N runs over raw output

Most of the experiments focus on how even at temp=0 results weren't determinsitic

A bit of a vague post mentions briefly that things like prefix caching, chunk prefilling and continuous batching can lead to non deterministic behavior

## Nvidia floating point guide 
https://docs.nvidia.com/cuda/floating-point/index.html

## Deterministic checkpointing 

https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9796431

This paper mostly seems to focus on sources of RNG and fixes a different seed per example

Otherwise for checkpoint replay insatead of sa ving the state of the data loader they replay it up to how many epochs or samples were done so far and then recover.  (This seems costly)

Idk why this paper focuses so much on adversarial attacks

## Survey on. reproducibility
A lot of people seem to care https://arxiv.org/pdf/1511.04217 but otherwise didn't much that was new from this paper. It's also unclear if some people meant determinism

This isn't a survey per se, it's actually more of a questionnaire

## What every CS should know about floats
A classic https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf

Has some

## NVIDIA Odds and ends
https://docs.nvidia.com/deeplearning/cudnn/backend/latest/developer/misc.html 

This doc page has a bunch of stuff but most importantly has examples of non determinsitc ops that require tomics. Most important ones are 
1. Convolution and pooling related: With max pooling you go from 1 output value to N input values, getting the right ones requires atomics
2. CTC_Loss: Which is a forgiving loss function used to map variable length input and output sequences. This requires atomics because multiple threads are computing gradients for different alignment paths that share nodes in the computation

## Cudnn paper
https://arxiv.org/abs/1410.0759

OG paper just had
1. forward and backward for convolution
2. Sigmoid, rectified linear, hyerbolic tangent
3. numerically stable softmax
4. maxa pooling
5. Optional broadcasting

They show how you can lower a convolution into a multiplciocation 

They also show a caffe integration

It's a cool paper but they don't actually discuss reproducibility


## NVIDIA float compliance 
https://docs.nvidia.com/cuda/floating-point/index.html

 IEEE 754 standard in 2008 also introduced FMA, also introduces rules for rounding rules

FMA basically makes it so we only need a single rounding step and that is more correct then introducing 2 rounding steps

`rn(X * Y + Z)` instead of `rn(rn(X*Y) + Z)` 

Rounding always happens when either
1. we're converting from one dtype to another
2. dealing with excess precision such as `+, -, x, /, FMA`

```
Standard multiply-then-add:
float32 × float32 → float32 (rounds to 24-bit mantissa)
float32 + float32 → float32 (rounds again)
= 2 rounding errors

FMA:
float32 × float32 → internal 48-bit exact product (no rounding)
48-bit product + float32 → float32 (only 1 rounding)
= 1 rounding error
``` 

Naively you'd think FMA would be slower because of the intermediate overhead but it's a single instruction with dedicated hardware units. It does cause reproducibility issues if the increased precision is not desirable and makes it so depending on which compiler flags we enable the results might not be reproducible

Machine differences could also cause issues. Unit tests that pass on CI (no FMA) fail on production (has FMA)

Dot product can be computed using FMA - 

for i in range(1,, 4)
  t = rn(a_i x b_i + t)
return t

There are 4 rounding modes
1. Round to nearest, ties to even
2. round to zero (bankers rounding)
3. round to floor
4. round to ceil

Bankers rounding assumes digits are random but if someone can exploit them in an attack called salami slicing

For instance instead of keeping small values around which need special handling for CPU we can flush denormals to just round them to 0

GPU arithmetic units have both fast passes that break IEEE compliance and slow ones (~10x slower) - so compiler choices can affect hardware unit choice which in turn affects reproducibility

In x86 the rounding choice is global but in cuda it's basically per instruction so you'd have something like `__fadd_rz(x,y)` round to zero addition this simplifies things like not needing trap handler or status register

You can choose which rounding mode to use if you just call the low level instrinsic otherwise the compiler will decide for you. in practice it just uses round to nearest most of the time

Since NVIDIA makes different choices on how their floats work then there is no hope to have reproducubility with CPU. In addition, CPU vs GPU will have different parallelism strategies that will also affect numerics (CPUs have much fewer threads)

they also recommend computing results in higher precision 

NVIDIA recommends that people porting their code study numerics and not just assume differences in results mean a bug

when doing fma rounding we use float64 to add float32 because we can use extra bits t o
1. determine rounding
2. handle alignment shifts for different exponents
3. safety margin



## siboehm articles

https://siboehm.com/articles/23/Inlining-FMA-FP-consistency

Inlining can affect numerics, even without FMA or fast math shenanigans

```cpp
float foo(float x) { return x * x + x; }
float result = foo(a + b);
```

On x86 intermediates will be in 80 bit registered whereas if we're calling another function then we have to cast it down to 32 or 64 bit numbers

Compiler could also reorder things differently or have some compiler pass that it runs like dead code elimination. Inlining can typically help the compiler do more because optimizations are at the function boundary.


Without FMA: `RoundToFloat32(RoundToFloat32(a * b) + c)`
With FMA: `RoundToFloat32((a * b) + c)`

IEEE standard does not specify what's the correct number here

It's possible in some languages that you have to explicitly call an FMA function

What happens if you call fma on harwdware that doesnt support it

Whether an FMA instruction can be fused into something else can also affect numerics

Some compilers will have FMA mean: run FMA only if it's faster otherwise default to without FMA semantics


https://yosefk.com/blog/consistency-how-to-defeat-the-purpose-of-ieee-floating-point.html


IEEE is fine for most people except those few nasty edge cases that we all need to think about

> This implies a general way of solving this sort of problem: find what the optimizer does by looking at the generated assembly, and do it yourself in the source code. This almost certainly guarantees that debug and release will work the same

Another approach is to get in the way of the compiler and force indirections that make unintended optimizations hard. 

In other cases a lot of compilers will have flags to disable specific optimizations by default

 IEEE FP philosophy – intermediate results should be as precise as possible; - this goes against what some users want, see for example the anthropic blog postg https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues

 What's interesting is that if youre using debug builds you wouldn't upcast to 80 bit registers lol 

https://nhigham.com/2018/12/03/half-precision-arithmetic-fp16-versus-bfloat16/

bfloat16 can make certain series converge when they should diverge lol

https://nhigham.com/2015/10/08/the-rise-of-mixed-precision-arithmetic/

Comparing to higher precision baseline is often good enough

Unstable low bit algorithms can be made stable by just using higher precision in a few places and there's a history of this pre deep learning https://epubs.siam.org/doi/10.1137/130911561

IEEE said that fp16 is a storage only dtype not compute one

Amazing author but none of his books seem available online anymore https://www.youtube.com/watch?v=L_lgdbYSGxY

Floats are cursed blog


https://www.siam.org/publications/siam-news/articles/a-multiprecision-world

There are lots of references to rounding error analysis which should give a bound on the expected error of a specific algorithim example  The usual rounding error bound for the inner product of two vecor is nu (n is size of vector and u is the unit roundoff)

For FP32: ε ≈ 2^(-24) ≈ 5.96×10^(-8)
For FP16: ε ≈ 2^(-11) ≈ 4.88×10^(-4)

|fl(x^T y) - x^T y| ≤ nε|x|^T|y| + O(ε²)
relative error ≤ nε · (|x|^T|y|) / |x^T y|

https://claude.ai/share/c35f5845-0033-4508-8cd7-75302927d105


More things to read

https://randomascii.wordpress.com/2013/07/16/floating-point-determinism/
https://fabiensanglard.net/floating_point_visually_explained/
https://nhigham.com/2020/05/04/what-is-floating-point-arithmetic/

My hobby: injecting code into other processes and changing the floating-point rounding mode on some threads


Pitfalls of verifying floats https://arxiv.org/abs/cs/0701192

On floating point determinism https://www.yosoygames.com.ar/wp/2013/07/on-floating-point-determinism/
## Float semantics

FP32 (float32)
- What: 1 sign, 8-bit exponent, 23-bit mantissa (full precision/range baseline)
- Storage/compute: stored as FP32; matmuls/conv run as FP32 unless TF32 enabled
- Accumulation: FP32

FP16 (IEEE half, float16)
- What: 1 sign, 5-bit exponent, 10-bit mantissa (narrow range, decent precision)
- Storage/compute: cast or autocast to FP16
- Accumulation: usually FP32 on Tensor Cores
- Use: fast but finicky for training; needs loss scaling
- Gotcha: under/overflow due to small exponent

BF16 (bfloat16)
- What: 1 sign, 8-bit exponent, 7-bit mantissa (FP32-like range, coarser precision)
- Storage/compute: cast or autocast to bfloat16
- Accumulation: FP32 on modern GPUs/TPUs
- Use: training default on modern hardware; usually no loss scaling
- Gotcha: slightly noisier than FP16/TF32 per multiply due to 7-bit mantissa

TF32 (TensorFloat-32) \u2014 NVIDIA Ampere+
- What: COMPUTE MODE for FP32 matmul/conv: inputs rounded to 8e/10m, accumulate FP32, output FP32
- Storage: tensors remain FP32 in memory
- Use: drop-in speedup for FP32 models without changing dtypes
- Gotcha: slightly less precise multiplies than FP32

FP4 is well explained here 
https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/

In particular

Feature	FP4 (E2M1)	MXFP4 	NVFP4 
- FP4 (E2M1): 4 bits (1 sign, 2 exponent, 1 mantissa) plus software scaling factor
- MXFP4: 4 bits (1 sign, 2 exponent, 1 mantissa) plus 1 shared power-of-two scale per 32 value block
- NVFP4: 4 bits (1 sign, 2 exponent, 1 mantissa) plus 1 shared FP8 scale per 16 value block


## Interesting threads from twitter

https://x.com/iannuttall/status/1984531393062240611

Codex had a regression with numerics on older hardware so just dropped it since it made their evals bad

https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook#scaling-surprises

Some interesting happenings
- Throughput would drop when a node died because data loader would lose its local data
- Random access data loader causes fewer loss spikes because one bad example could tank the gradients of one batch
- Sample packing also likely changes numerics but can improve efficiency, it makes the gradient of each example less clean

Defeating the LLM training-inference mismatch via fp16
https://arxiv.org/abs/2510.26788

RL is inherently unstable, existing solutions mostly rely on patches to importance sampling because everything is inherently off policy

BF16 causes large errors while fp16 is more precise (this matters less for pretraining). This paper is mostly vibes based in particular they fixed the instability with fp16 across VLLM and FSDP but it's not clear what the root cause beyond some handwavy arguments of fp16 being more precise



