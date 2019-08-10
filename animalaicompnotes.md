https://www.mdcrosby.com/blog/animalaieval.html
https://github.com/beyretb/AnimalAI-Olympics


Part of making this contest interesting is creating your own tasks since test tasks are unknown but has lots of stuff it could be tested on at evaluation time.

# Testing info
Main commonalities are understanding walls, ramps and tunnels (does ramps require a 3d understanding for this to work or are pixels enough?)
Movable objects like cardboard boxes which vary in weight and shape so the behavior in which they will turn - can we encode an understanding of object shape and how its supposed to move?
Rewards are in the shape of food or zones that give negative or positive reward

### Categories of tasks
1. Food: DQN should work - or dueling DQN, whatever vizbook dudes used
2. Preferences: Measure difficulty of obtaining vs reward
3. Obstacle navigation: create a world physics model or bootstrap via one seperately trained on Unity physics engine?
4. Avoidance: DQN should work
5. Spatial reasoning: CNN to an object encoding ? Physics engine? RNN for memory to remember sequence of actions?
6. Generalization: coloring
7. Internal models: blackout but still need to make actions. World model seems like the only thing that would work here. Store a snapshot of the game world and then try to remisumate it when there are no events happenning. Baseline to beat is not moving during blackout
8. Object permanance: what is the state of the art for encoding RNN with memory?
9. Advanced preferences: planning?
10. Causal reasoning: yeah IDK