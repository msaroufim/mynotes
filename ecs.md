

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

* Setup data needed completely seperately and put it in a struct that inherits from IComponent Data


Then create a movement system


```C#
public struct MoveSpeed : IComponentData
{
    public float Value;
} 
```

```C#
public MovementSystem : JobComponentSystem

struct MovementJob: IJobProcessComponentData<Position, Rotation, MoveSpeed>
{
    public float topBound;
    public float bottomBound;
    public float deltaTime;

}

public void Execute(ref Position, [ReadOnly] ref Rotation rotation) 
{
    ...
    ...
    position.Value = value;
}

protected override JobHandle OnUpdate(JobHandle inputDeps) 
{
    MovementJob moveJob = new ...

    JobHandle moveHandle = moveJob.Schedule(this, 64, inputDeps,);
    
    return moveHandle;
}

```

* Finally create a game manager
    * Use Native Array to instantiate more entities
    * For each entity call SetComponentData to set things
    * Dispose entities array if you don't need the references anymore


## Video 5
* Got 96K ships at the same time after these change
* If ECS is implemented Burst compiler just works - Go to jobs use Burst jobs and then they can get 156K
* His GPU started bottlenecking his CPU

Thoughts: This tutorial kind of sucks lol - I need to look at code examples

## Unity at GDC - ECS for small thing
https://www.youtube.com/watch?v=EWVU6cFdmr0

Resource Entity
* Sprite
* Audio CLip

Bullet prototype
* Transfor
* Sprit2d renderer
* Audiosource
* Velocity
* Damage
* Bullet
* Collider

Bullet system
* Shooting
* Collison
* Damage
* Cleanup
* Audio
* Rendering

Approach was still in beta as of 2018

# Unity GDC 2019 - Data oriented design
https://www.youtube.com/watch?v=0_Byw9UMn9g

This is the clearest talk Unity has so far - use this as a reference from now on

Object oriented design
* Classes with data and behavior
* Inheritance to reuse code

CPU perfomrance got a lot better - RAM is not faster

Cache and memory
* Spatial locality
* Temporal locality

Classes with references in OO can't align stuff in cache well and you load too much stuff in cache - you may not need all the data there

Instead of having an array of structures you cavn have a structure of arrays which gives you much better data locality and as a result better cache performance

> ECS is like an in memory data base for games so you can run queries on game objects so looking up stuff is a lot faster than doing a linear search with game tag for example

Input Data -> Processing System -> Output Data

They use the same cooking analogy used in the category theory book

Data oriented design it's not hard, we're just not used to it


# Code examples
https://github.com/Unity-Technologies/EntityComponentSystemSamples

Even within the basic hello cube examplee the use cases are not entirely trivial

## Hello cube
For each functionality unity creates .meta files with the necessary data
1. Rotation 
    * Keeps track of speed component
    * For each entity in system base iterate over entities, change their rotation adn then scheduleparallel()
2. Can use chunks to move objects that are close to each other in memory
3. Subscene
    * Load parts of a large scene
4. Has a custom way to spawn objects
5. 

Still feels fiddly, isn't as seamless as other workflows I've seen