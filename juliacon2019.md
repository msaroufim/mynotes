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
* 

## Gaussian Process Probabilistic Programming with Stheno.jl
* https://www.youtube.com/watch?v=OO3BBkGEMV8 - I keep falling asleep
* Talk was way too dense, need to check repo directly and some textbooks instead