# What is a graph neural network

## Intro

Great article on graph neural networks https://towardsdatascience.com/a-gentle-introduction-to-graph-neural-network-basics-deepwalk-and-graphsage-db5d540d50b3

## Types of ML problems on graphs

Given (node embedding, node data) do a classification for a node in a graph. Node embedding is computed as a function of (features, edge features, neighbor features, neighbor embeddings

Graph prediction, given a molecule predict if it is toxic

Generative, design a drug

Edge prediction, predict if two concepts are related

# How to compute node embeddings

2 ways of computing embedding
1. Deep Walk: Do random walks on graphs and then do skipgram prediction like in NLP. For classification do softmax over O(Vertices) so can use Hierarchichal softmax to reduce to O(log V) - Good summary of Hierarchichal softmax here https://www.quora.com/What-is-hierarchical-softmax, main idea is to compute probabilities of pairs of words at a time. Deep Walk doesn’t work for dynamic graphs because everytime data is added the entire network will need be retrained
2. GraphSage: At each step update hidden representation of node by taking aggregate of representation with neighbors and append the representation of the node at the previous timestep. There are many ways to do the aggregation over neighbors  by taking mean or pool for .eg. Finally loss function needs to make sure that nodes that are closer to each other should share more in their embeddings.

There are major companies using graph embeddings for their content discovery like Pinterest

# Libraries for graph neural networks
Pytorch Geometric https://towardsdatascience.com/hands-on-graph-neural-networks-with-pytorch-pytorch-geometric-359487e221a8

This is a great tutorial that shows how to use the library and how to implement the messag epassing interface to create the meaning vector for each node in the graph.

Goes over how to
1. Create a graph dataset and describes the edge index format for encoding edges
2. How to implement a custom layer
3. How to use this library of a recommender system kaggle problem

 
# How graph hardware could help?
https://medium.com/dair-ai/an-illustrated-guide-to-graph-neural-networks-d5564a551783

Nodes have to pass each other their embeddings as messages, so if each one can be on its own process then it'd be super efficient

# Applications of graph networks
* Geometry: https://towardsdatascience.com/hands-on-graph-neural-networks-with-pytorch-pytorch-geometric-359487e221a8
* Hard sciences: Biology, Chemistry, Physics
* Social network
* etc..



## VectorNet: Encoding HD Maps and Agent Dynamics from vectorized Representation
https://arxiv.org/pdf/2005.04259.pdf

Collaboration between Waymo and Google

Past approaches to modeling maps use Convolutional Neural Networks on top of high resolution image data but can instead model roads as vectors 

Augment perception systems such as object detection and tracking with prior knowledge provided from HD maps

Roads can be modeled as polylines - i.e: sequence of lines

Contributions
1. How to use vectorized scene context instead of rendered scene
2. Use hierarchical graph network and node completion auxilary task
3. Evaluate on argoverse dataset 

Each road is featurized as a node in a graph and keeps track of its end and start point with x,y,z coordinates, features like speed limit and an integer to map twhich polyline it belongs to.

Observed trajectories AND map features are represented as a sequence of vectors which are then passed to a fully connected graph (why fully connected?) and trajectories are masked and recomputed in a self supervised way

# Open questions (for me)
* How is fixed point theorem relevant? https://en.wikipedia.org/wiki/Fixed-point_theorem
* Longer survey useful? http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1015.7227&rep=rep1&type=pdf
* How useful are spectral techniques: https://towardsdatascience.com/an-introduction-to-graph-neural-networks-e23dc7bdfba5
* Can combine graphs with attention https://arxiv.org/pdf/1710.10903.pdf
* Good public Kaggle problem that would seem to benefit from graph neural networks: https://www.kaggle.com/c/champs-scalar-coupling/overview/description