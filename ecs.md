

# References
* Unity tutorial (Video): https://learn.unity.com/tutorial/entity-component-system#
* Julia ECS: https://github.com/louisponet/Overseer.jl
* C++ very popular library: https://github.com/skypjack/entt
* ECS tutorial based on ENTT library with loads of benchmarks: https://pvigier.github.io/2019/07/07/entity-component-system-part1.html
* ECS in Unity tutorial: https://app.getpocket.com/read/3102416168
* ECS complete tiny library with video on rendering a lot of different falling cubes: https://austinmorlan.com/posts/entity_component_system/
* Tiny short introductory tutorial with handrawn images: https://medium.com/ingeniouslysimple/entities-components-and-systems-89c31464240d
    * Check out Game Programming patterns data locality book
    * ECS helps you improve data locality better which also makes garbage collection easier
    * There was a point about CPUs improving a lot relative to RAM that I didn't entirely get

* Nice more complete list of references https://github.com/dbartolini/data-oriented-design

* A slow game isn't a game still need to render in 60fps so can't go over the entire memory hierarchy. Think about locality whenver something in your codebase is accessed a lot and is slow
* There isn't concensus around what ECS actually is https://gamedev.stackexchange.com/questions/4898/are-there-existing-foss-component-based-frameworks/4966#4966
* So in this tutorial we're going to look at what Unity defines as ECS and ignore the but aaaactually folks
