# References
* Rock paper scissors in Julia (basic game engine): https://giordano.github.io/blog/2017-11-03-rock-paper-scissors/
* Dual numbers in real AD: https://github.com/JuliaDiff/ForwardDiff.jl/blob/master/src/dual.jl
* Matrix multiplication: https://www.oxinabox.net/2020/02/09/whycompositionaljulia.html
* Uncertainty quantification: https://tutorials.sciml.ai/html/type_handling/02-uncertainties.html
* GPU code - run the same GPU code on multiple accelerators
    * https://github.com/FluxML/Flux.jl/blob/96943eaed54c451170c44c0bbb0e65643cf29561/src/cuda/cudnn.jl
    * https://github.com/FluxML/Flux.jl/blob/96943eaed54c451170c44c0bbb0e65643cf29561/src/cuda/curnn.jl
* Forward mode AD and reverse mode in 50 and 90 lines respectively: https://www.juliadiff.org/ChainRulesCore.jl/stable/autodiff/operator_overloading.html
* AD in a tweet: https://twitter.com/marksaroufim/status/1302301588925472768
* Basics of AD by Wikunia: https://opensourc.es/blog/basics-multiple-dispatch/

# Notes
By Lyndon White
The 3 key real "you cannot do this without multiple dispatch" that I ha e found are:
 - structured matrix multiply
 - flexible output formatting (dispatch on Mimetype, and object to be represented)
 - Arithmetic Type Promotion.

By Chris Rackauckas
Normally you need to rewrite a solver to do uncertainty propagation
Normally such a solver needs the user to rewrite their inputs to handle it
What comes out needs to be handled by the user to build an array to throw into matplotlib
Not only is the ODE solver part handled, but the measurement type is converted automatically to plot the point + the error bars.

