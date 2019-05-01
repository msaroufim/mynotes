# Alpha Chess in Python
https://github.com/AppliedDataSciencePartners/DeepReinforcementLearning

Main components
1. Make two bots of different versions play against each other
2. Logger that logs a sequence of actions and their score (Logging is actually the most interesting part of this codebase)
3. Uses graphviz and pydot to output a graph of the neural network architectures
4. Model is a CNN followed by batch normalizatino followed by Relu and then out dense output. Model has value and policy network that are the same but for some reason value head has 2 layers while policy has 1
5. Has a seperate memory implementation with long and short term memory of the same size. Logs the board state, id, chosen action, action value and player turn
6. Many global variables are pulled out from a central global config file which is python code (no seperate configuration language). This includes the neural net architecture. Config has ints, floats and dictionaries
6. Game interface which
    * Inits the game
    * Reset, step, identities? (not sure what is meant by identities)
    * Enumerates the allowed actions
    * Checks if game has ended
    * Get the current value of a state
    * Render the board as a text file
7. Implementation of the Connect4 game
8. Agent 
    * Simulates  MCTS by moving to a leaf, logging it, evaluating the leaf and then backfilling the value (I think this is something the MCTS tree should do automatically instead)
    * performs an action with some selection strategy (act takes as input a function that gets the best state by doing MCTS simulations then applies the action to the world and triggers logging code around which action was taken)
    * Agent also converts the state to somethign that the model file can actually consume
    * Replay which retrains the model from memories with training targets as its past q value 
9. It's useful to have a logger for the runs so you can reinspect all the values. Logger also has a central config that disables or enables it at different points
10. Loss function in its own seperate file for some reason (this should be part of the config as well)
11. Monte Carlo Tree SEarch implementation
    * Node data structure which keeps track of neighbors, if it's leaf, player turn and board state
    * Edge doesn't make much sense (NWQP?)
    * Most code is in move to leave
        * Q and U values determine 
    * Add Node is 1 line of code
    * Backfill go back up the tree and update values


# Alpha Go Julia
https://github.com/tejank10/AlphaGo.jl

Main components
1. Readme allows training by adjusting number of layers and num_games to train
2. Allows play takes in an environment, the model net, num_readouts of MCTS and player turn
3. Replay batch manager
4. UX rendering take in as a config  of a bunch of css files for play vs player only
5. Has board featurizations with the pre Alpha Go Zero techniques where number of liberties among others 
6. Has bindings for a Go engine called GTG
7. Has bindings for kgs coordinates
8. Interface for Web IO
9. A resnet stack implementation
10. MCTS
    * Board repreesnted as a n x N^2 tensor of value estimates. n is number of turns, N is size of the board
    * Longest code
11. MCTS player that loads a MC tree and can pick moves and manages updates to the Monte Carlo Tree Search
11. Main loads all the net params and if they don't exist train MCTS player
