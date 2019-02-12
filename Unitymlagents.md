# Unity ML agents tutorial

* Trainer param tutorial: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-ML-Agents.md
* Some tasks require memory to solve well, use RNN: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Feature-Memory.md
* Can setup a curriculum to make training easier if our tasks don't seem to be converging https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-Curriculum-Learning.md
* Can do imitation learning and show a video of an agent playing a game: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-Imitation-Learning.md
* Example environments: https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md

GPU training needs a small config change: https://github.com/Unity-Technologies/ml-agents/issues/1534

To train an agent from scratch, setup the Unity and use the CLI https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-ML-Agents.md - CLI needs a path to a config file to specify how the learning will happen exactly and needs a .app file which you can get from building the scene you're working with.

 Base algorithm is PPO with some default params but they can be changed easily


Let's look at an example with the Soccer game. Code has 4 files
* AgentSoccer: each agent has a role and a team, a reference to the soccer academy. AFter the helper functions to join blue team all the functions are part of the interface agents need to follow. There's a couple of interesting stuff here
	- Players are added to area
	- Vector observations are made by projecting rays out of the agents field of vision at various angles and whathever they collide with is added to vector observations
	- Move Agent which discretizes the action space
	- Agent action which adds an existential penalty for both kinds of players
	- Agent Reset which resets positions
	- Agent on done which stays
* SoccerAcademy which just holds references to brains and rewards
* SoccerFieldArea: which keeps track of when to administer rewards and punishments to the players and resets the game when its done
* SoccerBallController: keeps track of the last color that the ball touched and triggers an event when the ball reaches one of the two goals

Let's try modifying the game, retraining and see how everything works



## Pytorch integration
It's possible to train a Pytorch model which has a much simpler API than Tensorflow to able to train a model and also display the loss in the environment. https://github.com/xkiwilabs/DQN-using-PyTorch-and-ML-Agents. The way this works is
* In python use the unity agents library to get a gym like API for your Unity environment
* Create a trainer, tester, replay memory and the model file and everything just works
* You can even display the loss and training using Tensorboard

Unfortunately AFAIK it's not possible to embed the model as a trained brain in Unity ML agents: https://github.com/Unity-Technologies/ml-agents/issues/1300


## How to train for the example apps given in the repo
* Go to the academy and switch on control
* For each of the relevant agent prefabs drag in the learner brain
* go to anaconda prompt and activate the ml agents environemnet
* run mlagents-learn --path to config
* run tensorboard --lod_dir=summaries --host=127.0.0.1 to see the results
* wowza so ez
