Good tutorial for racing game,  training a self driving car: https://github.com/araffin/learning-to-drive-in-5-minutes

RTS and SC2: https://www.youtube.com/watch?v=v3LJ6VvpfgI&list=PLQVvvaa0QuDcT3tPehHdisGMc8TInNqdq - good for rule based starcraft

For tutorial using Open AI baselines starcraft can use
https://github.com/chris-chris/pysc2-examples

Platformer: example chase sequence in Celeste 
https://github.com/chris-chris/mario-rl-tutorial

Robotics: MorvanZhou tutorials on github

Need to find something for MOBA. In particular need to figure out how to use LSTM to model games of imperfect information. [This paper](https://arxiv.org/pdf/1507.06527.pdf) for example uses an RNN as the last layer of the Q learning networks but based on experimental results there wasn't that much evidence that this approach does all that much more than something like experience replay

For board games use Alpha Zero from Deep Learning and the game of go book

Need to understand curriculum learning better and whether Alpha Star or any game actually need it https://www.doc.ic.ac.uk/~ejohns/Documents/diego_mendoza_barrenechea_thesis.pdf

RL for blackjack https://towardsdatascience.com/playing-blackjack-using-model-free-reinforcement-learning-in-google-colab-aa2041a2c13d

RL poker http://willtipton.com/coding/poker/2017/06/06/shove-fold-with-reinforcement-learning.html

Remember Policy gradient is a classification and DQN is a regression. Obvious if you look at the code https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Policy%20Gradients/Doom/Doom%20REINFORCE%20Monte%20Carlo%20Policy%20gradients.ipynb not much changes besides the loss at the final layer
=======
Good article that explains what target networks are exactly https://medium.freecodecamp.org/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682

Don't forget arthur juliani class https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df

Evolutionary strategies are a form of random search where weights are sampled randomly at first and resampled from where the best random weights were with some noise. ES are easier to implement than backprop and can be parallelized in a more trivial manner.

RL is guess and check on actions while ES is guess and check on parameters
ES is parallelizable, deals well with credit assignment problems since we dont' have to reason over long timescales and more robust to tuning hyperparameters

Imitation learning is about turning an RL task into a supervised learning task. Example: given a chess position predict the move that top players would most likely play next. It works as a great bootstrapping method before self play starts.

* https://medium.com/@benjamin.phillips22/evolution-strategies-as-a-scalable-alternative-to-reinforcement-learning-paper-summary-691161b52ddd
* http://blog.otoro.net/2017/10/29/visual-evolution-strategies/
* https://blog.openai.com/evolution-strategies/

Rainbow networks combine all the famous DQN architecutres into one and is used as a benchmark in the Unity obstacle tower challenge
* https://twitter.com/awjuliani/status/1095028459389083649
* https://arxiv.org/pdf/1710.02298.pdf

Differentiable ray tracing engine https://people.csail.mit.edu/tzumao/diffrt/diffrt.pdf
Differentiable robotics engine https://arxiv.org/pdf/1611.01652.pdf - main idea is that they implemented a physics engine where the parameters can be differentiated with respect to the loss. Uses similar ideas to spring engines which are used in fluid dynamics and write the equations in Pytorch and then have them backpropped automatically.

Neural ODE: https://jontysinai.github.io/jekyll/update/2019/01/18/understanding-neural-odes.html

EVolutionary optimization book: https://www.researchgate.net/file.PostFileLoader.html?id=576447195b4952c3d05d7f7b&assetKey=AS:374040414965760@1466189593059

It may make sense to have a chapter on scaling RL techniques where I cover
* A2C and A3C
* Multi CPU and Multi GPU training

Keras implementations of all the RL algorithms: https://github.com/flyyufelix/VizDoom-Keras-RL

Can run Open AI baselines on Unity environment using this https://github.com/Unity-Technologies/ml-agents/tree/master/gym-unity

Interesting code bases
* https://github.com/peter1591/hearthstone-ai
* https://arxiv.org/pdf/1708.00730.pdf
* http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/games.pdf

Good RL survey in different environments: https://arxiv.org/pdf/1708.07902.pdf 
* document has two beautiful visualizations of all the RL algorithms
* list of open problems is also interesting
* Talks about what kinds of AI is used for each kind of game and gives canonical examples from each of those game genres


Good summary of RL techniques
* https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html#common-approaches


Hanabi learning environment: RL techniques suck for this and especially suck for more than 3 players https://www.researchgate.net/publication/330845137_The_Hanabi_Challenge_A_New_Frontier_for_AI_Research

I don't fully understand this paper but Bayesian ideas can be used in Hanabi: chrome-extension://bjfhmglciegochdpefhhlphglcehbmek/content/web/viewer.html?file=https%3A%2F%2Farxiv.org%2Fpdf%2F1811.01458.pdf - main idea is that when you see another player play an action you simulate what will happen from their perspective and see if that means you should be playing something


Auto ML, RNN samples blocks from common NN architecuteres to minimize some function. Kind of like RL, sequential decision making
* https://arxiv.org/pdf/1707.07012.pdf
* https://github.com/jhfjhfj1/autokeras
