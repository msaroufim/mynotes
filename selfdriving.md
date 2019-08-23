# Self driving cars

## Siraj tutorial

https://www.youtube.com/watch?v=EaY5QiZwSP4

Udacity open sourced a sim which is just an exe that has a training and inference mode created in Unity

Model is just a 9 layer CNN

Data generation uses human driver that creates data which is collected by 3 cameras, steering data and throttle value. Machine wants to clone this data which is called behavioral cloning. (plain old supervised learning)

Nvidia has an on board GPU. 

Sheeraz has nice Anaconda scripts to install Open CV and stuff

Supervised learning is easy. All other forms of learning are kind of hard.

Behavioral cloning in the sim recreates a csv files that can be used as a training dataset. https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-Behavioral-Cloning.md

CSV is: 3 sets of images for each timestep, steering angle, speed, throttle and break

Siraj spends most of the video talking about writing the ML model which is like 9 lines of Keras

Uses Client server model. Simulator is a server and we feed it actions from our client which hosts a keras model via Flask and socketio. Need to create your own event handlers on the client (TODO: Need to better understand how this works)

