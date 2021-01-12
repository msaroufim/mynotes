https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html

# Pytorch Geometric ops

Pytorch geometric has 4 special CUDA libraries it imports

1. torch-scatter
2. torch-sparse
3. torch-cluster
4. torch-spline-conv

## torch-scatter
https://pytorch-scatter.readthedocs.io/en/latest/
https://github.com/rusty1s/pytorch_scatter

Scatter and segment operations - reduce operations based on a group index. Reduce can be sum, mean, min or max by default sum

Scatter: For each element in a tensor, give it a group index then reduce along that index

Segment COO: is the same but assumes indexes are sorted so it's faster than general scatter operation

Segment CSR: Same as above but order in which groups are addressed is deterministic, it's also the fastest

## torch-sparse
https://github.com/rusty1s/pytorch_sparse

60% python code, 25% c++, 10% cuda

Libraries for 
* Sparse Dense matrix multiply (Adjancency matrix times feature matrix)
* Sparse to Sparse matrix multiply (Adjacency times Adjacency matrix)
* Transpose
* Coalesce - row wise sort and remove duplicate

## torch-cluster
https://github.com/rusty1s/pytorch_cluster

About ~60% of codebase is C++, 15% CUDA - just 20% is python code

Comes with several graph clustering algorithms
* k-nn
* random walk sampling
* pointnet++
* voxel grid, weighted graph cuts

## torch-spline-conv
Spline based convolution operator of spline CNN
https://github.com/rusty1s/pytorch_spline_conv
https://arxiv.org/abs/1711.08920
Not necessary to support torch-spline-conv?

Computation independent of kernel size as an alternative to filtering in the spectral domain (like what Graph Convolutional Networks do)