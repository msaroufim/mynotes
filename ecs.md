

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


## Important notes

* A slow game isn't a game still need to render in 60fps so can't go over the entire memory hierarchy. Think about locality whenver something in your codebase is accessed a lot and is slow
* There isn't concensus around what ECS actually is https://gamedev.stackexchange.com/questions/4898/are-there-existing-foss-component-based-frameworks/4966#4966
* So in this tutorial we're going to look at what Unity defines as ECS and ignore the but aaaactually folks
* Show CPU core meme https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FProgrammerHumor%2Fcomments%2Fbzv8q4%2Fparallelism_be_like%2F&psig=AOvVaw1bmaE8-VzLwcxQVv19Wfoj&ust=1599538672184000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIj9vISY1usCFQAAAAAdAAAAABAD


## Unity ECS summary
https://learn.unity.com/tutorial/entity-component-system# 

## Video 1
* Old Unity in Entity component - GameObject and Components
* Performant code, easier to read, easier to reuse, burst compiler for high performance C#
* Unity is based on Game Objects and Mono Behaviour and each component does Renderer Physics and Movement
* New Unity entities group together components, components contain data, systems contain behaviour - only systems have logic
* On entity player have 3 components renderer, physics and movement
* Build a render, physics and input system seperately
* Need to explicity install ECS in Unity
* We seperate our behavior and data into 2 seperate classes
* THere is pure ECS and hybrid ECS - hybrid is a bit confusing
* Entity debugger can show you which components are running

# Video 2
* GameObjects and Components are actually really nice from a programming standpoint once you get used to them but they fall apart when we're dealing with millions of entities in a game. Think complex simulators or massive multiplayer game
* Data is scattered - game object contains references to other memory location so we're thrashing RAM all the time (good time to show the picture)
* We don't want to move the entire transform, we just ned position and rotation
* All single threaded
* How can we use multicore processing (put picture of threadripper)
* We can have a bullet manager and pass updates for all bullets into somejob
* Most cores are actually unused - show my screenshot of task monitor to show how little my CPU is used
* Multithreading is hard: thread safe, race conditions, context switching is expensive
* C# job system worries about the complicated multithreading stuff - working on a distributed system now you have 2 problems

## Video 3
* Entities only have data
* Components have filters 
* System do a complicated job
* Performant code by default which leverages multicore processors and uses the burst compiler

## Video 4
* Actually shows some code
* Shows a demo of traditional game object and component systen can get up to 18K ships on screen at one
* Setup a movementjob which inhertis from IJobParralell ForTransform and thten just keeps the data you need for the job and then have an eexecute function which performs the behavior

TODO: Still need to watch 3 videos more closely, feels like a lot of extra boilerplate but it could just be habit