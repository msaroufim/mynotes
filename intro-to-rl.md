# How to learn? Introduction to Reinforcement Learning

Try to imagine what it was like when you were a young child, you aimlessly explore around an environment. At this point you aren't preprogrammed with any notion of what's safe or dangerous, what's useful vs a waste of time.

So there you are, happily exploring on all fours. At some point you get bored and you try walking on your two feet instead. The giants in the room with you seem to lose their collective minds, they start crying, patting each other on the back, they call their relatives and make sure to film the entire ordeal on their phones. 

They call you a good boy, and you don't know why but your entire body delights at being called a good boy.

> You wanna be a good boy

You take a nap and wake up a couple of hours later, you feel pretty hungry, so you start staring at the dust and cat hair on the floor. You grab a tiny handfull and stuff it in your mouth, it's not too bad, the textures are pretty unique relative to what you've had before, the flavor suggests that it's an acquired taste. No sooner as you start putting your finger on the taste, do you see giant hands yanking the tasty snack you were enjoying and then the never ending scolding starts. It doesn't feel all that good to be yelled at, you don't like being called a bad boy.

> You don't wanna be a bad boy

## Pavlovian learning

Turns out you can explain most human behavior by combining two things
1. Wanting to be a good boy
2. Not wanting to be a bad boy


So here we are, thinking we're somehow special even though we can read but not understand texts like "Critique of Pure Reason".

Once you see this pattern it's almost impossible to unsee and you can start mapping how all your actions are either in anticipation of a reward (good boy points) or in escape of a punishment (bad boy points)

It's important to note that 1 and 2 are with respect to some parent/teacher/master that is fully responsible for creating your rewards. There is a trick to make this work for an organism without any sort of teacher or judge which we'll cover later (Curiosity driven learning).

## Mathemizing Pavlovian Learning: Reinforcement Learning

We're gonna try to formalize the main intuition of Pavlovian Learning mathematically so we're gonna start by introducing some terminology to model the interactions between an agent and the environment it's operating in.

* $A$ is the set of all actions
* $S$ is the set of all states
* $R_t$ is the reward you get at time $t$ 

Your goal is to learn a policy $\pi$ where a policy is defined

In Picture courtesy of Sweta Bhatt

