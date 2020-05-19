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

## ALBERT
https://arxiv.org/abs/1909.11942

#### Main contribution
Increasing model sizes in language results in better perf but runs into memory limitations with GPU/TPU
Model inter sentence coherence in loss
Model code and weights are on github

Even in the distributed setting, communication cost is O(#parameters)

2 techniques to reduce size of models
1. Seperate embedding matrix into 2, that way we can grow the hidden layer without increasing size of vocabulary embedding
2. Cross layer parameter sharing, that way number of parameters is not O(# layers)

In Albert all the hidden layers are the exact same. Seems to invalidate the fact that we need complex architecutres

Instead of predicting next sentence like in BERT, ALBERT uses sentence ordering as a self supervised loss function

Benchmarks show that ALBERT is better but training methodology needs to take into account accurately how much time BERT and ALBERT are each respectively taking.

## Longformer
https://arxiv.org/abs/2004.05150

O(L) where L is sequence length, other work is doing O(L log L)

Sliding attention window
Dilate the attention window
Custom CUDA kernel for the dilated attention operation - can probably just use ```numba jit```
Task specific global attention, BERT representation is not dependent on representation

This paper is the least interesting of the bunch


## Reformer
https://arxiv.org/abs/2001.04451

BERT like models are huge even though text corpus and total weights per layer aren't crazy -> 13GB for corpus and 2GB per layer

3 ideas
1. Use Locality SEnsistive Hashing for attention which reduces cost from O(L^2) to O(L log L)
2. Reversible layers
3. Splitting activation inside feed forward layers 


## DistillBERT
Reduce BERT size by 40% while retaining 97% of perf

Introduce a triple loss including langauage modeling, distillation and cosine distance loss

> Knowledge distillation is a technique where a smaller model is trained to copy the ouput of a larger model. More specifically, goal is to minize the cross entropy between the 2 models.

Control smoothness of output distribution by controlling temperature with softmax-temperature

Add cosine embedding loss to align direction of hidden state vector of teacher and student

Smaller network specifically means fewer layers

Initialize student by taking every other layer from the teacher network

## Movement Pruning: Adaptive Sparsity by Fine Tuning
Magnitude pruning used a lot in supervised learning but doesn't work for transfer learning. Main idea is very simple sort nodes by weight and remove the smallest weight one by one. It's surpringly difficult to beat this simple heuristic

Paper proposes movement pruning which looks at how weights change from task to task and remove the weights that change the most

It's crazy how simple and effective the heuristics that hugging face uses are. Most of their work goes towards solid benchmarking and ablation studiesm, true empiricists


## Hugging Face transformers library walkthrough notes
* Pretrained bert-base-uncased is 440MB
* Tokenizer is great and easy to use. They even have a rust implementation for really fast tokenization for online use cases
* if you enable logging hugging face will show you the full model architecture  
* Can pad encoding of words 
* Can visually inspect attention matrices
* Special tokens can be used to separate sentences
* Position ID assigned
* Most of the models I read about are already implemented here  https://huggingface.co/transformers/pretrained_models.html#
* Different NLP tasks can be setup with ```pipeline('task_name')``` including text generation, named entity recognition, masked language modeling, summarization, translation
* Can upload models with the CLI
* Usage examples of running on TPU
* Some helper CLI functions to run on different tasks
*  


## TODO
* just read the hugging face code for how this stuff works
* Look up precise definition for multihead attention https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html#multi-head-self-attention - Key, Query and Value are just abstractions to represent attention
* Reversible transformer: recover activation form a layer  by the activation from following layers (downloaded Gomez 2017 paper on reversible resnet)
