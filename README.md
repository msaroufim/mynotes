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

## Basics of Reinforcement Learning

## Deep Deterministic Policy Gradients
Vanilla reinforcement such as techniques like Q-learning don't naturally extend to problems with continuous spaces, as in for the most part you'll see Q-learning work really well in discrete environments like board games. You could discretize your continuous space to use Q-learning but if your discretizations are small enough you'll end up with a very large number of states which will substantially slow down the convergence of Q-learning if it converges at all.

DDPG also has two key advantages which make it more user friendly

1. Off policy: which means that the training and testing of the model are independent. With DDPG in particular the testing becomes deterministic which has huge advantages for debugging
2. Model free: which means it doesn't need to build a model of the space it's trying to learn in. This is extremely conveninent since the algorithm doesn't need to store O(f(number of states)) to perform

### How does DDPG work
DDPG is an actor critic algorithm which means it has two neural networks. 

The actor $$\mu(s|theta) $$ provides an action in the form a real valued number given the current state of the environment $$s$$.


The critic $$Q(s,a|\theta) gives an error as a real valued number to criticize the actions made by the actor network.


The specific hyperparameters for the actor and critic network can be found in the original paper. It's very likely that other settings and neural net architectures would probably work but that's something you can optimize if your usecase requires better performance.


## References
* https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html
* http://www.mujoco.org/
* http://www.cs.sjsu.edu/faculty/pollett/masters/Semesters/Spring18/ujjawal/DDPG-Algorithm.pdf
* 