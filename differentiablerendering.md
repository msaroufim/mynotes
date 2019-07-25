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