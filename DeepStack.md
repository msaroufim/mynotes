https://int8.io/counterfactual-regret-minimization-for-poker-ai/#more-2443

# Poker bot
No limit poker has a practically infinite number of actions
Uses counterfactual regret minimization and solves nested subtrees 
Limits tree depth by using a value network
Limits tree breadth by having actions be: call, fold, all in, and 2 different kinds of raises
Videos of the bot playing can be found online https://www.youtube.com/channel/UC4vSx3bbs8dbaHl2tkzU8Nw/videos

Poker is interesting because it has randomness in the draws that show up and there's imperfect information between the players

Utility of given node in the tree is a weighted sum of payoffs lower down in the tree and the probability of reaching those nodes

Nash equilibrium is guaranteed to exist for poker with a finite number of rounds
True state can't be really observed but can be used during self play to train the agent

Suppose we have n experts and each gives us advice on what to do. Regret is the difference between what we end up doing and the best expert
Algorithm learns without regret if over time taking average over experts converges towards best expert
Very similar ideas to the probability and statitics Vovk book, should really check it out again

https://www.youtube.com/watch?v=qndXrHcV1sM

Traditional tree techniques dont work well with Poker for a few reasons
1. History is important because it tells us what our opponents know about our cards
2. We don't have a state since we don't have access to our opponents cards
3. Value of a state depends on what opponents know of each others cards

When exploring the decision tree if some node was reached that the agent didn't expect then bets are smushed back into the closest kind of bet

Full strategy is essentially a giant table create offline that's 160TB big with 4,000 CPUs trained for 2 years with the goal of making exploitability 1mmg (meaning it would take a lifetime for someone to verify that you can't play perfectly)

No limit 10^160 possible states vs 10^12 for limit poker -> so huge difference in complexity (almost like the difference between checkers and Go)

Limit poker is basically solved
No limit poker is much harder so it's easier to beat top players than to solve the game

No limit poker means you decide how much to bet (limit poker means you can just say I bet) and there's several rounds of betting that can happen before cards are shown

At each node we store two vectors one tells me the value of my hand and the other tells me the value for my opponent. Range and counterfactual value. (if my opponenent didnt want a specific branch he wouldnt act in such a way as to end up there) - min 28 in video

Poker players don't release their hand histories out of fear of being exploited

Python implementation of DeepStack https://github.com/cgnicholls/deepstack

Counterfactual reasoning explained intuinetely: https://www.quora.com/What-is-an-intuitive-explanation-of-counterfactual-regret-minimization

Original paper: https://static1.squarespace.com/static/58a75073e6f2e1c1d5b36630/t/58b7a3dce3df28761dd25e54/1488430045412/DeepStack.pdf