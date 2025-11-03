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
- 4 bits (1 sign, 2 exponent, 1 mantissa) plus 1 shared power-of-two scale per 32 value block
- 4 bits (1 sign, 2 exponent, 1 mantissa) plus 1 shared FP8 scale per 16 value block