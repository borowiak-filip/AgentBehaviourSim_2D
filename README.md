# 2D Square Grid Simulator

The intent of this project is to enable testing the behaviour of different types of agents in simple grid environment.
The run.py file is the main simulator setup where you can specify how many objects (rewards, obstacles, anti-rewards etc) the game will have. 

The Hero class in game_objects/ is an example of simple stochastic agent that has a random movement. The Hero's update function is invoked everytime the game is render to perform an action.
The run.py has a while loop that determies what should happened at each time step. By default the simulator allows to either use keyboard when hero's 'stochastic' = False or stochastic behaviour with 'stochastic' = True.

Simulator implements simple reward function (extras/RewardGenerator.py) that generates locations and values based on Manhattan distance to the end goal.

Environment's objects positions are stored in extras/EnvironmentSetup.py.

Simulator comes with simple assets 32x32 for each object.

## License

### Code
The code in this project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Assets
The assets (images) are licensed under the ASSETS LICENSE:
- No Redistribution
- No Commercial Use
- Attribution Required

See the [LICENSE](LICENSE) file for more details.