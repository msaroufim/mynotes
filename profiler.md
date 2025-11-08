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