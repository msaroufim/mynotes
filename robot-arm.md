## Introduction

The goal of today's blog post will be to program the motion of a 2D robotic arm in Python. We won't be using any external libraries so we can focus on learning the inner workings.

Hopefully by the end of this tutorial you'll understand the basics of robotics and how to program robots to achieve their goals using Reinforcement Learning. This technique has the advantage of being very light mathematically in comparison to alternatives which use quite advanced algebra.

If by the end of this tutorial you'd like to learn more then you can expect  further blog post which generalizes the below blog post to a 3D arm.

If using Reinforcement Learning to program goals is of strong interest to you then I'd also like to invite you to sign up at [Yuri.ai](http://www.yuri.ai)

## Robotics environments

There's a wide variety of open source and closed source environments to perform robotic simulations in. A popular one which you'll often see in papers is Mujoco which is a full 3D physics simulator. Mujoco's primary disandvantage is that's it not free and it's personal non-commercial license goes for $500.
 
There are other options such as Gazebo or any game engine such as Unity or Unreal. Unity in particular has recently published [Unity ML agents](https://github.com/Unity-Technologies/ml-agents) which makes it really easy to add intelligence to your Game Objects in a very Unity like fashion.

Another option which keeps us free of big dependencies is building our own simple physics simulator in a graphics engine such as [Pyglet](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/) or a game engine such as [Pygame](https://www.pygame.org/news). While this approach is not recommended if your goal is to eventually publish a Reinforcement Learning  paper or publish a multiplatform game with real users, it has the advantage of being transparent which makes it an excellent first step for us to learn how robotics engines are built with very little magic.

[Mujoco](http://www.mujoco.org/)

![Mujoco environments](mujoco.png)

## Learning in robotics environments

### Inverse Kinematics

The typical approach to learning to solve goals in robotics environments is [Inverse Kinematics](https://en.wikipedia.org/wiki/Inverse_kinematics). At a high level, a robot is comprised of limbs and joints and the goal of Inverse Kinematics or IK is to figure out the joint movements that would help the robot reach a given configuration. These configurations can be quite general, from imitating a certain pose or motion to something like picking an apple. IK is a rich field that has solved many practical problems but we won't go into its details today.

### Reinforcement  Learning approach to IK

Instead we assume that most of our audience is more familiar with Machine Learning techniques and will instead propose a general method to solve goal oriented problems in robotics in a fairly general fashion.

In essence all that's required from the user is to specify the desired goal in code as a reward function and our RL infrastructure will take care of the rest.

As an example in Python, we'd like the finger of a robot to reach a certain goal so we'll translate this in a fairly straightforward manner into the below.

```python
def reward(finger, goal):
    return -distance(finger, goal)
```
Our goal is to minimize the distance betweeen the finger and the goal so we'll output rewards close to 0 when they are close to each other and negative rewards if they are far apart. And that's it! That's the interface we can work with if we're willing to use Reinforcement Learning as an API.

If your only interest is getting things to work then a high level understanding should be enough sufficient but we'll also go through the details and explain how everything works so you can debug it if it comes to that.

## Let's look at some code

### Main function
Let's work backwards assuming that we've already implemented or are using someone elses implementations of some Reinforcement Learning algorithm and/or some robotic environment, how do we put everything together. Or in other words what do we use typical RL and robotics APIs.

#### Setup 
Most RL algorithms will require you specify the sizes of the action and state spaces of the environment you're working with. Since DDPG outputs actions as continuous variables we'll also specify a maximum bound for it. We also need to specify how many episodes we're running the algorithm for and how long each episode lasts.

```python
from env import ArmEnvironment
from rl  import DDPG

#Training specific hyperparameters
#Try modifying these values and see what works
MAX_EPISODES = 500
MAX_EP_STEPS = 200
ON_TRAIN = True

# setup
env = ArmEnvironment()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound
rl = DDPG(a_dim, s_dim, a_bound)
```

#### Training code
Any Reinforcement Learning algorithm will be used in a main function that looks very similar to what you see below. 
1. You start an environment and record its state in a temporary variable
2. You then use this variable to find the optimal action according to the current best policy
3. You feed that action back to the environment to record the new state you're in, by how much you're rewarded and whether you've reached a terminal state
4. The transitions from step 3 are stored in a priority queue to make training more stable
5. Repeat the above until an adequate number of episodes
6. Plot your reward error over time, if things are working correctly this should steadily be going down

```python

def train():
    # start training
    for i in range(MAX_EPISODES):
        s = env.reset()
        episode_r = 0.
        for j in range(MAX_EP_STEPS):
            env.render()

            a = rl.choose_action(s)

            s_, r, goal = env.step(a)

            rl.store_transition(s, a, r, s_)

            #increment reward for the episode by reward taken for the specific action
            episode_r += r
            if rl.memory_full:
                rl.learn()

            s = s_
            if goal or j == MAX_EP_STEPS-1:
                print('Episode: %i | Reward: %.1f' % (i, episode_r))
                break
    rl.save()
```

#### Evaluation code
Evaluation code is even simpler
1. We load the model we trained in the previous section
2. We pick actions according to this new model until we're done

One special note worth mentioning is that we set ```vsync = True``` to make sure that the simulation doesn't go faster than our monitor's refresh rate
```python
def eval():
    rl.load()
    env.render()
    env.viewer.set_vsync(True)
    while True:
        s = env.reset()
        for _ in range(MAX_EP_STEPS):
            env.render()
            a = rl.choose_action(s)
            s, r, done = env.step(a)
            if done:
                break


if ON_TRAIN:
    train()
else:
    eval()
```
### How to program a 2D robot arm
We'll mention again that in practice you'll use a more robust simulator such as the ones in [Open AI gym](https://gym.openai.com/). However, I've found that blindly using someone elses simulator tends to make the behavior seem more complex than it actually is so we'll go over the basics of how to program a 2D robot arm now.


### How to program DDPG
We won't go in detail over the code of DDPG since that would require its own blog post and an extensive explanation of the theory behind Reinforcement Learning but we'll say a few important notes so you can understand why the algorithm is interesting.

### Deep Deterministic Policy Gradients
Vanilla reinforcement such as techniques like Q-learning don't naturally extend to problems with continuous spaces, as in for the most part you'll see Q-learning work really well in discrete environments like board games. You could discretize your continuous space to use Q-learning but if your discretizations are small enough you'll end up with a very large number of states which will substantially slow down the convergence of Q-learning if it converges at all.

DDPG also has two key advantages which make it more user friendly

1. Off policy: which means that the training and testing of the model are independent. With DDPG in particular the testing becomes deterministic which has huge advantages for debugging
2. Model free: which means it doesn't need to build a model of the space it's trying to learn in. This is extremely conveninent since the algorithm doesn't need to store O(f(number of states)) to perform

### How does DDPG work
DDPG is an actor critic algorithm which means it has two neural networks. 

The actor $$\mu(s|theta) $$ provides an action in the form a real valued number given the current state of the environment $$s$$.


The critic $$Q(s,a|\theta) gives an error as a real valued number to criticize the actions made by the actor network.

We'll look at code which will make the above more concrete but it's worth skimming the original [DDPG paper by Silver et al](http://proceedings.mlr.press/v32/silver14.pdf) to get a better idea of how everything works.

The specific hyperparameters for the actor and critic network can be found in the original paper. It's very likely that other settings and neural net architectures would probably work but that's something you can optimize if your usecase requires better performance.


## References
* https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html
* http://www.mujoco.org/
* http://www.cs.sjsu.edu/faculty/pollett/masters/Semesters/Spring18/ujjawal/DDPG-Algorithm.pdf
* 