# Finding friend and foe in multiagent games

* https://arxiv.org/pdf/1906.02330.pdf
* Finding friend and foe in multi agent games

Current state of the art on various games
* Real time strategy (Dota and SC 2): Proximal Policy Iteration with custom code to encode the state
* Alpha Go Zero: Self play with MCTS + DNN for node evaluation (state encoding removed for Zero)
* General robots: TBD
* 1v1 Poker DeepStack: Conferfactual regret minimization

Dota has no ambiguity around who to cooperate with
Starcraft all units controlled by the same player


What's interesting about multiagent games with cooperation is that you don't know really know what the internal state of your enemies and teammates is.

Main technique is counterfactual regret minimization with deep value networks trained through self play

Gives interpretable representation of win probabilities

Game tested on Avalon board game