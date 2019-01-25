# Building a race car AI
In this chapter we'll be looking at building an agent in a racing game. The primary application we'll be looking at is building a superhuman AI to drive around the racetrack you'd be defining. The ideas in this chapter extend beyond video games and you'll be learning the foundations of self driving cars in this manner. Self driving cars contains many subproblems including sensor networks, electronics, SLAM algorithms and finally navigation algorithms. Everything you'll learn here will mostly be relevant for navigation algorithms that have as input some RGB camera and need to decide for example whether to move left, right, speed up or break.

If you end up finding the contents of this chapter inspiring, I'd highly recommend you try to build your own RC car using a 3D printer, an arduino microntroller and some small servo motors.

We will use a technique called Deep Deterministic Policy Gradients which work well for continuous spaces.
1. Critic model: continuous Q-learning (SARSA)
2. Actor model: policy gradient $$c^2$$

## How to put things together

### Network architecture

We'll have a policy network that takes in the state of the game either as raw pixels or as a data structure including things such as the velocity of the car.

$$\pi_\theta = P[a|s, \theta]$$

Policies can be deterministic or stochastic. A stochastic policy is often preferrable in strategic environments since they're less exploitable by an opponent.

The actor critic architecture is well explained in Sutton and Barto.

A sample implementation for a racing game would look like the below

```python
    def create_actor_network(self, state_size,action_dim):
        #Try and figure out what are good param sizes for this
        #Is most likely dependent on size
        HIDDEN1_UNITS = 300
        HIDEEN2_UNITS = 600

        print("Now we build the model")
        S = Input(shape=[state_size])  
        h0 = Dense(HIDDEN1_UNITS, activation='relu')(S)
        h1 = Dense(HIDDEN2_UNITS, activation='relu')(h0)

        #Steering ranges from [-1,1] because of tanh where -1 means full left and +1 means full right
        Steering = Dense(1,activation='tanh',init=lambda shape, name: normal(shape, scale=1e-4, name=name))(h1)   

        #Acceleration and breaking range from [0,1] - no break or acceleration to full break or acceleration
        Acceleration = Dense(1,activation='sigmoid',init=lambda shape, name: normal(shape, scale=1e-4, name=name))(h1)   
        Brake = Dense(1,activation='sigmoid',init=lambda shape, name: normal(shape, scale=1e-4, name=name))(h1)  

        #Merge is a great helper function to ask our model to ouput those 3 things 
        V = merge([Steering,Acceleration,Brake],mode='concat')  

        #Return a model object        
        model = Model(input=S,output=V)
        print("We finished building the model")
        return model, model.trainable_weights, S
```

And the critic network

```python
    def create_critic_network(self, state_size,action_dim):
        print("Now we build the model")
        S = Input(shape=[state_size])
        A = Input(shape=[action_dim],name='action2')    
        w1 = Dense(HIDDEN1_UNITS, activation='relu')(S)
        h1 = Dense(HIDDEN2_UNITS, activation='linear')(w1)

        a1 = Dense(HIDDEN2_UNITS, activation='linear')(A)
        
        #Look at the different merging mechanisms, this function sounds nuts
        h2 = merge([h1,a1],mode='sum')    

        h3 = Dense(HIDDEN2_UNITS, activation='relu')(h2)
        V = Dense(action_dim,activation='linear')(h3)  
        
        #Training
        model = Model(input=[S,A],output=V)
        adam = Adam(lr=self.LEARNING_RATE)
        model.compile(loss='mse', optimizer=adam)
        print("We finished building the model")
        return model, A, S 

```
Would be very useful to run this a few times and see what kinds of results I get out of it


Below makes sure to slowly change the values of the actor weights to improve the stability of the entire algorithm. GANs use similar tricks
```python
    def target_train(self):
        actor_weights = self.model.get_weights()
        actor_target_weights = self.target_model.get_weights()
        for i in xrange(len(actor_weights)):
            actor_target_weights[i] = self.TAU * actor_weights[i] + (1 - self.TAU)* actor_target_weights[i]
        self.target_model.set_weights(actor_target_weights)
```

### Inputs
As we mentioned previously, it's possible to learn directly from pixel values on the screen but that approach is mostly useful if you're treating a game as a blackbox. Thankfully your own games are not a blackbox since you have full access to your source code. In the most general case you would just input the entire game state as input and let DDPG handle the rest but there's value in cleaning up the input just a bit to only keep the values that would be relevant for the model. Some useful values would include

* Angle between the car direction and the direction of the car axis
* Car speed in both the x and y directions
* The vehicle RPM
* Wheel spin velocity
* Data about the track which can be encoded in a variety of ways. One way would be the distance between the car and track end at 20 different points in front of the car

Inputs need to be normalized, we don't want to bias our model to believe that larger values are more important than smaller ones.

### Main function
We finally put everything together in the below loop which many reinforcement learning algorithms share and a pattern you'll see many times over in this document.

```python
for j in range(max_steps):
    a_t = actor.model.predict(s_t.reshape(1, s_t.shape[0]))
    ob, r_t, done, info = env.step(a_t[0])
```

## How to engineer the car do drive smoothly
We can be creative with the reward function. A first try may look something like

```python
reward_t - V_x * cos(\theta)
```
The issue with that first try is that agent will prioritize going forward very fast. One could argue that given sufficient training time, the agent would learn that braking on turns is within its best interest if it wants to go faster overall.

We can directly encode our intuitions about braking in the below variation.

```python
reward_t - V_x * cos(\theta) - V_x * sin(\theta) - V_x | trackPos|
```

Exploration policy used is Ornstein-Unhlenbeck (look at a better explanation online)

## Reference
* Sutton and Barto
* https://yanpanlau.github.io/2016/10/11/Torcs-Keras.html
* https://arxiv.org/pdf/1509.02971.pdf (original paper on continuous control using deep reinforcement learning)