RTS and SC2: https://www.youtube.com/watch?v=v3LJ6VvpfgI&list=PLQVvvaa0QuDcT3tPehHdisGMc8TInNqdq


## Python-sc2
* Be on Windows, we haven't tested the below on Linux but it could probably work. Submit a PR and I'll take a look
* Download SC2 from Battle.net
* Download [python-sc2](https://github.com/Dentosal/python-sc2) which is different from pysc2 which is directly supported by DeepMind
* Download [map pack](https://github.com/Blizzard/s2client-proto#downloads) and add it to the following directory C:\Program Files (x86)\StarCraft II\Maps\Ladder2017Season1

Text based version of the tutorial can be found here https://pythonprogramming.net/starcraft-ii-ai-python-sc2-tutorial/

Above is a good tutorial if you want to write your own custom bots but you'll notice that you're writing a whole bunch of code that requires you to have good domain knowledge of how the game works which even if you're the game developer will be extremely challenging in the beginning

## Pysc2

Pysc2 shows two things when you run their hello world example

```
$ python -m pysc2.bin.agent --map Simple64 --agent2 pysc2.agents.random_agent.RandomAgent
```

1. The game being played similarly to how this is done in Python-sc2
2. A feature map (need to elaborate how this works)


## How to use Open AI baselines to train RL for SC2

1. Follow instructions in this tutorial https://github.com/chris-chris/pysc2-examples
2. Git clone the repo
3. Train
4. Test

Training seems to work but can't figure out how to watch a replay