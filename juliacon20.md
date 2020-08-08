# Exciting talks at Julia Con 2020

## Group theory for molecular vibrations
https://www.youtube.com/watch?v=Bkkqdr2vmZ4&list=WL&index=2&t=6s

Molecular vibration is harmonic and depends on the molecule geometry

Take the kinetic and potential energy of a molecule by taking a weighted average of its velocity along each atom in the x,y and z axis
Once you have the Kinetic and Potential Energy you can use the Lagrange equations to find the actual vibration.

This approach works but doesn't use symmetry considerations. So the authors implemented a simple group theory library in Julia. Because Julia supports symbolic math you can treat the math in a symbolic way and reduce the complexity of expressions via known symmetry.

Note: Could not find a Github repo

## Terminal user interfaces
https://www.youtube.com/watch?v=-TASx67pphw&list=WL&index=5&t=23s

CRLF (Carriage Return Line Feed) is borrowed from typewriter terminology

The way the canvas works is that words can each have their own word and then there's some custom code to move the cursor to the right location

A terminal emulator behaves like a state machine, interfaces with TTY driver in OS

## Pluto jl
https://www.youtube.com/watch?v=IAF8DjrQSSk

Pain points for notebooks
* Global scope is persistent
* Can't version control (well)
* Can't send someone your environment as well (Google collab as well)

There are nice reactive environments like Observable but they don't work with Pytohon or Julia
Pluto has built in live docs and all cells are dependent on each other so no global scope, there's a dependency graph between the cells
@bind period html"<input type-range min=11 max=14 step=1e-2>
Additional work will tell you how long dependencies will take to run

https://github.com/fonsp/Pluto.jl


## Climate models in 16 bits
https://www.youtube.com/watch?v=GiSsoA1udUk&list=WL&index=6&t=2s

Similar to ML in that climate models don't need high precision to have high accuracy
Posit numbers have higher precision for smaller values close to 0 (best for uniform values)
Float numbers is best for uniform values
Julia's type flexibility makes it easier to design algorithms with different precision for different submodules of the codebase

## Watson.jl 
https://www.youtube.com/watch?v=jKATlEAu8eE&list=WL&index=4&t=17s

Can type initialize project and then automatically create notebooks, data, manifest.toml, readme etc..
with a macro to @quickactivate
@savename("prefix, params) where params is a jason to name a file with the parameters in the name
Lots of obvious stuff that scientsits already do a lot, I've expereinced all of these painpoints


## Alegraic Julia: Applied Category Theory
https://www.youtube.com/watch?v=7zr2qnud4XM&list=WL&index=7&t=959s

Code goes from your scientific understanding -> math -> code -> domain code and quirks

Many tools have graphical representaiton like signal flow graphs, quantum diagrams, compartemental models in epidiomiology and electric circuits etc.. 

Create that graph and then build a simulator to simuulate the results

Build a model in a high level language and get 3 outputs
* A mathemtical formula
* A wiring diagram
* Some domain specific code

And then do the numerical computing in Julia

You can define a Category as an Object and Homomorphism and then define a compisiton rule - math the went over my head

SIR model -> Petri net -> Vector field -> Solve trajectories which you solve with DiffEq.jl