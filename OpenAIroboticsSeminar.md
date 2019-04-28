# TL;DW: Summary of Open AI robotics symposium 2019
https://www.youtube.com/watch?v=WRsxoVB8Yng

## Matthias Plappert - Opening
* Talked about overall Open AI mission
* Event is about helping people in robotics meet people in ML and vice versa
* How to design robots that learn efficiently and safely, factory robots are dangerous so it's worth design robots that don't kill you if they make mistakes

## Wojciech Zaremba - Learning Dexterity
* Lots of robots exist out there today but they don't interact much with the environment e.g: Roomba, quadcopter
* Reinforcement Learning is a tempting solution for robots since it works really well for games like and Dota but it's sample inneficient, both of the above games took around 40,000 years of data to train
* Dexterity that can be achieved by training on physical robots is more constrained than in a simulator
* It's important to be able to reset a physical environment when it fails
* Measuring reward signals for physical robots requires sensors which is OK for grasping but more challenging for environments like riding a bike
* Goal: train complex policies in simulation but run on the real robot
* A robot can solve a variety of tasks requires a flexible morphology (e.g: human hand) that can then solve several tasks. As opposed to having a bottle morphology for opening bottles
* Task: reorient an object in hand - in software ez but in hardware challenges since tips of fingers for e.g are soft rubber bodies which aren't simulated
* Sensors inside of physical hand are magnetic so they interfere with each other so had to build a cage with external sensors to measure the state of the physical hand
* Domain randomization: simulators can be used to generate tons of training data (Sadeghi and Levine 2016) and this idea applies well to Reinforcement Learning - visually change colors and lighting and physical properties of the simulator  to make it learn better in the physical world (Peng et Al 2017)
* Use distributed workers to collect experiences at a large scale then
    * Train control policy using RL that picks the next best action based on fingertip position and object pose
    * Use a CNN to predict the object pose given three simulated camera images
* Combine pose estimation and the control policy to give an action
* Randomize gravity vector, joint limit, actuator force gains, surface friction coefficients, object and robot link masses, object dimension, noisy observations, noisy actions
* Training is done with PPO and Architecture has rollout workers with 6,000 CPU cores and optimizers consists of 8GPUs
* Value functions have different inputs like fingertip positions, target orientation, object pose, hand joint angle and velocities etc..
* Lots of emergent behaiors like sliding, finger pivoting and finger gaiting which is because theres only a high level reward function. Several known grasping behaviors are seen like tip pich grasp, palmar, trippd, quadpop, power, 5 finger precision
* Experiments show taht randomization increases physical success dramatically
* Best experiments used LSTM (vs feedforward) for both the policy and value function
* TL;DR: Distribution of environments + memory = meta learning

## Pierre Sermanet - Learning from play
* Does not use Reinforcement learning and uses self supervision and play instead since it's difficult to have robots work on labels
* So best to work on unlabeled data and this work shows how to do this for vision and control
* Supervision costs: playing is free, then imitation then demonstrations then labeled frames
* Self supervision can lead to higher sample efficiency in RL
* Labeling is hard to define for robot tasks
* Play here means looking at data from agents that can already play like children but not robots right now
* TCN, TCC and OCN networks can produced disentangled invariant states and attributes for visual representations
* Can do semantic alignment between two control tasks using TCN and using this new embedding we can feed it to a reinforcement learning algorithm to learn a policy with a small number of iterations vs pure RL
* Temporal cycle consistency, given 4 videos you can align them (best approach is TCC +TCN) and can visualize the progress using t-SNE
* Pose imitation can also be done by play with self supervision
* Tasks live on a continuum since many discrete tasks are somewhat similar to each other and this continuum can be covered by using learning from demonstration and learning from play. Data is created by having a human play in the simulator in VR for 3h
* Instead of predicting action predict how far away you are from the correct action. Can do KL divergence between the detected plan and the current plan to decode out an action distribution from which you can sample an action
* Play-LMP result is a task agnostic policy and evaluate it on 18 zero shot tasks
* Skills can be composable

## Leslie Kaelbling - Doing for our robots what nature did for us
* Very charismatic speaker!
* Good proxy problem: make tea in a kitchen you've never been in before. This is hard even for humans
* When robots come out of a factory they need to be encoded with some policy that optimizes over a distribution over environments with some sort of objective function
* 3 approaches for this: reverse engineer humans (hard), evolution (slow), engineered (hard)
* Use insights from different scientific fields as bias to the factory
* Ideal of a pile of wires that is smart is a fantasy and we have to design an agent with lots of structure and many small circumscribed learning problems
* Build in general algorithms and learn models (use IK, path planning etc...)
* Belief space hierarchical planning in the now - showed large graph which combines many different ideas from ML, control and robotics
* Information theoretically Go is easy if you have infinite compute but problems with learning about the world is harder because there are more real time constraints
* Dynamics modeling in large hybrid domains: MCTS wont work cause of large branching factor but task and motion planning strategies such as constrained optimization and pre image back chaining
* Can use ideas from active learning - robot experience is expensive
* Have several submodels and then build a transition model
* Deictic rules: rules around where other objects are situtated around each other is important to learn. So don't plan over pixels directly but plan over objects

## Anca Dragan - Treating People as Optimizers in Human-Robot Interaction
* Humans and robots interacting setting
* Robot policy is a function of policy of human, it's very difficult to model humans in a closed form
* Other approach treat human behavior as a black box, collect a bunch of data and then integrate it into the full model
* Continue at 3:26
## Jin Joo Lee - Social-Emotional Intelligence in Human-Robot Interactions 

## Chris Atkeson - What Should Be Learned?

## Jeff Clune - Robots that adapt like natural animals 

