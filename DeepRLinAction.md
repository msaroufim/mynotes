# Deep RL in Action notes

## Chapter 1: What is RL
* General overview of SL, UL and RL
* Brief overview of Turing and quest for intelligence
* History of backprop
* RL doesn't need labeled data
* History of Dynamic programming
* Deep Q-network: 1 algorithm for multiple games vs IBMs deep blue
* Simulated environments have all sorts of advantages e.g
    - Quantopia: portfolio simulator
    - self driving car simulator
* Uses Open AI gym to play Go, control robots and do non linear dynamics


## Chapter 2: Modeling RL problems - markov decision processes
* Reintroduces general framework of RL: Agent takes an acito nwihch changes the environment
* Starts off with discussing bandit problems
* Builds networks with Pytorch and introduces the idea of automatic differentiation. Gives a very quick Pytorch introduction that's pretty clear
* Goes over examples of what has the markov property (driving a car) vs what doesn't (diagnosing a patient)
* Defines policy, optimal policy, value function, 



## Chapter 3: Predicting the best states and action: deep Q networks
* Defines the gridworld problem
* Introduces the Atari DQN approach. Q learning has been around for decades (can get a specific year from the Sutton and Barto book)

```python
def get_updated_q_value(old_q_value, reward, state, step_size, discount):
 term2 = (reward + discount * max([Q(state, action) for action in actions])
 term2 = term2 – old_q_value
 term2 = step_size * term2
 return (old_q_value + term2) 
```

* Has nice code samples on training and testing Q-networks using Pytorch
* Talks about experience replay
* Improving stability with a target network

## Chapter 4: Learning the best policy - policy gradient methods
* Discusses difference between Q learning and policy gradients - here is a good stat exchange site that goes over this https://ai.stackexchange.com/questions/6196/q-learning-vs-policy-gradients
* I should find a good concise explanation of the difference between Q-learning and policy gradient methods
## Chapter 5: