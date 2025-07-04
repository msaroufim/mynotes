Compute/Communication Overlap in Distributed Training
The Core Problem
In distributed training, you want to overlap gradient computation with communication (AllReduce), but this is hard to express and optimize.
Why Compilers Are Better Than Manual Approaches
Manual Runtime Approaches:

Require complex CUDA stream management and async operation handling
Need per-model tuning (bucket sizes, timing)
Achieve only ~60-80% of theoretical overlap potential
Hard to maintain and debug

Compiler Approaches:

Perform global dependency analysis across entire computation graph
Automatically find optimal communication insertion points
Achieve ~85-95% of theoretical overlap potential
Work across different model architectures automatically

Key Technical Insight: Gradient Dependencies
python# Gradients flow backwards with specific dependencies:
# Forward:  Input → Layer1 → Layer2 → Layer3 → Output
# Backward: Input ← Layer1 ← Layer2 ← Layer3 ← Output

# KEY: Parameter gradients can be communicated immediately after computation
grad_layer3 = layer3.backward(grad_output)  # Can start AllReduce now
grad_layer2 = layer2.backward(grad_layer3)  # Can start AllReduce now
# Communication for layer3 overlaps with layer2 computation
Compiler Pass Example

Dependency Analysis: Build graph of which operations depend on which data
Earliest Insertion Point: Find when communication can start (right after gradient ready)
Async vs Sync Decision: Use async when there's parallel work, sync otherwise
Stream Assignment: Assign compute vs communication to different CUDA streams
Code Generation: Emit optimized code with proper overlap

The SPMD Problem
SPMD (Single Program Multiple Data) assumes synchronous execution:
python# SPMD thinking - everyone does same thing at same time
backward_pass()      # Everyone computes
all_reduce()         # Everyone communicates (barrier)
But efficient execution is asynchronous:
python# Optimal execution
grad = backward_layer3()
handle = all_reduce(grad, async_op=True)  # Start comm
backward_layer2()  # Compute while communication happens
handle.wait()      # Only wait when needed
Why this matters: SPMD makes it conceptually hard to express overlap patterns, requiring compilers to automatically transform synchronous-looking code into efficient asynchronous execution.
Bottom Line
Compiler-based overlap optimization bridges the gap between easy-to-write SPMD code and efficient asynchronous execution, automatically finding overlap opportunities that manual approaches miss.
