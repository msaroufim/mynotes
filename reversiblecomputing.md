# Reversible computing

## Book by Kalyan S. Perumalla

* Adiabatic computing: computing where lost energy can be recovered
* Inverse programming: at the application level
* Only bit erasure consumes energy
* Reversible computing can drive down synchronization overhead - can basically take an arbitrary decision and if it's wrong apply $f^{-1}$ which means you can beat the typical lower bound associated with distributed applications based on critical path analysis
* Can either save a copy of all variables or have a copy of all inverse operations - tradeoff depends how much compute vs storage you have
* Can be used for complex instruction scheduling
* Can undo memoization - tradeoff compute vs storage idea again
* Has applications to source code control - is it possible to build a memory efficient git?
* Can be used for fault detection - do a computation twice and double check
* Quantum computers are reversible by design - every unitary operation is reversible
* Can do fast writes in database and reverse if paradox found
* There are revirsible languages like Janus, ISA like Pendulum, Gates like CNOT and CCNOT and circuits
* Reversal can defined at any time $t$ or just the original time $t_0$
* $E_{in} = E_{irr} + E_{unr} + E_{rec}$ 
* Landauer's principle minimum energy to erase a bit is $kT \ln 2$
* Can rewrite Turing Machines in a reversable manner with some modificiations, same for circuits
* Jump statements can be made reversible by introducing a comefrom command or keeping track of some extra external data
* 3 approaches: Compute, Copy, Uncompute Execution or Undo, Redo, Do paradigm, Begin, Rollback, Commit paradigm
* Checkpointing can be total, w.rt to previous state, or w.r.t to initial state
* If conditions can be reversed if we record in the forward pass which of the two branches was taken so that we can reverse the correct one in the backward pass