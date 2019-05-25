# Visualization libraries for RL

## RL baselines zoo
* https://github.com/araffin/rl-baselines-zoo
* Display action prob over time
* Display state representations
* Visdom integration to show #of timesteps and #of espidoes
* Hyperparam optimization using hyperband and hyperot algorithms. Also use optuna which does
    * grid search
    * Early stopping
    * Try same hyperparms several times to average and be sure
    * uses some bayesian optimization techniques
* Has utilities to record a video of an agent training and then use a slider to see what was happening at different iterations of the algorithm
* Uses pandas dataframe to store logs and pytable writer to turn them into a markdown file
* Has all sorts of trained agents in pkl files, probably better to use Git LFS for something like this
* Hyperparams per environment per algorithm are stored in a YAML file
* Docker files to setup the libraries, looks like regular shell scripts
* Main directory has a train file wihch uses teh stable baselines project

## RL State Representation Learning
* https://github.com/araffin/robotics-rl-srl
* Uses git submodules to pull dependencies

```
  python -m rl_baselines.train --algo rl_algo --env env1 --log-dir logs/ --srl-model raw_pixels --num-timesteps 10000 --no-vis
```

* Can also use srl-model ground truth which would give the x, y locations of a robot instead of training on raw pixels
* Seperate training and testing CLI, can even pipeline different algorithms with different models
* Uses sphynx to build documentation which requires a config file
* Can work with real robots using  ROS interface
* State representation learning can be done in a few ways - either pixel, some positional and rotational encoding and various embeddings, not sure what inverse and forward models are
    - ground_truth: Hand engineered features (e.g., robot position + target position for mobile robot env)
    - raw_pixels: Learning a policy in an end-to-end manner, directly from pixels to actions.
    - supervised: A model trained with Ground Truth states as targets in a supervised setting.
    - autoencoder: an autoencoder from the raw pixels
    - vae: a variational autoencoder from the raw pixels
    - inverse: an inverse dynamics model
    - forward: a forward dynamics model
    - srl_combination: a model combining several losses (e.g. vae + forward + inverse...) for SRL
    - pca: pca applied to the raw pixels
    - robotic_priors: robotic priors model (`Learning State Representations with Robotic Priors <http://www.robotics.tu-berlin.de/fileadmin/fg170/Publikationen_pdf/Jonschkowski-15-AURO.pdf>`_)
    - multi_view_srl: a SRL model using views from multiple cameras as input, with any of the above losses (e.g triplet and others)
    - joints: the arm's joints angles (kuka environments only)
    - joints_position: the arm's x,y,z position and joints angles (kuka environments only)
* Many custom environments written in Python. Could just be a list of all the open AI environments
* Environments need to be registered for some reason
* In main loop for starting inference, if ppo then just do the model predict and if not use an exploration strategy + regular RL loop
* Some utilities to fusion logs
* Also some tools to work with real robots which lets you control an omnibot, robobo bot and baxter bot based on topic mechanism of ros
* URDF robot and dae mesh files are in the repo
* Episode saver logs all the necessary data from training - can further visualize the output of this
* TODO: I don't quite understand what's happening with the state representation server..
 * There is a base class to handle state representations and the kinds of things they can return like their dimension
 * Nice trick with Python tests - can also mark tests as fast or slow
 
 ```python @pytest.mark.parametrize("baseline", ["supervised", "vae", "autoencoder"])
```

## RL baselines
* Has a main interface for RL algorithms that can init the spacees, load, save and train. And then each of the main algorithms a2c, ddpg, ppo, trpo add their own handles
* Moving average is a convolution operation
* Vizdom integration (the FB viz library) is fairly limited. Plot an array is pretty much as fancy as it gets
* Also has evolution strategies (CMA-ES seems to be the fancy one)

## Pytorch RL
* https://github.com/jingweiz/pytorch-rl


