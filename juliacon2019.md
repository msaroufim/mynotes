# Differentiable rendering

## JuliaCon 2019 | Differentiable Rendering and its Applications in Deep Learning


https://www.youtube.com/watch?time_continue=2&v=cdwLJCb45Kk

* Rendering is converting a 3d dimensional field into a 2d projection in the camera space.
* Ray tracing is a particular rendering technique for photorealistic images that's very computationally expensive
* Most renderers are written in low level languages
* Raytracer.jl writetn in Julia uses Zygote.jl for differentiability
* Uses Duckietown.jl as an environment
* Define light and get primary rays, load scene objects from .obj file
* Compute gradient w.r.t light between ray trace and target
* Inverse rendering. Convert 2d image and turn it into a 3d scene - in general hard because there are an infinite number of solutions. So use an approach where we fix some parameters compute gradient w.r.t to optimal closed form expensive solution and update weights 
* Weight updating done using Flux or Optim with MSE loss


![rendering](rendering.png)

![rendering2](rendering2.png)

![rendering3](rendering3.png)

* Elongated episode idea from reinforcement learning

* Backpropagation done via entire pipeline which means you can learn robotics tasks from pixels as well if you do inverse rendering in the pipeline - paper?
* In some sense having a ray tracer in the pipeline means your neural network can look into what the world will look like and what it looked like before to be able to make a decision 
* Is there anything special done on Duckietown.jl that would make it also differentiable?
* This method can make the networks really shallow
* Next steps
    * **benchmark vs Redner and TF graphics**
    * Multi threading and GPU support. Support hardware acceleration and real time rendering techniques


## Gen: A General-Purpose Probabilistic Programming System with Programmable Inference Built on Julia

https://www.youtube.com/watch?v=B7mc1wXPZR8

* Probabilistic programming where you want to infer some latent variables that explain some observations
* Can invert simulators
* This project is close in inspiration to Flux
* Generative model: Start with random observations and then sample observations
* Inference model: go from real observations back to a model
* Refine guess using MCMC 
* Each inference algorithm overrides sample and observe in a different way
* Generative function  is compiled into its own type which can do stuff like simulate, generate, update, assess, propose, regenerate, choice gradients, accparamgrads


## How we wrote a textbook using Julia

* https://www.youtube.com/watch?v=ofWy5kaZU3g
* Good discussion on tooling, mostly they use what I use

## Computational topology and Boolean operations with Julia sparse 
* https://www.youtube.com/watch?v=N7YHAcv8DEk&t=9s
* The lab has an insane list of projects https://github.com/cvdlab/
* People wanna analyze all sorts of geometric data from point clouds, meshes, CT scans from applications ranging from simulation to graphics
* Can solve problems by turning them into datastructures and then doing transformations on them
* Wow wow - can use this to generate floorplans that people can draw in browser to train robots https://github.com/cvdlab/react-planner

## Geometric algebra in Julia with Grassmann.jl
* https://www.youtube.com/watch?v=eQjDN0JQ6-s
* Speaker was really hard to understand

## Gaussian Process Probabilistic Programming with Stheno.jl
* https://www.youtube.com/watch?v=OO3BBkGEMV8 - I keep falling asleep
* Talk was way too dense, need to check repo directly and some textbooks instead
* Need to remember that geometric algebra works for tensors of arbitrary dimension so it feels like this should speed up tensor math for neural networks

## Electrifying Transportation with Julia
* https://www.youtube.com/watch?v=4mZmlSNnsrI&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=100&t=0s
* Transportation responsible for 29% of greenhouse gas emissions
* Electrifying airplanes is possible but difficult by stuff like distributed electric propulsion
* Use Julia to integrate fast models of vehicle dynamics and battery dynamics
* Can calculate diffusion, temperature, SEI growth and concentration of lithium between cathode and anode which is really important to understand aging characteristics

