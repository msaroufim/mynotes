# Flux JL

Models are just function composition

```julia
foo = Chain(exp, sum, log)
foo([1,2,3]) == 3.408 == log(sum(exp([1,2,3])))
```

Internally models such as affine are represented as a type

```julia
@net type MyAffine
  W
  b
  x -> x * W + b
end```

More complex function

```julia
@net type TLP
  first
  second
  function (x)
    l1 = σ(first(x))
    l2 = softmax(second(l1))
  end
  ```

  Initializers are simple

  ```julia
  Affine(in::Integer, out::Integer; init = initn) =
  Affine(init(in, out), init(1, out))
  ```

Recurrent models

```julia
@net type Recurrent
  Wxy; Wyy; by
  y
  function (x)
    y = tanh( x * Wxy + y{-1} * Wyy + by )
  end
end
```

Can chain several neural networks using 
```julia
 unroll(model, 20)
 ```

 Can debug array mismatches regardless of backend

 ```julia
InferShape Error in dot5: [20:37:39] src/operator/./matrix_op-inl.h:271:
Check failed: (lshape[1]) == (rshape[0]) dot shape error: (15,21) X (20,1)
 in Flux.Affine at affine.jl:8
 in TLP at test.jl:6
 in mxnet(::TLP, ::Tuple{Int64,Int64}) at model.jl:40
 in mxnet(::TLP, ::Vararg{Any,N} where N) at backend.jl:20
 ```

Has both 1-hot encoding and its inverse 1-cold encoding
