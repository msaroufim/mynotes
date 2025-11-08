Some ideas
1. Sampling based profiler so we can keep something always on (similar to RL-Scope and DeepContext)
2. Profiling overhead should be xcluded from report
3. Make cpu overhead clearer to understand. Maybe even a macro mode that shows cpu overhead, amount of naked transfers
4. Better defualts for wait, warmup, active, this would be BC breaking
5. Kills torch.utils.benchmark, its number seem off and we should perhaps just tell people to use do_bench in triton
6. Automatically add syncs for people?? (This seems like a no but worth thinking about)
7.Show launch latency of each kernel explicitly in each place
8. Compiler is useless if we're using torch.compile, so we need to roll things up a bit better
9. DeepContext seems to show hotspots as well
10. Espeially for RL, whole model profiling seems crucial, the bottlenecks aren't just PyTorch
11. Add regions in the profiler (I beleive those already exist just not 100% sure)
12. We could kill tensorboard and use our own visualizer or just recommend people use W&B
13. Have the profiler export an html trace as well so they can just open it and not have to deal with using another tool
14. PyTorch should just have a function like do_bench(), the footguns we have are insane
15. Revive HTA and make it more first class
16. Closer integration with ncu
17. Study nsys more


## Misc issues from reading github

18. Interesting we have a (broken flop counter in the profiler) https://github.com/pytorch/pytorch/issues/69782 - we should perhaps revive and maintain Horaces flop profiler https://github.com/pytorch/pytorch/issues/69506
19. Get energy consumption (maybe people dont care as much these days IDK) but its a good proxy for cost https://github.com/pytorch/pytorch/issues/65985
20. TF32 is incorrect https://github.com/pytorch/pytorch/issues/153901
21. A common issue https://github.com/pytorch/pytorch/issues/120235 around how the profiler breaks when you load a model
22. Goals of kineto relative to pytorch profiler arent super clear to me