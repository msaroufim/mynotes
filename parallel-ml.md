# Survey paper
https://arxiv.org/pdf/1802.09941.pdf

Scope
1. Foundations of ML, SGD, work and depth model, MPI
2. Generalization vs utilization
3. Concurrency
    * Operators
    * Networks
    * Training

## Related work
* Overviews of scaling deep learning
* Hardware architecture that scale
* Optimization methods
* Hardware acceleators including FPGAs
* How to scale various layers

Other surveys in the field focus on applications of deep learning[175]
, neural networks and their
history[143,154,209,236]
, scaling up deep learning[17]
, and hardware architectures for DNNs[113,138,225]
.
In particular, three surveys[143,209,236] describe DNNs and the origins of deep learning methodologies from a historical perspective, as well as discuss the potential capabilities of DNNs w.r.t.
learnable functions and representational power. Two of the three surveys[209,236]
also describe
optimization methods and applied regularization techniques in detail.
Bengio[17] discusses scaling deep learning from various perspectives, focusing on models, optimization algorithms, and datasets. The paper also overviews some aspects of distributed computing,
including asynchronous and sparse communication.
Surveys of hardware architectures mostly focus on the computational side of training rather than
the optimization. This includes a recent survey[225]
that reviews computation techniques for DNN
operators (layer types) and mapping computations to hardware, exploiting inherent parallelism.
The survey also includes discussion on data representation reduction (e.g., via quantization) to
reduce overall memory bandwidth within the hardware. Other surveys discuss accelerators for
traditional neural networks[113]
and the use of FPGAs in deep learning[138]
.


## Weight update rules
They go over a survey of learning rate vs adagrad vs rmsprop etc..
Then batching

Authors also go over an example of which architectures people used over time and as of 2017 its mostly GPUs and an increase in multiple nodes

In general datacenters now have much more improved bandwidth in data centers but network is generally slower than intra machine communication

The majority of deep learning clusters today actually use MPI or Sockets for the most part

## Parallelism
Every computation can be modeled as a DAG where vertices are computations (Work) and edges are data dependencies (Depth longest path) and then you can determine the computational complexity using this model.

Some layers like convolutions can be optimized with locality considerations as such as MPI Neighborhood collectives also called sparse collectives https://cvw.cac.cornell.edu/mpiadvtopics/neighborhood

# Generalization vs utilization
Larger batches help initially but after some point stop helping
There's a lipschitz constraint for what the optimal batch size is
There's scheduling constraints to find a better batch size over a training run

Have a nice table about the work depth characteristic of each kind of operator

Post 2015 a lot of deep learning research has shifted towards more energy efficient methods (outside of transformers)

# How to optimize layers
* Dense layers: use matrix libraries because its a matmul
* CNN: Look at the survey in more detail
* RNN: Can do async in a single recurrent layer or accross multiple layers


# Parallelism Model, Data and Pipelining

Below, we discuss three prominent partitioning strategies, illustrated in Fig. 14: partitioning by input samples (data parallelism), by
network structure (model parallelism), and by layer (pipelining).

Overlap idea comes out here again

## Model
To reduce communication costs in fully connected layers, it has been proposed[174]
to introduce
redundant computations to neural networks. In particular, the proposed method partitions an NN
such that each processor will be responsible for twice the neurons (with overlap), and thus would
need to compute more but communicate less.
Another method proposed for reducing communication in fully connected layers is to use
Cannon’s matrix multiplication algorithm, modified for DNNs[72]
. The paper reports that Cannon’s
algorithm produces better efficiency

## Pipelining
Distbelief and Project ADAM mix and match data and model parallelism + pipelining

Reread the original tensorflow paper https://arxiv.org/pdf/1603.04467.pdf
They discuss pipelining, model parallelism vs data

 Pipelining can be viewed as a form of data parallelism, since
elements (samples) are processed through the network in parallel, but also as model parallelism,
since the length of the pipeline is determined by the DNN structure


Lastly, the DistBelief[56] distributed deep learning system combines all three parallelism strategies.
In the implementation, training is performed on multiple model replicas simultaneously, where
each replica is trained on different samples (data parallelism). Within each replica (shown in Fig.
17c), the DNN is distributed both according to neurons in the same layer (model parallelism), and
according to the different layers (pipelining). Project Adam[39]
extends upon the ideas of DistBelief
and exhibits the same types of parallelism. However, in Project Adam pipelining is restricted to
different CPU cores on the same node.


# Distributed optimization
* Centralization parameter servers
* SYnchronization
* Model consolidation
* Optimization algorithms


# Useful references
* Scheduling multi threaded computations by work stealing (MIMD): https://dl.acm.org/doi/10.1145/324133.324234
* 


### Scaling Deep Learning by Bengio https://arxiv.org/pdf/1305.0445.pdf

#### Async SGD
* GPU
* Multicore performance on CPUs
* Asynchronous SGD, occasionally sync weights, large minibatches, tradeoff between communication cost and computation cost
* Related theory paper discussing tradeoff between communication and computation cost: http://132.206.31.57/sites/default/files/cdc2012_main.pdf

#### Sparse updates
* In general we know that dropout and pooling are good and reduce the number of updates you actually need to make

#### Conditional computation
* Learn to drop weight using something like a decision tree, gives sparse gradients and helps the convergence of hard mixture of experts


#### Optimization issues
Layer wise pretraining One of the early hypotheses drawn from experiments with layer-wise pre-training as well as
of other experiments (semi-supervised embeddings (Weston et al., 2008) and slow feature analysis (Wiskott and Sejnowski, 2002a; Bergstra and Bengio, 2009))


Greedy Layer-Wise pretraining: https://papers.nips.cc/paper/3048-greedy-layer-wise-training-of-deep-networks.pdf 

Diminishing returns with larger network


### Great survey paper on scaling deep neural networks
https://arxiv.org/pdf/1703.09039.pdf