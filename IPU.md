# IPU

Graph processor for ML


## IPU intro video
https://www.brainshark.com/1/player/en/graphcore?pi=zI5zd8WVwzYUeXz0&r3f1=&fb=0

Very large amount of on chip memory
High performance floating point computations
Multiple chips can communicate with each other
600 MB of on chip memory
IPU communicate with CPU via PCIe (I believe same interface is used for GPU)
C2 Accelerator gives graet performance on REsnet it has 2 IPUs connected to each other
Data access latency is important as well as parallel input such as LSTM
IPU contains many independent processors with 1216 tiles 
Each tile contains memory and a processor unit, 300MB of memory stored accross chips, no shared memory
Each tile processor is its own CPU. Each tile has multiple hardware threads. Can do single presision or double
All tiles work synchronously to execute a program - bulk synchronous parallel (BSP execution)
Exchange, compute, wait for sync, sync - exchange takes the most time
Each tile contains a copy of the control program
Code and data are in the same location
High end CPU like https://www.amazon.com/AMD-Ryzen-3950X-32-Thread-Processor/dp/B07ZTYKLZW - has 72MB of cache. Graphcore has 300MB per IPU
To program IPU there are poplar tools, user environment are standard deep learning libraries
Lowest level part of the stack is the PCIe drivers then Poplar drivers then Poplar C++ libraries then some translation layer to popular deep learning libraries
NO CODE CHANGES TO RUN ON IPU - this is kinda crazy
Tensorflow graph -> XLA graph -> Poplar graph then runs on accelerator
XLA is a Tensorflow library to accelerate linear algebra stuff https://www.tensorflow.org/xla
Pytorch support for XLA can't be done in user space but as of January 2020 some people are working on it https://www.kaggle.com/c/flower-classification-with-tpus/discussion/129820

## Programmers guide
https://www.graphcore.ai/docs/ipu-programmers-guide

Each tile can be either a worker or supervisor and each tile will do floating point computation (32 bit and 16 bit)
There are many ML tasks where you can do fine even with 1 bit precision. Specifically for embedded ML lower precision is more popular because it's cheaper
Stochastic rounding, round numbers up or down with some probability to avoid bias in rounding mechanism
Chip uses SRAM which is more expensive and faster than DRAM - SRAM is typically used for CPU cache. So IPU basically has a giant distributed CPU caches
Typical IPU applications operate on variables that are large multi-dimensional arrays of data (tensors); these can be distributed across the tiles, with parts of each variable stored on different tiles.

Can represent computation as a graph
* Edge: Read is either a read from local memory or a communication to another tile
* Vertex: represents some arithmetic computation

How to execute code in parallel in 3 steps
1. Local compute
2. Global sync
3. Data Exchange

Most time is spent in compute then exchange then sync and also waiting
Each tile also loads a control program which helps sync all the chips (the  user doesn't need to do this)

ML frameworks -> ML accelerator backend such as XLA or PopArt -> C++ code which calls Poplar -> LLVM -> Device code -> PCI Express -> IPU


## How to Tensorflow from IPU
https://www.graphcore.ai/docs/targeting-the-ipu-from-tensorflow

* Needs Ubuntu 18.04, Python 3.6, Intel AVX-512 (SIMD with 512 bit instructions)

How to run a basic graph
1. Add Tensorflow 1.0 libs
2. Boiletrplate to configure IPU for the system, ideally this should be streamlined
3. Setup tensorflow graph
4. Deploy graph on IPU
5. Create a session where you instantiate the nodes in the graph

These libaries also make a simulator available

If you want control flow code in your network like in the example of an RNN then you need to compile your model using XLA

You can shard a neural network trivially over multiple IPUs by just specifying NUM_IPUS

There's all sorts of helper functions to help debug IPUs, trace them, see what the supported functions are and shard

## Poplar and Poplib libraries
https://www.graphcore.ai/docs/poplar-and-poplibs-user-guide

* Object code per tile
* The control-program code from your graph
* Code to manage exchange sequences
* Initialised vertex data
* The tensor data mapped to that tile

Communication from host to IPU happens via data streams

Given some TF graph you can cut it into parts and move those individual parts to different tiles, how you do so what is good vs bad is an open question for me

## Open questions
* When does the CPU become a bottleneck for IPU and vice versa?
* Common transcendentals - why should I care about this?
* Read the Leslie Valiant BSP paper https://dl.acm.org/doi/10.1145/79173.79181
* Understand Poplar
* Is Tensorflow 2.0 support coming? It feels like static graphs are really needed to make this work
* I don't understand how tiles are mapped, how data and code are sent to the various IPUs and how the sync works exactly
* In the RL example, the only change was using the ```PoplarRNN```, how much more perf can you squeeze out? What's the perf like if you use the default RNN and does an IPU still help?
* Why would I want to replicate graphs? RNN??
* I may need some C++ refresher to link libraries orrectly

## Code

### Hello Poplar

```c++
 #include <poplar/Vertex.hpp>

using namespace poplar;

class AdderVertex : public Vertex {
public:
  Input<float> x;
  Input<float> y;
  Output<float> sum;

  bool compute() {
    *sum = x + y;
    return true;
  }
};
```
### Reinforcement Learning example
https://github.com/graphcore/examples/blob/master/applications/tensorflow/reinforcement_learning/rl_benchmark.pys

* uses the tensorflow plugin library for custom ops
* Environment in this code base is fitting random data, shouldn't be too hard to generalize this for Open AI gym. 
* Benchmarking code is skipping XLA compile step, seems like a common trend in graph benchmarking code
* Code looks alsmost identical to vanilla tensorflow code, the only exception is using PopnnLSTM, otherwise it's only native tensorflow code that's used


#### TODO:
* Add support for Open AI gym or PyBullet - some cool environment NOT random data
* Show actual benchmarks vs CPU and GPU code (probably only CPU for RL stuff will be enough)
* Read the BERT example since it looks like one of the more complex ones https://github.com/graphcore/examples/tree/master/applications/popart/bert 

### Python API
https://www.graphcore.ai/docs/popart-python-api-reference

You can wrap an ONNX model either for inference or training to deploy. Deployment doesn't look different from vanilla deployment in Tensorflow but I guess instead of using Tensorflow serve we can use the popart libraries

### Command Line tools
https://www.graphcore.ai/docs/ipu-command-line-tools

This helps you figure out how much on device memory and the activity that an IPU has. Typically each hardware vendor will have their own library here anyway so nothing too surprising. 

There is room for visualization tools like HWMonitor to debug, monitor and alert on IPU performance.

## References
* https://www.graphcore.ai/developer-documentation