![RL-intro](https://www.kdnuggets.com/images/reinforcement-learning-fig1-700.jpg)

In English

A policy $\pi$ is a function that takes an action $a$ from the set of all actions $A$ and a state $s$ from the set of all states $S$

In Math

$$\pi : A \times S \rightarrow [0,1]$$

In Julia

```julia
function policy(action, state)
    return other_action
end
```

Your main constraint in learning this policy is to either maximize some reward function or minimize some punishment function.

Suppose you're going to make a total of $T$ decisions then the total reward $R$ you should be trying to maximize is a sum of all rewards at each timestep t $r_t$

$$R = \sum_{t=1}^{t=T} r_t$$

Return of reward formula

Finally, rewards are more valuable if you get them sooner rather than later. E.g: if you get a dollar today you can invest it and have two dollars at the end of the year. So we will codify this insight using a discounted reward formula. 


$$R = \sum_{t=1}^{t=T} \gamma^t r_t$$ 

Where the discount rate $\gamma \in [0,1]$. 

if we set $\gamma = 1$ then we get $R = \sum_{t=1}^{t=T} 1^t r_t = \sum_{t=1}^{t=T}r_t$ which is equivalent to not having a discounting factor, i.e not valuing present reward more than future reward.

If we set $\gamma = 0$ then we get 


## API of RL algorithms

Let's take a look at a popular ```Julia``` reinforcement learning package called [Reinforce.jl](https://github.com/JuliaML/Reinforce.jl) to really understand how everything fits together.

First off we need an environment to work with which we can define as

```
reset!(env) -> env
actions(env, s) -> A
step!(env, s, a) -> (r, s′)
finished(env, s′) -> Bool
```

The ```!``` in the code is a convention we use to say that the function changes its inputs or has side effects while functions that don't have ```!``` are called pure functions with no side effects.

That's great and all but without knowing what the different states even are, how are we supposed to learn a policy on them?

Over multiple iterations we can codify our observations as Episodes where an episode is defined as a tuple.

```julia
ep = (s,a,r,s',done)
```
where
* $s$ is the current state
* $a$ is the chosen action
* $r$ is the instantaneous reward at this iteration
* $s'$ is the new state you end up in
* ```done``` is a boolean that lets you know if the goal was achieved

With this mind we can then explore a bunch of such tuples by taking for example random actions in the environment and recording all these episodes in a key-value pair.

Theoretically speaking once we have the full list of all possible episodes we can learn a policy by picking the highest value action for each possible episode. This approach has two key weaknesses and we'll address them one by one.
1. We can't tell when the table is complete
2. The table is huge

SHOW A DIAGRAM OF THE TABLE

### When is the table complete?

The key to answering this question is almost philosophical in nature and is what the reinforcement learning community refers to as the tradeoff between exploration and exploitation.

You can't fundamentally know when the table is complete, I'm sure if you have the patience you can reduce this to some version of the halting problem.

The analogy here is often best understood with respect to the multi armed bandit problem which is just fancy terminology for a bunch of casino slot machines. 

> Suppose you had $n$ slot machines, how do you which one to pick?

Very informally, the answer is that you would first try a bunch of different ones a couple of times (you would explore). You would keep track of which one was the best one and then use that slot machine a couple of times (you would exploit). If it never dries up, good for you, you're now rich and don't need to read Machine Learning books to be succesful. 

We can represent the above intuition using $\epsilon$-greedy strategy which would look something like 

```julia
function select_arm(algo)
  if rand() > epsilon
    return ind_max(algo.values)
  else
    return randi(length(algo.values))
  end
end
```

This exploration strategy will have to do for now but bear in mind that there's so many different ideas you can experiment with here. One cool one is annealing where you slowly reduce $\epsilon$ over time. When you're learning something new you wanna be really flexible when you're closer to a master you wanna be more rigid


### The table is too damn big

The value tables we deal with in reinforcement learning can be too massive to fit into memory so it's worth thinking about how we can compress it. All of the ideas here fall under a broader field called Representation Learning. For example, when learning a video game we can either use raw pixels or we can directly encode the $x, y, z$ coordinates of each object in the scene after running some object detector.

Finding good representations manually is worthwile and I'll talk about it more in a later chapter but there's one really famous trick to compress the table using a deep neural network and surprise surprise we call it deep reinforcement learning.

The main idea is that instead of explicitly keeping a giga table. We instead keep in memory the weights of a deep neural network. We then modify those weights using succesive applications of back propagation on the error between the output of the net KEEP GOING

## Next steps for what you can learn
* TD learning: Change value of state-action pair after simulating up to n steps
* Monte Carlo sampling: will talk about this in the gambling chapter
* Tabular methods vs deep methods
* Exploration strategies
* Policy gradient vs policy iteration
* How state and actions can be represented by different kinds of sets to get very different behaviors - introduce DDPG idea
* Model learning methods (world learning)
* Using RNN to keep long memory
* Distributed RL
* Advantage Actor critic methods

## Bibliography
* [Summary of all the methods on Medium](https://medium.com/@jonathan_hui/rl-reinforcement-learning-algorithms-quick-overview-6bf69736694d)
* https://medium.com/@SmartLabAI/reinforcement-learning-algorithms-an-intuitive-overview-904e2dff5bbc
* https://www.altexsoft.com/blog/datascience/reinforcement-learning-explained-overview-comparisons-and-applications-in-business/ - applications and challenges of RL
* [Arthur Juliani's RL tutorial](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-7-action-selection-strategies-for-exploration-d3a97b7cceaf)
* [Open AI baselines](https://github.com/openai/baselines)