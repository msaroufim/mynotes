# Stacking

This is a proposal to implement a ```stack``` operation in ```nalgebra``` which is extremely useful in projective geometry and deep learning libraries. This proposal aims to bring a compile time typecheched version of [numpy stack](https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html) to ```nalgebra```.

```rust
//Need to type annotate this more properly
fn stack(array1, array2, axis: u32) -> array3 {

}
```


## Open questions for discussion
* Should we have variable int declarations for the axis argument?


## Some personal notes
* Vstack takes a tuple of ndarrays that all need the same shape except on the first axis. Vstack is deprecated in favor of np.concatenate and np.stack. Implementation just checks if arrays are at least 2 dimensional and then stacks them row wise by calling concatenate with 
* Vstack is implemented using concat with axis 0 and hstack is implemented using concat with axis 1
* Concatenate is implementd in ```multiarray.py```. Weirdly enough even though axis is an argument it seems like the function always assumes no axis which means flattening a bunch of arrays. Turns arrays into a list of arrays, appends them to each other and then returns - lolwut??
* Ok so turns out the real implementation is in C https://github.com/numpy/numpy/blob/master/numpy/core/src/multiarray/multiarraymodule.c - I wonder if the Python code is translated or just runs as is
* Looks like based on my current understanding of the C code that memory is copied and not referenced
* Good ndarray docs https://docs.scipy.org/doc/numpy/reference/arrays.html

## How does ndarray work
* 1D contiguous array of memory that you index into via strides (similar to layout of heaps in memory)
* Fixed size objects in each cell so ndarrays aren't heterogenous
* Axis is really important to understand for numpy - here is a link that helped me not forget everything all the time https://colab.research.google.com/drive/1pJ8n9QWizFDSMu8ta5OzGc3z47UrtPBG
* ctypes allows a foreign function interface for C in Python
* 


