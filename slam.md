# SLAM basics

## SLAM part 1 by Whyte and Bailey

Simulataneous Localization and Mapping (SLAM) is a process by which a mobile robot can build a map of its environment and figure out where it is in that environment. This process is entirely online meaning we don't need to encode any prior information about landmarks or the environment for it to converge.

In what follows we'll cover the standard SLAM algorithm and how it works and we'll conclude with some more advanced tricks that will allow us to scale SLAM to the real world.

Keep in mind that there are tons of different SLAM algorithms and it's possible to write an entire book on this topic alone. In fact there are many such books that I'll recommend in the references section.

## Problem definition

Suppose our robot is moving around an environment with \\(n \\) static landmarks and is taking in some sensor data from times \\(t = 0, 1, \mathellipsis  T \\).

Any 3D object can be defined via a transform which is a combination of position and orientation. 

We'll use \\(x_t \\) to denote the transform of our mobile robot at time \\(t \\)

\\(z_{it} \\) will denote the observed location of the \\(i \\)'th landmark at time \\(t \\) and \\(m_i \\) will represent the true position of the \\(i \\)'th landmark.

We'll use a capitalization convention to refer to histories. E.g: \\(X = x_1, x_2, \mathellipsis T \\)

The SLAM problem is about computing the probability distribution (\\ P \\) at each timestep \\(t \\) where \\(P \\) is defined as

\\(P(x_t, m | Z_{0:t}, U_{0:t}, x_0) \\)

\\(x_t \\) is the localization problem and \\(m \\) is the mapping problem

The idea is that we want to compute \\(P(x_t) \\) in a recursive manner via \\(P(x_{t-1}) \\) 

ADD FULL FORMULA HERE

SLAM converges because even though we have a lot of uncertainty about absolute positions of landmarks and the mobile robot, our relative estimates improve monotonically with additional measurements as the individual measurements at every iteration \\(t \\) are independent of each other.

The SLAM problem as described is not tractable because it involves an extremely expensive integration. One of the many possible solutions is the Extended Kalman Filter (EKF) where the main insight is to model some gaussian noise to our models.


## More advanced tricks in part 2 by Whyte and Bailey
 * Partitioned updates
 * State augmentation
 * Sparsification
 * Global vs relative submaps


# Libraries
* https://github.com/JuliaRobotics/Caesar.jl - do a usage example


# References
* Thrun book
* SLAM by Whyte and Bailey