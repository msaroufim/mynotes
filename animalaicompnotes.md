https://www.mdcrosby.com/blog/animalaieval.html
https://github.com/beyretb/AnimalAI-Olympics


Part of making this contest interesting is creating your own tasks since test tasks are unknown but has lots of stuff it could be tested on at evaluation time.

# Testing info
Main commonalities are understanding walls, ramps and tunnels (does ramps require a 3d understanding for this to work or are pixels enough?)
Movable objects like cardboard boxes which vary in weight and shape so the behavior in which they will turn - can we encode an understanding of object shape and how its supposed to move?
Rewards are in the shape of food or zones that give negative or positive reward

### Categories of tasks
1. Food: DQN should work - or dueling DQN, whatever vizbook dudes used
2. Preferences: Measure difficulty of obtaining vs reward
3. Obstacle navigation: create a world physics model or bootstrap via one seperately trained on Unity physics engine?
4. Avoidance: DQN should work
5. Spatial reasoning: CNN to an object encoding ? Physics engine? RNN for memory to remember sequence of actions?
6. Generalization: coloring
7. Internal models: blackout but still need to make actions. World model seems like the only thing that would work here. Store a snapshot of the game world and then try to remisumate it when there are no events happenning. Baseline to beat is not moving during blackout
8. Object permanance: what is the state of the art for encoding RNN with memory?
9. Advanced preferences: planning?
10. Causal reasoning: yeah IDK


# Unixpickle obstacle tower challenge
Codebase has lots of interesting ideas
* core RL code + memory etc..
* Some scripts to evaluate the agents on obstacle tower and log data and plot whatever you need
* A recorder that can help bootstrap the agent with play from a human and past agents
* A web based tool to label objects

# Catalyst starter kit
https://github.com/Scitator/animal-olympics-starter-kit
Can do multiple GPU training for later 

```
# start db node
redis-server --port 12012

# start trainer node
export GPUS=""  # like GPUS="0" or GPUS="0,1" for multi-gpu training
CUDA_VISIBLE_DEVICES="$GPUS" catalyst-rl run-trainer --config ./configs/_exp_common.yml ./configs/ppo.yml

# start sampler node
CUDA_VISIBLE_DEVICES="" catalyst-rl run-samplers --config ./configs/_exp_common.yml ./configs/ppo.yml --sampler-id=1

# view tensorboard logs
CUDA_VISIBLE_DEVICE="" tensorboard --logdir=./logs
```


# Bsuite 

https://github.com/deepmind/bsuite

Loggers are here
https://github.com/deepmind/bsuite/blob/master/bsuite/logging/csv_logging.py
https://github.com/deepmind/bsuite/blob/master/bsuite/logging/sqlite_logging.py
https://github.com/deepmind/bsuite/blob/master/bsuite/logging/terminal_logging.py

Logger is very straightforward but an environment can be wrapped with a logger like so

```python
from bsuite.utils import wrappers

return wrappers.Logging(env, logger, log_by_step=log_by_step)
```

Generalizes the Open AI interfaces

* dm_env.Environment: An abstract base class for RL environments.

* dm_env.TimeStep: A container class representing the outputs of the environment on * each time step (transition).
* dm_env.specs: A module containing primitives that are used to describe the format * of the actions consumed by an environment, as well as the observations, rewards, * and discounts it returns.
* dm_env.test_utils: Tools for testing whether concrete environment implementations * conform to the dm_env.Environment interface.