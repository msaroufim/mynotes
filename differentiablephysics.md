# Differentiable physics

## Differentiable Physics and Stable Modes for - Tool-Use and Manipulation Planning
* http://www.roboticsproceedings.org/rss14/p44.pdf
* Humans have a built in physics engine in their brain that can let them simulate the outcome of an action or tool manipulation
* Differentiable physics engine means we can have an efficiently invertible physics engine which means we can start from the world that we want and get the state and aciton that we'd need to get there from a previous state. However fully differentiating physics engine is complicated so can model it with a smaller net
* Model actions as discrete combination of tasks as opposed to just forces on joints
* Kinda meh paper

## End to end differentiable physics for learning and control
* https://papers.nips.cc/paper/7948-end-to-end-differentiable-physics-for-learning-and-control.pdf
* Simulates rigid body dynamics via a linear complementary problem. LCP is about building a constraint matrix subject to contact constraints and solving it using interior point methods
* Learn bothy physical constants of the world and of the task
* They derive the derivatives of LCP and call the resulting engine differentiable
* Benchmaks are evaluated on cartpole. I'd expect a more interesting experiment

## The OG paper
* https://arxiv.org/pdf/1611.01652.pdf
* Write a physics engine in Pytorch to make it differentiable. Only supported balls as objects


## Differentiable game theory?
* https://www.ijcai.org/proceedings/2018/0055.pdf