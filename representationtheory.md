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

## State representation learning
* https://arxiv.org/pdf/1802.04181.pdf

## OSS projects
* https://github.com/dlfivefifty/RepresentationTheory.jl
* https://github.com/gbarsih/Representations-in-Robotics
* TODO: more stuff on geometric deep learning

