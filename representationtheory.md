# Representation Theory

## Algebraic Topology and Neural networks
* https://arxiv.org/pdf/1802.04443.pdf
* Can use algebraic topology as a measure of data complexity
* Intuitively the more holes and clusters are in a dataset, the harder it is to learn
* With more layers in a network it becomes easier to learn on datasets with more holes so this work aims to to characterize different neural net architectures using persistent homology
* Final contribution is an algorithm called topological archtecture selection which uses this insight on Open ML benchmark datasets
* A, B are homeomorphic and f is their homomorphism if there exists f: A -> b and f^-1 : B -> A
* The power of topology is that it can differentiate between two spaces while ignoring certain irrelevant features like rotation, translation and curvature
* Algebraic topology is about showing how two spaces are equivalent or not by first mapping them to algebraic constructs like groups and chains
* Many flavors of algebraic topology but a computationally realizable one is homology
* A homology H is equal to the set of all homology groups H_n(X) = \Z ^\beta_n where \beta_0 is the number of seperated components 
* If X ~= Y then H(X) = H(Y)
* Trivial homology is treating each point in a dataset as its own component. Persistent homology allows us to have a non trivial homology
* Persistent homology feels like a sort of clustering (rest of this could be wrong)
    * Start with n balls centered at each point in dataset of radius 0
    * Grow each ball by epsilon
    * Merge connected components
    * Grow each ball and reconnect until you have just 1 component
* Homological expressivity is the ratio of Betti numbers of the neural net divided by the Betti number of the dataset
* Models are parametrized by the number of layers they have
* homology doesn't do well for high dimensional data so they embed high dimensional datasets using Locally linear embeddings
* Need to read up more on persistent homology
* Homology helps us figure the kinds of spaces that a neural net can cover and we can then compare that with the space of the dataset to figure out if the model can actually learn the data

## State representation learning
* https://arxiv.org/pdf/1802.04181.pdf
* Applications: find lower dimensional representations of the world and learn on them more efficiently
* Several metrics exist to measure the quality of a representaiton all summarized in a table. ALl methods mostly fall into 2 buckets: task performance and measures of the geometrical coherence of the embeddings
* Work in manifold learning and Pyotr Indyk work is gonna be relevant again - Distortion is measure local and global geometry coherence of representation changes w.r.t to ground truth (used for embeddings).
* Talks about the various encoders that can be used to learn a state repreesntation
    * Denoising autoencoders: Add noise to input
    * Variational encoders: Approximate P(s_t|a_t) with approximate posterior model q_theta(st_t|o_t) q_theta is trained by regularizing to normal distsribution and minimizing the error between o_t and o_t hat
    * Siamese networks: Differentiate between input data using 2 identical networks with the same wieghts. Can be used to implement priors and compute similarity score between s_t and s_t+1 (temporality principle, slowness principle)
* Can learn a forward model as an objective for the autoencoder sˆt+1 = f(s_t, a_tt; θ)  , inverse model a_t = g(s_t,st_t+1 | ), do pca, adversarial training
* Can also use reward functions from RL as additional signal but not necessary. There are also other loss functions that can be added
    * Slowness: Small changes in state locally
    * Variability: Representation should spend more space describing moving objects
    * Proportionality: state changes by roughly same magnitude for any action
    * Repeatability: making same change to same state should result in teh same state


## OSS projects
* https://github.com/dlfivefifty/RepresentationTheory.jl
* https://github.com/gbarsih/Representations-in-Robotics
* TODO: more stuff on geometric deep learning

## Other papers
* http://www.robotics.tu-berlin.de/fileadmin/fg170/Publikationen_pdf/Jonschkowski-15-AURO.pdf
* https://pdfs.semanticscholar.org/24f0/35f6493d8a1c6d3386ed9b3b62fd16072803.pdf
* https://arxiv.org/pdf/1709.06560.pdf
