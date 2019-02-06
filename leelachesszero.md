# Leela Chess Zero

Open source engine that provides libraries and utilities to run Alpha Go and Alpha Go zero style training for chess.

Noone seems to have been able to replicate the Alpha Zero results for chess but supervised training seems to have been replicated.

Leela zero uses a Chess client written in Go (slightly modified to better suit RL purposes) and implements MCTS in C++ to be able to speed up computations and have scalable performance on distributed machines since single machine was not enough for self play.



There's also a library that does Alpha Go like training for the game Reversi https://github.com/mokemokechicken/reversi-alpha-zero


Project structure of https://github.com/Zeta36/chess-alpha-zero
* binder which includes all the libraries in yaml format
* data/model which includes the model weights and model specifications
* demo notebook which renders the the chess board and takes the best move from the current best model
* source
    - run.py: uses multiprocessing to run 10,c000 instances
    - env: contains the implementation of a chess environment and the the code that turns the board into a plane to make it easier to consume for DNNs
    - lib has a bunch of miscellaneous stuff
    - manager.py is a CLI to do training
    - Interesting code is in the worker folder
* worker folder - TODO: SUMMARIZE SELF PLAY, OPTIMIZE, SL, EVALUATE