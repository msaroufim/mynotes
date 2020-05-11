# Differential Equations in Julia

Anything that varies over time can be modeled with a differential equation

## Github issues
#### https://github.com/SciML/DiffEqFlux.jl/issues/48
* Tracked array: Array represents the weights of some neural network, tracked array makes it clear that we want to backprop these weights
* Keep track of this issue and when I can solve it means I understand hwat's going on a bit better


#### https://github.com/SciML/OrdinaryDiffEq.jl/issues/1064
Lie group differentiator https://arxiv.org/pdf/1207.0069.pdf 

#### SciML https://sciml.ai/2020/03/29/SciML.html
* We're seeing a lot more scientific code show up in ML
* Traditional optimizers like SGD and ADAM don't work that well for physics informed or scientific code

Has solvers for many kins of differential equations

* Discrete equations (function maps, discrete stochastic (Gillespie/* Markov) simulations)
* Ordinary differential equations (ODEs)
* Split and partitioned ODEs (Symplectic integrators, IMEX Methods)
* Stochastic ordinary differential equations (SODEs or SDEs)
* Random differential equations (RODEs or RDEs)
* Differential algebraic equations (DAEs) - system of differential equations
* Delay differential equations (DDEs) - differential equation with feedback
* Mixed discrete and continuous equations (Hybrid Equations, Jump * Diffusions)
* (Stochastic) partial differential equations ((S)PDEs) (with both finite difference and finite element methods)

To make all of this scale
* GPU acceleration with CUDA
* Sparsity detection
* Progress metre integration similarly to the ```tqdm```
* Multithreading 
* Forward and adjoint local sensitivity analsis
* Arbitrary precision + wrappers for Fortran


Scientific computing in Julia is great because the libraries are
* short
* fast
* easy to use

What can you do with a scientific library in genreal
* Maximum Likelihood estimation - basic supervised learning in machine learning
* Forward and adjoint sensitivity - fast automatic differentiation
* Global sensitivity analysis: how sensitive is the output to various inputs
* Surrogates of models: if output from some model is hard to measure can you pick a simpler model - Monte Carlo Techniques
* Uncertainty quantification: Probabilisitc programming and ML

Can even add support for
* chemistry like libraries https://github.com/SciML/DiffEqBiological.jl
* Quantum optics
* Rigid body simulation
* Nbody simulators
* Chaotic system
* Pharmaceutical implementations like Pumas that they've licensed, looks like this is a good business https://pumas.ai/

Core ideas of sciML project
* More ideas from science are making it to ML and we want to be able to use them quickly and efficiently
* Performance issues are bugs
* Everything should be automatically differentiable
* Work with top hardware as much as possible
* Modular, have small libraries

Benchmark wrappers for python code are in this library https://github.com/SciML/SciPyDiffEq.jl - makes it easy to benchmark everything from Julia

Testcases and benchmarking code for DiffEq: https://github.com/SciML/DiffEqDevTools.jl

ModelingToolkit vs DiffEq: 


## Differential Equation Flux.jl 
https://github.com/SciML/DiffEqFlux.jl

## Data driven differential equation
https://github.com/SciML/DataDrivenDiffEq.jl

Learn the dynamics of a system from data! Mind blown
Autoscientist work

## https://github.com/SciML/DiffEqFlux.jl
Differential equations in Flux
1. Define your ODE system
2. Define a neural network and a loss function

When you're working with an ODE system you need to guess what the parameters should be for example in teh case of Lotka Volterra you need to figure out what alpha and beta are OR you can learn them from the data directly.

Out of the box in Julia we can add noise to our observations. Any observation in science is noisy so adding the right prior is super useful

COre value proposition of ML + science work: observations, noise model, ML model, ODE model -> ODE hyperparameters

## Neural ODE
Compute the derivative of an ODE, you can do so with a neural network.

Advantages
* Continuous number of neural network layers
* Tradeoff between memory and time - dynamically set it depending on whether for you compute or storage is more compute
* https://twitter.com/search?q=slide%20from%3Aformalsystem&src=typed_query

## Notes from stream
* Check out K programming language and see ideas that I could use from APL derivatives
* Check out data driven differential equations in more depth, sounds amazing

## References

https://benchmarks.sciml.ai/
https://tutorials.sciml.ai/
https://github.com/SciML/OrdinaryDiffEq.jl/issues/1064
https://sciml.ai/2020/03/29/SciML.html
https://github.com/SciML/DataDrivenDiffEq.jl
https://github.com/SciML/ModelingToolkit.jl
https://github.com/SciML/DiffEqFlux.jl
https://arxiv.org/abs/2001.04385
https://github.com/SciML/DiffEqFlux.jl/issues/48