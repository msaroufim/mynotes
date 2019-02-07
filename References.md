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