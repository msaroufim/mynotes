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

## NVIDIA Odds and ends
https://docs.nvidia.com/deeplearning/cudnn/backend/latest/developer/misc.html 

## Cudnn paper
https://arxiv.org/abs/1410.0759

## NVIDIA float compliance 
https://docs.nvidia.com/cuda/floating-point/index.html

