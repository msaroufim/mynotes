# Notes from neurallink presentation
* I wonder what's the book on human machine interfaces
* Does read and write of neurons, up to 10K tiny electrodes so can measure 10K neurons simultaneously
* 2mm incision and chip is wireless and can be updated wirelessly 
* Main purpose of presentation is recruiting ranging from meidcine and bio to robotics to software engineering (recommend to Maya too)
* Does a brief intro to information theory
* Focused on statistics of spikes so need a specific kind of sensor - other imaging techniques carry different kinds of data
* Talks about basic dynamical systems in neurons
* Even with a small number of electrodes we can do stuff like control a cursor
* 2 main techniques utah array and deep brain simulation
* Had to also build a surgical robot that can lay out where threadsd should be placed
* There is an outside pod that can you can configure and update your phone vs the immobile chip on the inside
* V1 is control phone, mouse and keyboard - doing clinical studies in 2020
* want to change the modern neurology surgery process into something non invasive
* Probes are roughly as large as an electric beam and there had to be lots of fancy material science going on
* design and implement a new chip every 3 months but at a high level turn analog to digital, do error correction and manage power - all in a 4x5mm silicon die
    * Analog pixel: amplifier + filter + analog to digital converter
    * on chip spike dectection with 200Mbit per second for each 1024 channels that is being recorded
    * stimulation engine 
    * Diagnostics for electrode
* From different signals can create a spike raster to visualize spikes
* can interface to motor cortex could help interface with different robots or synthesize speech
* Can write to brain by for eg simulating different areas in the visual cortex wihch each generate a pixel in your visual field 
* Reading and writing could be used to treat neurological diseases
* Different physical processes have their own readings in the brain which we can identify and then read or write to once identified