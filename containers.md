Sandboxes are so hot right now https://sprites.dev/

Goals are often to provide guarantees of isolation, security and finally having low overhead and cold starts

Modal uses gvisor

Modal https://modal.com/blog/gpu-health - interesting issues on how different vendors vary wildly in quality of perf, tons of passive microbenchmarking and also at startup microbenchmarking help avoid some of these issues. One of their most recommended tools is dcgmi

Technologies to look at 
* crosvm
* e2b
* daytona
* gvisor + nvproxy
* kata
* firecracker
* in slurm: pyxis + enroot

Whatever happened to MIG? does it make kernel microbenchmarking possible? (probably no)