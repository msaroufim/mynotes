# Poplar setup

## Variables

1. Link C++ libraries
2. Setup Device and target
3. Create graph object and add variables to graph
4. Allocate each variable to a tile
5. Setup engine for control flow, in this example we only use streams
6. Graph by default will run on IPU and can create handles to read and write from host

## Operations
* Poplar supports an add operation on tensors

## Vertices
* Compute Set looks really fancy and I don't get how it works yet
* What's t he difference between a compute est and control program

## Profiling
* Engine has a profile summary which you can call after loading a graph

## Regression Example
* Setup IPU with num IPUs and number of tiles
* As a usage exampl ewould be good to varry numIPU and numtilesPerIPU to see how the algorithm scales
* mapTensorLinearly? What does this do exactly?
* Is SGD training happening on the host?

## Matrix multiply
* Multipy a vector by a matrix codelet
* Allocate 1 vertex for each row
* Input vecotr needs to be broadcast over every tile

## Efficient Matrix multiply
* Split each row into several segments and have the vertices calculate the dot product of each segment
* Then reduce results to return an output
## Miscellaneous notes
* dcpkg to manage installations of packages