## Let's play hanabi
* https://www.youtube.com/watch?v=BnGBX_DV3xY&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=96&t=0s
* 3 messages
    * Julia interop with other languages is easy
    * Productive to provide HTTP services
    * FAST and easy to use for Reinforcement Learning
* Possible to write engine in Julia and wrap the environment in Julia (Hanabi engine written in C++) - creating a wrapper only took the team 4 lines of code
* Use web socket in HTTP.jl in 200 LOC and then can interact with it via Julia REPL
* Used rainbow which contains a couple of ideas: Distributional RL
* Flux CPU better than TF but TF GPU is better than Flux GPU
* Julia code 1 LOC for each 10 of TF
* Perf tricks
    * Release resources with a finalizer
    * Avoid extra allocation
    * Fused broadcast will make your code fast and easy to read

## Modia3D: Modeling and Simulation of 3D-Systems in Julia
* https://www.youtube.com/watch?v=b3WfqXZRKpA&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=53&t=0s
* Can define 3d systems using Julia code, no seperate config language like YAML is needed
* Can do collision handling
* Modiator: model diagram editor - their entire toolsuite on Github looks invaluable to study

## Julia's Killer App(s): Implementing State Machines Simply using Multiple Dispatch
* https://www.youtube.com/watch?v=WGT9_cEImAk&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=14&t=0s
* Core tech of Julia is Multiple Dispatch and a Type system
* States and transitions can be types and multiple dispatch can simplify the implementation

## Symbolic Manipulation in Julia
* https://www.youtube.com/watch?v=bGYSae90hA0&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=36&t=0s
* Can model pharcamometric models and diff equations in a symbolic manner
* ModelingToolkit.jl
* Term rewriting is undecidable
* Can model a system is a bunch of rules and then apply those rules to get the simplest possible form of an expression
* Can do logic expressions in a project like https://github.com/HarrisonGrodin/Rewrite.jl

## A New Breed of Vehicle Simulation
* https://www.youtube.com/watch?v=K8rPZVotroY&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=38&t=0s
* Works for companies that build unmaned aircraft that can deliver blood which needs to be stored centrally to be preserved
* Have a YAML configuration for the plane
* Flight controllers need to be ran as C code. Can call C from Julia easily

## Debugging Code with JuliaInterpreter
* https://www.youtube.com/watch?v=SU0SmQnnGys&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=12&t=0s
* Programmer written code -> AST -> Lowered AST -> Typed and optimized AST -> LLVM IR -> Native code
* Debuggers exist from Debug.jl, JuliaInterpreter.jl, Galium.jl
* Julia lowered code is pretty easy to understand and the team built a debugger for this and it has a Juno integration

## Differentiate all the things
* https://www.youtube.com/watch?v=OcUXjk7DFvU&list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&index=13&t=0s
* Zygote is gonna change the Flux API a lot
* GPU support is now a macro as well ```cuda()```
* Pytorch code is written in LLVM and can take its gradient

## The Unreasonable Effectiveness of Multiple Dispatch
* https://www.youtube.com/watch?list=PLP8iPy9hna6StY9tIJIUN3F_co9A0zh0H&time_continue=2&v=kc9HwsxE1OY
* Code reuse in Julia is particularly good vs Object Oriented programming
* +- syntax exists so that values can have built in errors
* 2 kinds of code reuse:  generic algorithms (same algorithm on multiple types) and common types shared by very different packages stem from different aspects of multiple dispatch
* Function overloading and multiple dispatch are not the same
* Multiple dispatch means you get exponential expressive power in the number of arguments
* Write Julia code with no types 
* E.g: An inner product on vectors also works for one hot encodings
* Multiple dispatch means you barely need to touch the original code vs in C++ the function needs to be in the class or you do inheritance. Sticking methods inside a type means that a package becomes huge but it makes namespacing good
* The expression problem
    * Defining new types to which existing operations apply: easy in OO and hard in Functional
    * Defining new operations which apply to existing types: easy in functional but hard in OO

## SLAM in Julia ROME.jl