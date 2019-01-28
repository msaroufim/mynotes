## Introduction

The goal of today's blog post will be to program the motion of a 2D robotic arm in Python. We won't be using any external libraries so we can focus on learning the inner workings.

Hopefully by the end of this tutorial you'll understand the basics of robotics and how to program robots to achieve their goals using Reinforcement Learning. This technique has the advantage of being very light mathematically in comparison to alternatives which use quite advanced algebra.

If by the end of this tutorial you'd like to learn more then you can expect  further blog post which generalizes the below blog post to a 3D arm.

If using Reinforcement Learning to program goals is of strong interest to you then I'd also like to invite you to sign up at [Yuri.ai](http://www.yuri.ai)

## Main components

### Arm environment
We will first need to program an arm in Python and since we'll be teaching the arm how to move using Reinforcement Learning, we'll need an interface that's amenable to reinforcement learning.

More precisely this usually means
* A way to initiate the environment
* A way to step through the environment given an action
* A way to restart the environment

And we'll also add a render function so we can see results on screen since dealing with numbers for simulations while correct is opaque and uninspiring.

Or in Python code


```python
class ArmEnv(object):

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass
```

### Deep Determninistic Policy gradient
We won't go through the basics of Reinforcement Learning in this blog post and will point our readers to the previous post by [INSERT POST HERE]

It suffices to know that we'll use Deep Deterministic Policy Gradients which for the rest of this blog post we'll refer to as DDPG.

A DDPG class will need
* A way to execute a policy
* A way to learn a policy
* Some memory to store the transitions it's seen

```python
class DDPG():
    def __init__(self, a_dim, s_dim, a_bound,):
        pass

    def choose_action(self, s):
        pass

    def learn(self):
        pass

    def store_transition(self, s, a, r, s_):
        pass
```

### Main file
We'll also have a main file to orchestrate the training and visualize the training process

## Back to the arm environment
Let's start implementing the functions of the interface we've laid out
```python
class ArmEnv():

    def __init__(self):
        pass

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass
```
Let's get started with the easy functions init and reset
```python
#Rename below l and r to something more readable
def __init__(self):
    self.arm_info = np.zeros(
        2, dtype=[('l', np.float32), ('r', np.float32)])
    self.arm_info['l'] = 100        # 2 arms length
    self.arm_info['r'] = np.pi/6    # 2 angles information

def reset(self):
    #bring back the arms to their original rotation
    #arm length remains unchanged
    self.arm_info['r'] = 2 * np.pi * np.random.rand(2)
    return self.arm_info['r']

```

Then we'll implement the render function using the Pyglet library

Finally the meat is in the step function

```python
class ArmEnv():
    viewer = None
    dt = .1    # refresh rate
    action_bound = [-1, 1]
    goal = {'x': 100., 'y': 100., 'l': 40}
    state_dim = 2
    action_dim = 2



    def step(self, action):
        done = False
        r = 0.
        action = np.clip(action, *self.action_bound)
        self.arm_info['r'] += action * self.dt
        self.arm_info['r'] %= np.pi * 2    # normalize

        # state
        s = self.arm_info['r']

        (a1l, a2l) = self.arm_info['l']  # radius, arm length
        (a1r, a2r) = self.arm_info['r']  # radian, angle

        #Position of first joint
        a1xy = np.array([200., 200.])    # a1 start (x0, y0)
        
        #Position of second joint
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy  # a1 end and a2 start (x1, y1)
        
        #Position of third joint
        finger = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_  # a2 end (x2, y2)

        # if close to goal in x and y distance then end give reward
        # can refactor this into a single if condition
        if self.goal['x'] - self.goal['l']/2 < finger[0] < self.goal['x'] + self.goal['l']/2:
            if self.goal['y'] - self.goal['l']/2 < finger[1] < self.goal['y'] + self.goal['l']/2:
                done = True
                r = 1.
        return s, r, done
```

## Putting everything together
Notice that the step function looks like
```python
"""
Plug a RL method to the framework, this method can be discrete or continuous.
This script is based on a continuous action RL. If you want to change to discrete RL like DQN,
please change the env.py and rl.py correspondingly.
"""


#SETUP

MAX_EPISODES = 500
MAX_EPISODE_STEPS = 200
ON_TRAIN = True

# set env
env = ArmEnv()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

# set RL method (continuous)
rl = DDPG(a_dim, s_dim, a_bound)


def train():
    # start training
    for i in range(MAX_EPISODES):
        s = env.reset()
        ep_r = 0.
        for j in range(MAX_EPISODE_STEPS):
            env.render()

            #pick an action
            a = rl.choose_action(s)

            #observe new state and reward
            s_, r, done = env.step(a)

            rl.store_transition(s, a, r, s_)

            ep_r += r
            if rl.memory_full:
                # start to learn once has fulfilled the memory
                rl.learn()

            s = s_
            #break once max number of steps are reached
            if done or j == MAX_EPISODE_STEPS-1:
                print('Ep: %i | %s | ep_r: %.1f | steps: %i' % (i, '---' if not done else 'done', ep_r, j))
                break
    rl.save()


def eval():
    rl.restore()
    env.render()
    env.viewer.set_vsync(True)
    while True:
        s = env.reset()
        for _ in range(200):
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
We'll need to supply the step function