# How to learn? Introduction to Reinforcement Learning

Try to imagine what it was like when you were a young child, you aimlessly explore around an environment. At this point you aren't preprogrammed with any notion of what's safe or dangerous, what's useful vs a waste of time.

So there you are, happily exploring on all fours. At some point you get bored and you try walking on your two feet instead. The giants in the room with you seem to lose their collective minds, they start crying, patting each other on the back, they call their relatives and make sure to film the entire ordeal on their phones. 

They call you a good boy, and you don't know why but your entire body delights at being called a good boy.

> You wanna be a good boy

You take a nap and wake up a couple of hours later, you feel pretty hungry, so you start staring at the dust and cat hair on the floor. You grab a tiny handfull and stuff it in your mouth, it's not too bad, the textures are pretty unique relative to what you've had before, the flavor suggests that it's an acquired taste. No sooner as you start putting your finger on the taste, do you see

> You don't wanna be a bad boy

## Pavlovian learning

Turns out you can explain most human behavior by combining two things
1. Wanting to be a good boy
2. Not wanting to be a bad boy


So here we are, thinking we're somehow special even though we can read but not understand texts like "Critique of Pure Reason".

Once you see this pattern it's almost impossible to unsee and you can start mapping how all your actions are either in anticipation of a reward (good boy points) or in escape of a punishment (bad boy points)

It's important to note that 1 and 2 are with respect to some parent/teacher/master that is fully responsible for creating your rewards. There is a trick to make this work for an organism without any sort of teacher or judge which we'll cover later (Curiosity driven learning).

## Mathemizing Pavlovian Learning: Reinforcement Learning

We're gonna try to formalize the main intuition of Pavlovian Learning mathematically so we're gonna start by introducing some terminology.

$A$ is the set of all actions
$S$ is the set of all states

Your goal is to learn a policy $\pi$ where a policy is defined

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

Return of reward formula

Discounted reward formula