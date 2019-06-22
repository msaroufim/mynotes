# https://github.com/MikeInnes/diff-zoo


## Intro

* Julia has basic filesystem commands incorporated natively so don't need to open a shell like in Python

The ```:``` operator in Julia helps interpret the rest as an expression, same as the ``` ` ``` notation in Lisp

```julia
y = :(x^2 + 1)
```

Expressions have a tree like structure with a head and arguments. We can even build them by hand. We can also call eval on expressions to get a number out.

Basic rules of differentiation look like a recursive algorithm so we can implement it.

Can use MacroTools ```@capture``` macro to figure out if an expression is a * b or a /b or a + b and apply the right differentiation rule

You end up with a large tree this way which has O(n^2) cost

Julia has a piping operator |>

```julia
:(1*2 + 1*2) |> printstructure;
```

Writing an expression as a tree is called a Wengert list

## Forward mode
1. Given the Wengert List (list of operations)
2. we also keep track of the list of derivatives of each operation. y is the primal code and we call dy the dual code. 
3. Now we need to decide which direction we go in.

Create a container that holds both y and dy/dx called a dual number

```julia
struct Dual{T<:Real} <: Real
  x::T
  ϵ::T
end

Dual(1, 2)
```

And then use the same rules as regular differentation but on both the dual and primal number. What's good about it though is that we don't need to store intermediate results so we save lots of space

Can look at the internal representation of code using ```@code_typed```


AD still has a relationship with automatic differentation where we replace x + epsilon by x + i * epsilon but the difference is that AD gives exact derivatives.

## Forward and reverse mode differentiation

Given basic derivatives like that of cos(x) and chain rule we can either do derivatives in a forward or reverse mode

Chain rule works in both directions

It should be clear, then, what mode is better if we have a gazillion inputs and one output. In forward mode we need to carry around a gazillion "perturbations" for each element of  𝑦𝑖 , whereas in reverse we only need a gradient of the same size of  𝑥 . And vice versa.

Reverse mode gives us intermediate gradients for free dy/dy = 1 while forward mode with multiple params requires going through computation graph O(number of inputs) which is no bueno

It's easy to see, then, why reverse-mode differentiation – or backpropagation – is so effective for machine learning. In general we have a large computation with millions of parameters, yet only a single scalar loss to optimise.

## Tracing based AD
Use macros to write an arbitrary function as a Wengert list or in ML talk a graph because even for loops and conditions can be turned into functions. 

For loops can be explicitly written out
Conditions can be modeled with discrete functions like f(a) ^ b where b = 0 if false and b = 1 if true