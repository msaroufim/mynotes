Gradient Accumulation Count - How many batches do you use before you update network parameters
Steps per epoch = data_length // batch_size - better to skip this if your dataset is of finite size 
validation steps - same as steps per epoch but  over validation set
epochs - number of times you train over entire dataset
Batch size is between size 1 to your entire dataset or what can fit on your GPU
TF dataset prefetch - how many minibatches or examples your IO should load in - only useful if compute is your bottleneck

drop_remainder - use this when you want all your batches to be of the same size

Make sure to use NVIDIA profiler to figure out if IO or compute is bottleneck https://developer.nvidia.com/nvidia-visual-profiler




Batch size: # examples in batches. Size from 1-device memory

Epochs: # passes over data

Steps/epoch or validation steps: # examples // batch_size

Gradient accumulation: # batches for gradient update

Prefetch: # batches preloaded to accelerator - for IO bottlenecks

Instead of waiting a magic compiler, I'm going to make a tutorial about how to use the NVIDIA profiler to debug IO vs compute bottlenecks next week https://developer.nvidia.com/nvidia-visual-profiler