# Pytorch Geometric

https://pytorch-geometric.readthedocs.io/en/latest/

## Installation

Kind of a pain in the ass, requires lots of extra cuda libraries - specifically libraries that deal with sparsity. Graph connectivity is sparse and it requires special batching to fully utilize a GPU since the matrices are all relatively small.

## Usage

Define a graph in COO format which ```[i, j, data]```

Comes with 3 kinds of benchmark datasets
1. Planetary (Citeseer, Pubmed)
2. Graph classification QM7 QM9
3. 3D mesh pointcloud like FAUST, ModelNet, ShapeNet

## Mini batches

Mini batches are created by concatenaing edges into block diagonal format - still need to understand how this works exactly. Explained in more detail here https://pytorch-geometric.readthedocs.io/en/latest/notes/batching.html

Each graph (e.g: molecule) is an element of a diagonal matrix. The whole diagonal matrix is the batch and then we combine this data with the node embeddings and graph target value to formulate the full ML problem.

Can also mix graphs into same point if we're doing graph comparison algorithms

## Data transforms

Similarly to how torchvision has data augmentation helper functions so does pytorch geometric and you can do stuff like translate data for each node

Can turn pointcloud data into a graph dataset by running KNN

## Training

Training is identical to regular pytorch code


```python
def __init__():

def forward():
```

## Message passing interface
A convolution is an aggregation where each node picks a message that it transmists its neighbors. Common messages are ```min, max, mean``` which let you change each node embedding.

## Creating datasets 
Project has a simple interface to create datasets

# References

* This is the original graph convolution paper https://arxiv.org/pdf/1609.02907.pdf - read and summarize this
* Edge convolution https://arxiv.org/pdf/1801.07829.pdf
* List of tutorials here https://pytorch-geometric.readthedocs.io/en/latest/notes/resources.html

