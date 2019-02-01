## Introduction

The goal of today's blog post will be to program the motion of a 2D robotic arm in Python. We won't be using any external libraries except ```Tensorflow``` and ```numpy``` for the reinforcement learning model so we can focus on learning the inner workings of a robotics environment.

Hopefully by the end of this tutorial you'll understand the basics of robotics and how to program robots to achieve their goals using Reinforcement Learning. The advantage of this technique is that you can program very high level goals simply and learn complex behavior such as motion. You can download the code we'll be using [here](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part5) and run ```python main.py``` and follow the comments from this post.

If by the end of this tutorial you'd like to learn more then you can expect  further blog post which generalizes the below blog post to a 3D arm.

If using Reinforcement Learning to program goals is of strong interest to you then I'd also like to invite you to sign up at [Yuri.ai](http://www.yuri.ai). I'm also writing a book on using Reinforcement Learning for video games where I'll be covering things like Alpha Go Zero, Alpha Star and Open AI 5. If you sign up for [Yuri.ai](http://www.yuri.ai) we'd love to add you to the early access list.

## Robotics environments

There's a wide variety of open source and closed source environments to perform robotic simulations in. A popular one which you'll often see in papers is [Mujoco(http://www.mujoco.org/)] which is a full 3D physics simulator. Mujoco's primary disandvantage is that's it not free and it's personal non-commercial license goes for $500.
 
There are other options such as Gazebo or any game engine such as [Unity](https://unity3d.com/) or [Unreal](https://www.unrealengine.com/en-US/what-is-unreal-engine-4). Unity in particular has recently published [Unity ML agents](https://github.com/Unity-Technologies/ml-agents) which makes it really easy to add intelligence to your Game Objects in a very Unity like fashion.

Another option which keeps us free of big dependencies is building our own simple physics simulator in a graphics engine such as [Pyglet](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/) or a game engine such as [Pygame](https://www.pygame.org/news). While this approach is not recommended if your goal is to eventually publish a Reinforcement Learning  paper or publish a multiplatform game with real users, it has the advantage of being transparent which makes it an excellent first step for us to learn how robotics engines are built with very little magic.


## Learning in robotics environments

### Inverse Kinematics

The typical approach to learning to solve goals in robotics environments is [Inverse Kinematics](https://en.wikipedia.org/wiki/Inverse_kinematics). At a high level, a robot is comprised of limbs and joints and the goal of Inverse Kinematics or IK is to figure out the joint movements that would help the robot reach a given configuration. These configurations can be quite general, from imitating a certain pose or motion to something like picking an apple.

### Reinforcement Learning approach to IK

Instead we assume that most of our audience is more familiar with Machine Learning techniques and will instead propose a general method to solve goal oriented problems in robotics in a fairly general fashion.

In essence all that's required from the user is to specify the desired goal in code as a reward function and our RL infrastructure will take care of the rest.

As an example in Python, we'd like the finger of a robot to reach a certain goal so we'll translate this in a fairly straightforward manner into the below.

```python
def reward(finger, goal):
    return -distance(finger, goal)
```
Our goal is to minimize the distance betweeen the finger and the goal so we'll output rewards close to 0 when they are close to each other and negative rewards if they are far apart. And that's it! That's the interface we can work with if we're willing to use Reinforcement Learning as an API.

## Let's look at some code

A lot of the code is borrowed from [Morvan Zhou from his tutorial in Chinese](https://morvanzhou.github.io/tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1/) His code is very clear but unfortunately does not have any comments which makes it somewhat inaccecible unless you have some background in robotics and reinforcement learning. We'll amend this problem right now.

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
6. Inspect your reward over time, if things are working correctly this should steadily be going up

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

One special note worth mentioning is that we set ```vsync = True``` to make sure that the simulation doesn't go faster than our monitor's refresh rate which is a constraint we can relax to get faster results during training.

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
We'll mention again that in practice you'll use a more robust simulator such as the ones in [Open AI gym](https://gym.openai.com/). However, we've found that blindly using someone elses simulator tends to make the behavior seem more complex than it actually is so we'll go over the basics of how to program a 2D robot arm now.

At a high level what we ne need for the 2D robot environment or for that matter any environment on which we hope to run a reinforcement learning algorithm is the below. If you look at the [core interface in Open AI gym](https://github.com/openai/gym/blob/master/gym/core.py) you'll notice that it looks very similar to the below.

```python
class ArmEnvironment():
    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass
```

We'll skip over the implementation of ```reset``` since it's very similar to ```__init__``` conceptually.

Since we're not looking to create our own graphics library (although this is something you could do if you were interested), we'll be using ```Pyglet``` as a way to render our arms as rectangles and our goal as a square so let's create our ```Viewer``` class now which should take in an ```arm_info``` data structure and a```goal``` and render the state on our monitor.

The most important point below is that ```Pyglet``` displays a batch of rectangles together where each rectangle is composed of 4 vertices and a color.

```python
class Viewer(pyglet.window.Window):
    thickness = 5
    def __init__(self, arm_info, goal):
        # vsync=False to not use the monitor FPS, we can speed up training this way
        super(Viewer, self).__init__(width=400, height=400, vsync=False)

        #make screen black so you can start rendering other stuff on it
        pyglet.gl.glClearColor(0, 0, 0, 0)

        #take our arm state
        self.arm_info = arm_info
        self.center_coord = np.array([200, 200])

        self.batch = pyglet.graphics.Batch()
        
        #Render goal
        self.goal = self.batch.add(
            # Goal is a square: specify its 4 corners with v2f
            4, pyglet.gl.GL_QUADS, None,    
            ('v2f', [goal['x'] - goal['thickness'] / 2, goal['y'] - goal['thickness'] / 2,               
                     goal['x'] - goal['thickness'] / 2, goal['y'] + goal['thickness'] / 2,
                     goal['x'] + goal['thickness'] / 2, goal['y'] + goal['thickness'] / 2,
                     goal['x'] + goal['thickness'] / 2, goal['y'] - goal['thickness'] / 2]),
            
            #specify its color with c3b
            ('c3B', (255, 0, 0) * 4)) 
        
        # Can generalize the below to multiple arms
        # Let's do 2 arms for now
        # Same idea as for goal, we have 4 corners specified by their x, y location on our window with a color for each arm
        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,                
                     250, 300,
                     260, 300,
                     260, 250]),
            ('c3B', (255, 255, 255) * 4,))   
        self.arm2 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [100, 150,             
                     100, 160,
                     200, 160,
                     200, 150]),
                    ('c3B', (255, 255, 255) * 4,))
```

[Arm screenshot](arm.png)

Great now we can display an arm! Let's think a bit more about how to represent the state of the arm environment and then how to move the arm around and how we'll make this environment work with our reinforcement learning code. The Arm environment needs to hold the following key information
1. A viewer class 
2. State dimension which consists of
    - Whether the goal was reached
    - The position of the two joints on the screen
    - The distance of the joints to the goal
3. Action dimension which consists of the two joints we're operating on with a scalar value that would nudge each one up or down to make them more likely to reach the goal
4. An arm info data structure which keeps track of the length of each arm and the radius the arm makes with a horizontal line going through the center of the screen.

```python
class ArmEnvironment():
    #Pyglet specific viewer, we could use others like pygame
    viewer = None

    # refresh rate
    dt = .1    

    #we specify a goal 
    goal = {'x': 100., 'y': 100., 'thickness': 10}
    
    #state is comprised of 9 elements
    state_dim = 9

    #we have two joints which we'll put forces on
    action_dim = 2

    #actions correspond to a nudge up or down
    action_bound = [-1, 1]


    def __init__(self):

        #Will track arm length and arm radius info in the same data structure
        self.arm_info = np.zeros(
            2, dtype=[('l', np.float32), ('r', np.float32)])
        
        #arm lengths
        self.arm_info['l'] = 100 

        #arm radiuses       
        self.arm_info['r'] = 0

        #boolean variable that tracks whether finger is on the goal   
        self.on_goal = 0


```

Many of the remaining functions are formalities so we'd suggest you check out the repo directy to understand how they work so let's get to the meaty part which is the ```step``` function.

```python
    def step(self, action):
        done = False
        action = np.clip(action, *self.action_bound)
        self.arm_info['r'] += action * self.dt

        # normalize angles
        self.arm_info['r'] %= np.pi * 2    

        # arm 1 and 2 lengths
        (a1l, a2l) = self.arm_info['l']

        # arm 1 and 2 radiuses
        # map to theta 1 and theta 2 on the image
        (a1r, a2r) = self.arm_info['r']
        a1xy = np.array([200., 200.])    # a1 start (x0, y0)

        # look at screenshot below to convince yourself that this works
        # a1xy is the origin joint at the base of arm 1
        # a1xy_ is the point between the two arms
        # finger is the point at the tip of arm 2
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy
        finger = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_

        # We are choosing to represent the state of the arms as a function of the distance from the goal
        # there are other ways to do this that would work just fine including automatic ones using convnets
        # the 400 is there because we are normalizing distances by the window size
        dist1 = [(self.goal['x'] - a1xy_[0]) / 400, (self.goal['y'] - a1xy_[1]) / 400]
        dist2 = [(self.goal['x'] - finger[0]) / 400, (self.goal['y'] - finger[1]) / 400]

        # The reward function could be engineered further but for now we'll just say we want the finger to be close to the goal
        r = -np.sqrt(dist2[0]**2+dist2[1]**2)

        # if the finger touches the goal we want to give it a big bonus reward
        if self.goal['x'] - self.goal['thickness']/2 < finger[0] < self.goal['x'] + self.goal['thickness']/2:
            if self.goal['y'] - self.goal['thickness']/2 < finger[1] < self.goal['y'] + self.goal['thickness']/2:
                r += 1.

                # We are done when the finger stays on teh goal for more than 50 iterations
                # This is to prevent the agent from learning a flailing policy
                self.on_goal += 1
                if self.on_goal > 50:
                    done = True
        else:
            self.on_goal = 0

        # state is of size 9 because we have two joints each need 2 points to describe
        # we have one distance with two values to describe
        # and boolean for whether we are on goal or not
        s = np.concatenate((a1xy_/200, finger/200, dist1 + dist2, [1. if self.on_goal else 0.]))
        return s, r, done
```




We still have one more loose end when it comes to the arm environment, we need to update what's displayed on screen and we can do this by adding an additional function to our ```Viewer``` class. The ```update_arm``` function works in the following way
1. Calculate joint positions
2. Calculate new joint positions after movement
3. Given the new joint positions use trigonometry to move each vertex of each rectangle the appropriate amount
4. Redraw the rectangles

```python
    def _update_arm(self):
        (a1l, a2l) = self.arm_info['l'] 
        (a1r, a2r) = self.arm_info['r']    
        
        #calculate joint positions
        a1xy = self.center_coord    
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy
        a2xy_ = np.array([np.cos(a1r+a2r), np.sin(a1r+a2r)]) * a2l + a1xy_

        #figure out by how much joints need to be rotated
        a1tr  = np.pi / 2 - self.arm_info['r'][0] 
        a2tr = np.pi / 2 - self.arm_info['r'].sum()

        #Rotate 4 vertices of the first arm rectangle
        xy01 = a1xy + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.thickness
        xy02 = a1xy + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.thickness
        xy11 = a1xy_ + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.thickness
        xy12 = a1xy_ + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.thickness

        #Rotate the 4 vertices of the second arm rectangle
        xy11_ = a1xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.thickness
        xy12_ = a1xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.thickness
        xy21 = a2xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.thickness
        xy22 = a2xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.thickness

        self.arm1.vertices = np.concatenate((xy01, xy02, xy11, xy12))
        self.arm2.vertices = np.concatenate((xy11_, xy12_, xy21, xy22))
```



### Deep Deterministic Policy Gradients
We won't go in detail over the code of DDPG since that would require its own blog post and an extensive explanation of the theory behind Reinforcement Learning but we'll say a few important notes so you can understand why the algorithm is interesting. For this tutorial we've chosen DDPG as our reinforcement learning algorithm of choice but any reinforcement algorithm that can output continuous values would also work. So an alternative way of going about this tutorial would be to plug a bunch of the reinforcement learning algorithms from [Open AI baselines](https://github.com/openai/baselines) and see what works best.

Vanilla reinforcement such as techniques like Q-learning don't naturally extend to problems with continuous spaces, as in for the most part you'll see Q-learning work really well in discrete environments with a fixed number of actions e.g: Super Mario bros. You could discretize your continuous space to use Q-learning but if your discretizations are small enough you'll end up with a very large number of states which will substantially slow down the convergence of Q-learning if it converges at all.

DDPG also has two key advantages which make it more user friendly

1. Off policy: which means that the training and testing of the model are independent. With DDPG in particular the testing becomes deterministic which has huge advantages for debugging
2. Model free: which means it doesn't need to build a model of the space it's trying to learn in. This is extremely conveninent since the algorithm doesn't need to store O(f(number of states)) to work and in our case the number of values the states can take is infinite because the environment is continuous.


### Putting everything together

Given the 3 components we built above we're now finally ready to see the fruits of our labor. Remember we have
1. The DDPG algorithm which is a reinforcement learning algorithm that outputs continuous values
2. An Arm environment that keeps track of its state and can render itself using ```Pyglet```
3. A training and evaluation pipeline

As far as I know it's not possible to run ```Pyglet``` inside of a Jupyter notebook, so you can train the arm using Floydhub for best results and then view your results on your local machine. We've tested the arm on Mac OS X.

## ADD GIF VIDEO HERE

### Outro
I hope you've enjoyed reading this article as much as I've enjoyed writing it and if you did please let us know if you'd like to read more similar posts.
* [Add me on Github](https://github.com/msaroufim)
* [Sign up for Yuri](http://www.yuri.ai) 


## References
* https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html
* http://www.cs.sjsu.edu/faculty/pollett/masters/Semesters/Spring18/ujjawal/DDPG-Algorithm.pdf

* https://github.com/MorvanZhou/train-robot-arm-from-scratch