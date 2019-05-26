# Fourier Policy gradients
https://arxiv.org/pdf/1802.06891.pdf

* Recast integral analyses with policy gradients as convolutions and turn them into multiplication
* Critic uses trigonometric functions and radial basis functions
* Up until this work policy gradient methods were either high variance or deterministic
* Summary of policy gradient methods with special mention to expected policy gradient
* Goes over basic properties of FT such as F(fg) = F(f) * F(g)
* Fourier transform from state, action space to frequency space (not sure what this means exactly)
* Benchmarks are of questionable quality
* Most of the paper goes over how to derive the expectations inside the policy gradient integrals. I'm disapointed that the paper does not go over ideas like state compression or how to do RL in a more sample efficient manner
