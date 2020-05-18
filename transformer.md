# Transformer

## Generating long sequences with sparse transformers
https://arxiv.org/pdf/1904.10509.pdf

Transformers are O(N^2) and this work uses sparse factorizatioon to make it O(N log N)
Recomputation of attention matrices to save memory
Fast attention kernetls for training

Can model sequences with thousands of timesteps using hundreds of layers, works ofor images and text

Future work can use self attention to model sequences of length million or more

Long sequences needs networks with lots of layers (autoregressive) which also means they are way harder to train. Dilated convolutions from the Wavenet paper are one way to address this problem with ```log``` as many layers

Self attention amps a matrix of input embeddings X to an output matrix.
* Full self attention means you attend to all previous positions
* Factorized self attention means you attend to a subset of the indices and the problem becomes about picking which ones - this is a similar idea to striding in convolutional networks
* Attention layers can be aggregated for e.g: one layer looks at previous x inputs and other looks at every other input
* There are also several ways to merge attention, merge them sometimes, merge them all the time etc..
* Fixed attention layers, some specific cells summarize all past information and send it to everyone - works best for NLP

Recomputation of attention is faster than storing results in memory
Implemented their own GPU kernels to get things working fast
Network activations done at half precision to save time

Sparse transformer