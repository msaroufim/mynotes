# Notes on grokking deep reinforcement learning

## Chapter 1: Introduction
Introductory chapter talks about
* The origins of the term artificial intelligence
* The high level differences between supervised learning, unsupersived and Deep RL
* The tabular approach to RL and how Deep RL makes it more scalable
* Mentions space complexity for atari games and how Go and chess have more positions than there are atoms in the universe then approximation methods are a must
* The reasons why DRL can work now: better algorithms, better compute, more games engines than ever before
* Early success stories like
    -  TD Gammon: used a NN classifier to compute probability of winning with handcrafted features
    - Inverse Reinforcement Learning: Andrew Ng research team to teach a helicopter to fly by watching experts (anything from youtube videos has immense value)
    - Policy Gradient: to play in robot tournaments
* Field picked up again when DeepMind published their DQN algorithm to teach agents how to play Atari games straight from Pixel values. After that there were several more innovations with DPG, DDPG and TRPO algorithms
* Big commercial successes came in the form of Alpha Go Zero
* In 2018 we had Open AI 5 and in 2019 we had AlphaStar
* Alpha Go was bootstrapped on professional players and this was only possible because Go and Chess are old and richly documented games. Odds are unless you're the lead AI researcher at Blizzard or Valve you're not in a similar situation so having an approach that works without bootstrapping such as Alpha Go Zero is immensely powerful
* Has some parts talking about the singularity and how revolutions are becoming more frequent in our time
* When to use DRL and when not to use it
    - Exploration strategy in games can involve catastrophic failures but not so much in the real world like self driving cars
    - Hierarchichal tasks where humans don't need to relearn basic motions if they know how to use a wrench, it doesn't take much more time to learn how to use a screwdriver. Transfer learning should be faster in principle but again assumes you have training data to look at
* Main issue of DRL is that it's not very sample efficient so it'll take time to get an initial interesting agent that works well 
* Intrinstic motivation is a good exploration strategy, it's mentioned in more detailed in an Open AI blogpost
* There is a nice image on page 26 that compares various approaches to DRL and how they compare on sample efficiency, their control and computational complexity
* What you will need
    - Previous basic knowledge in ML
    - Setting up an environment: headless servers, jupyter notebooks etc..
    - Curiousity to check out papers, dive into Github projects and experimenting with hyperparameters

## Chapter 2: Planning for sequential decision making problems

* Mostly a simplified explanation of first few chapters from Sutton and Barto. It's going to be very important for me to have code, an environment and the basic mathematical equations (proofs most likely not necessary but Sutton and Barto should be mentioned)
* Very worthwhile to go through the Ipython notebook for the this chapter and play around with it
* It is difficult in a sequential process to figure out which exact action was most responsible for a future reward
* Sets up the main structure of a sequential decision problem with an agent an environment
* Some games like Chess are fully observable others like Poker or Starcraft are partially observable
* Explains Frozen Lake environment which has the Markov property where given the current state and action we are independent of the history of interactions (not true for partially observable games)
Actions can be taken deterministically or probabalistically
* Shows equation for transition function
* Shows how to engineer a basic reward signal. Rewards can be negative. Also shows math for reward
* I don't think I can get away from explaining the basics of RL in the first chapter
* Time horizon also needs to be set. Infinite horizon vs horizon of length 1 is called greedy
* Several types of MDPS: POMPD, CMDP (continuous), multi agent MMDP, RMDP (can integrate relational knowledge)
* I really like how the author labels an example output of frozen with the
    - state
    - action
    - probability of transitioning to new state
    - reward at new state
    - terminal flag
* Value of a state = expected returns from that state by following the current policy
* Value of taking an action = value of a state where we'd end up with new action
* Advantage function: difference between value of state and value of action from that state
* policy iteration and evaluation: gives simple mathematical explanation + code + intuition
* Also codes up the basic frozen lake environment and encourages the reader to change the goals and stochasticity of the environment

## Chapter 3: Learning to act through interaction

* Interestingly enough book doesn't go over stuff like how to install Python or TF etc.. - I wonder how much time I should spend on this stuff
* Will learn to solve decision making problems when the dynamics of the envrionment are unknown
* Will look at different exploration strategies
* Optimality requires exploring new things and gives examples based off of hjuman psychology to illustrate the point
* How much do you explore vs exploit, goes over bandit problem to illustrate this point
* Exploration strategies fall under
    - random exploration
    - optimistic exploration: exploring states with the highest amount of uncertainty
    - information state-space exploration strategies: make uncertainty a property of the environment state when modeling
* Codes up greedy strategy and then epsilon greedy strategy in Python and then decaying epsilon greedy action selection to maximize exploitation in the later parts of a game
* Also adds benchmarking code for the different kinds of environments uses ```import  gym_bandits``` for the different bandit implementations and ```import tqdm``` to see how long each iteration of a for loop is taking
* Uses Monto Carlo learning to collect episodes from learning in the Frozen Lake environment. MC learning looks at a full episode before updating its value function while something like TD learning can update even after a single observation
* Goes over SARSA pseudocode which is on policy learning
* There are other off policy algorithms like Q-learning
* Also goes over Double Q learning which helps minimize some of the bias of Q learning. Q learning tends to overestimate the value of certain states

## Chapter 4: More effective and efficient Reinforcement Learning
* UCB frequentist aprpoach vs Thompson sampling as bayesian approach
* Sofmax exploration strategy
* Model based reinforcement learning: Dyna architecture
* Is it better to wait 1 step, 2 steps .. n steps before updating estimate or we could use a weighted function of all of them for our estimate - this is what $$TD(\lambda) $$ is all about
* Next chapter is on deep RL methods