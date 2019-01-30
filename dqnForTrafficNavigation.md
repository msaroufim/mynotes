# DQN for traffic navigation

https://towardsdatascience.com/deeptraffic-dqn-tuning-for-traffic-navigation-75-01-mph-solution-23087e2411cf

Competition can be found [here](https://selfdrivingcars.mit.edu/deeptraffic/). You're expected to write the code directly in the browser which is pretty nice to get started.

Can customize the input with how far to the side, back and forward our car sees. You can imagine this as an abstraction of some cameras that would be on a real car

```javascript
lanesSide = 2;
patchesAhead = 17;
patchesBehind = 5
```

We can also take a look at the actions available to us

```javascript
var noAction = 0;
var accelerateAction = 1;
var deceleratAction = 2;
var goLeftAction = 3;
var goRightAction =4;
```

DQN is already built into the code so we don't need to do anything for this either but we should customize the different hyperparameters to see what works best for us. When you're debugging your own game this is the level of granularity you should be expecting to go down to in case stuff just doesn't seem to work.

![image](dqnhyperparams.png)

Adjusting the different hyperparams is a question of resolving tradeoffs. Is training time an issue for you? Or is the actual performance of the racing car the key for you?

In general having a larger input is better, it corresponds in real life to having higher quality sensors which can only improve the performance of a driving agent. Similarly, increasing the network size and training time can result in a higher quality network.

## Note

Author of the original blog post didn't much more than add some comments on top of the code that already exists on MIT website but he also has a bunch of interesting tutorials to use DRL on a variety of board games. It seems like towards data science requires a monthly subscription for me to continue reading