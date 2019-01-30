# Deep Learning and the Game of Go

* Book starts with a foreword by the alphaGo team that highly recommends the book.
* Authors built an open source engine called BetaGo that combines RL and Monte Carlo Tree Search.
* Book builds up towards one key idea, how to make ALpha Go and Alpha Go Zero work


## Chapter 1: Towards Deep Learning a Maching learing introduction
* ML vs traditional programming
* ML as a subfield of AI including logic systems, expert systems and fuzzy stems
* Don't use ML when there are other closed form solutions or simple heuristics work better or when you expect perfect accuracy
* How to model a linear function
* Brief summary of libraries like NumPy, TensorFlow, Keras
* Basic explanation of Supervised learning and examples that relate to Go
    - Given games 
    - Given a board position, how likely are you to win from that state
* Unsupervised learning
    - Find units that belong to the same group
* Reinforcement learning: attempt task, evaluate success, generate training data and improve agent
* Deep Learning: each layer models higher order concepts and allows you learn representations
* DL is a good choice when
    - Data is unstructured
    - You have large amounts of data
    - You have plenty of computing power or plenty of time
* DL is a bad choice
    - When model is essentially somehting like a spreadsheet
    - You want an interpretable model you can debug

## Chapter 2: Go as a machine learning problem
* It's dangerous to train robot in the real world directly since it can cause accidents so doing things in a simulated environment is a generally good idea
* Goes over a simple explanation of the rules of Go
    - Standard board is 19x19 but we can work with a smaller board first to make sure things work
    - Players alternate placing stones
    - You capture opponents stones by filling all their liberties
    - A group with two unconnected liberties can't be captured (strategy mostly comes from this rule)
    - When both players pass game ends, dead stones are considered captured stones unless of one the two players contests this
    - You can't play a move that would return teh board to a previous state
    - Score is one point for every point surrounded by your own stones + one point for every captured enemy stone 
    * Go to online-go.com to play the game
* Go bots typically have opening databases (Chess also has endgame databases but this is not possible in Go)
* Core idea behind board game AI is tree search
* Branching factor of Go is 250 vs Chess. This is something worth thinking about when building the AI for any board game
* Start off with a supervised learning approach where you predict the human move
* Can setup your Go AI on a public server vs other Go engines to benchmark it or setup a Go server for humans to play against

## Chapter 3: Implementing your first Go bot
* Chapter goes over the code found in [this repo](https://github.com/maxpumperla/deep_learning_and_the_game_of_go/blob/master/code/dlgo/goboard_slow.py)
* Uses Python ```@property``` a lot for getters and setters
* Prints board as text
* Creates a random agent
* To detect whether Ko position happened in the past, they use a hash table
* Also provide in the github repo a faster implementation of Go that doesn't involve copying as many pythong variables
* Also sets up a script so you can play against the bot


## Chapter 4: Playing games with tree search
* Tree search: pruning and Monte Carlo Tree Search
* Games can be
    - Deterministic vs nondeterministic: chess vs backgammon
    - Hidden information vs perfect information: Poker vs Backgammon

* Most of the code is game agnostic but a new game would need to implement game logic of ```Player, Move, GameState: apply_move, legal_moves, is_over and winner``` - github repo has an example for this from Tic Tac Toe
* Other games that would work well are: Mancala, Gomoku, Nine Mens Morris, Hex, CHeckers, Chess
* Minmax, writes a FULL MINMAXAGENT IMPLEMENTATION
    - Write the function to find the winning move
    - elmininate all losing moves
    - Iterate over multiple moves in advance
* Minmax is unbeatable for games like Tic Tac Toe but own't work well for trees with large height or depth. Tree size is ```width^depth```
* Reduce tree size via position evaluation with heuristics
    - Chess: difference between total value of pieces of white - total value of pieces for black
    - etcc..
* With position evaluation we can prune the depth of search 
* Alpha beta pruning: if opponent has one really good response move you don't need to compute the rest of the tree
* Idea of MTCS: given some position, simulate a bunch of different random moves - if one side wins way more often than the other, it means that one of the sides had a better initial position
* MCTS needs to balance exploration vs exploitation using the UCT formula which is a weighted sum of the likelihood of winning at a certain node + how little visited the other nodes are
* Faster game engine means you can evaluate more moves in advance
* Can optimize how to choose MCTS rollouts based on some domain knowledge from the game
* Can use MCTS to make the bot resign once it realizes that it has less than 10% chance of winning

## Chapter 5: getting started with neural network
* Design a neural network library from scratch where you can stack layers (Keras style) - using handdigit recognition as a use case

## Chapter 6: Designing a neural network for Go data
* Take Go board and featurize it as -1 for black pieces and +1 for white pieces and 0 otherwsise then flatten the board into a single column vector (later chapters will look at using a convnet to exploit spatial locality)
* So we need to create an encoder class to  turn a board game state into numeric data and way to encode and ecode specific point
* Generate data using MTCS and have a CLI interface to make it easy to specify board size nad number of games to generate - ```parser.add_argument()``` is extremely useful and I should use it more often
* Gives an overview of Keras, how it has multiple backends. How to install it using ```pip``` although ```pyenv``` is not covered and probably should be. Also no platform specific instructions, book is assuming everyone has Mac OS X and goes over an example of Image processing using Keras
* For Go, model needs to take in an array of size the game board and output an array of size the game board where each element will have the predicted move probability
* First network has 3 layers with roughly 600K weights, accuracy of predicting best move is 2.3% which is twice as good as randomly guessing which is 1.2%. Improvements can come from several areas
    - MCTS isn't generating all that great of moves so games arent that good
    - Neural net architecture can capture spatial data like in donvnets
    - Using sigmoid activation
    - MSE isn't the best function for classification
* Explains what a convolution operation is
* Explains what a tensor is and where the name tensorflow comes from
* Mentions the flatten operation that needs to be added between dense layers and conv2d layers in Keras
* Introduces pooling
* Uses softmax function as an activation function - Keras makes it really easy to plug in a custom activation function
* Uses categorical cross entropy instead of MSE as a loss function
* Uses Dropout and ReLu
* With all the above improvements our accuracy goes up to 8%

## Chapter 7: Learning from data a deep learning bot
* Now use actual data from Go games instead of randomly simulating them
