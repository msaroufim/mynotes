ICML 2018: Tutorial Session Optimization perspectives on learning to control
https://www.youtube.com/watch?v=hYw_qhLUE0o&t=756s

* EE people: RL is a subset of control theory - mostly deal with continuous domains
* CS people: Control theory is a subset of RL - mostly deal with discrete domains

RL: data -> action
Control theory: model -> action

RL also has a better PR department since gets published in science magazine vs control theory gets published in IEEE

Main question
* How well must we understand a system to control it
* 

Control theory is the study of dynamical systems with inputs. RL is the same but discrete. Functions vs tables
Control minimize cost. RL maximize reward

Linear quadratic regulator
* Quadratic cost
* Linear system

Optimal control can be solved using
* batch optimization (even if the underlying problem is not convex)
* IPOPT (optimization solvers) 
* Dynamic programming

How do you do control when the system is unknown?

Data center cooling can be solved using (bad PR example)
* PDE control: identify everything
* Coarse model: model predictive control
* Reinforcement learning: don't build a model at all (similar to PID control)

95% of robots in industry use PID control. Example: self driving car want to stay in lane
1. Take error which is distance from the center of the lane
2. Take error, its derivative and its integral
3. Need to find parameter weights for each of the above 3 things. In practice people don't even use the derivative since its hard to tune



Learning to control
* Generate N trajectories of length N
* Build a controller with smallest error with fixed sampling budget

## Different approaches to RL

Written tutorial by the speaker https://arxiv.org/abs/1806.09460

Model based RL - this is most of what people in control did historically. They call it system identification and then control
* Collect simulation data to find x_t+1 from x_t and u_t + noise
* Fit dynamics using supervised learning
* Solve the approximated problem and hope the new problem isn't too far

Approximate dynamic programming
