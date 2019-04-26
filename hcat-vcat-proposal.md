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
* Good ndarray docs https://docs.scipy.org/doc/numpy/reference/arrays.html


