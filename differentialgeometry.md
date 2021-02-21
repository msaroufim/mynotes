# Keenan crane class
https://www.youtube.com/watch?v=KZjoxwUxlIs&t=990s

I really want to spend more time reading his material

Differential geometry is about discovering global properties about a manifold using local properties
A nice manifold for simplicial manifold (as in made with triangles) means that every edge is shared by at most 2 vertices or 1 if it's a boundary and that every vertex is surrounded by a (k-1) dimensional circle where k is the dimension of the manifold

These properties are nice and are reminscient of how we use 2d grids to represent images. Predicatle structure where every pixel has 4 neighbors

Topological data structures to represent meshes like
* adjacency list -> small storage cost but hard to iterate over edges
* incidence matrix -> one matrix for edges and another matrix for triangles https://www.youtube.com/watch?v=KZjoxwUxlIs&t=990s
* Sparse matrix -> associative array (row, col) -> val or array of linked lists or compressed column format

https://en.wikipedia.org/wiki/Doubly_connected_edge_list
Half edge is the most popular data structure used almost exclusively
Split each edge into 2 oppositely oriented half edges, each half edge is also going to know about its twin and next half edge, its parent, the edge that it belongs to and the face that it belongs to

Vertexes, Edges and Faces only need to keep track of which half edge its part of

Dual complex (half edge mesh also encodes it)

Poincare Duality - turn a simplicial compelx into its poincare dual (cell complex)

Poincare duality in nature - species of tilapia want dominion over ocean floor and they scoop up pebbles and spit pebbles at neighboring fishes and eventually every fish is a primal vertex and they carve out dual polygon homes
