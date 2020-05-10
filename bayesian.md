# Deep Bayesian Learning

## The Case for Bayesian Deep Learning
https://arxiv.org/pdf/2001.10995.pdf

3 main topics
* Marginilization
* Prior
* Bayes rule

* Bayes rule is already used quite a bit- to switch from a generate to discriminative model.
* Prior is to encode some constraint about your data mathematically. Measurements from sensor data then a reasonable prior for that model is gaussian because you expect the sensor measurement somewhat noisy
* But paper claims main distinction is marginilization

Your neural network architecture represents a prior over your model even though the specific parameters of the model need to be learnt
Ensemble methods where you for example aggregate the output of several neural networks to make a prediction can be viewed as Bayesian
Bayesian models help when the same model can express various different problems. Large feedforward fully connected neural network

marginilization is doing an average over all possible hypotheses

2 kinds of noise
1. Epistic: which weights of the model are correct
2. Aleotoric: noise from data

Model space ```[w_1 ... w_n]```, find optimal weights but in the case of bayesian deep learning you're asking yourself what is the distribution of the optimal weights. Instead of predicting a single high dimensional point, you're predicting a distribution over these points. 

Question: Why is this better?
Answer: your testing accuracy will be better this way. Because the model is basically bigger (is there a deeper reason?)

If we look at model space, where are the basins of attraction to our data. This language is very close to what I see in ODE (Ordinary Differential equations)

There's two ways of viewing model space
1. Neural network architecture (but this is what Bayesians refer to as the model space)
2. Specific weight of the network

What is a good prior? What is a reasonable prior? Where have priors in general been succesful at modeling anything except sensor measurements.

Main issues to resolve for basyesian deep learning
1. performance bottleneck for Bayesian deep learning is can you implement integration over various models very quickly. 
2. Model accuracy (science) is it really better on benchmarks that people care about

How do you make Bayesian deep Learning scale. The model space informs the kinds of accuracies that you can expect and so there's a sort of continuous geometric space you can explore to better come up with models and weights but AFAIK this is an open problem.

From a business standpoint, AUTO ML is one the main goals of Bayesian Deep Learning. There are non bayesian approaches (like evolutionary algorithms, tree search algos, grid search over models) for auto ML but bayesian seems like the most natural fit

Conclusion paper says that Bayesian Deep Learning would be useful with more work but definitely not stop what you're doing write now to deploy bayesian models

## Probabilistic ML and AI
https://www.repository.cam.ac.uk/bitstream/handle/1810/248538/Ghahramani%202015%20Nature.pdf

Main advances
1. probabilistic programming
2. Bayesian optimisation
3. data compression
4. automatic model discovery.
5. Hierarchichal learninig

Main criticism of Deep Learning is they don't model the uncertainty in a prediction. Philosophically is it really possible to model uncertainty.

Many intro to ML classes prior to Deep Learning teachers introduce graphical models because any probability distribution can be modeled as a graph. It's easy to compose graphs to solve more complex problems.

When humans make decisions we model uncertainty somewhat in our brains and so we expect our systems to do the same. Doesn't the Reinforcement Learning framework take care of this already?

Solutions to deal with this
1. MCMC
2. Variational methods
3. Expecation propagation
4. Sequential Monte Carlo

How to generalize from data
1. Have lots of parameters for generalization
2. Non parametric components

## Probabilistic programming
1. Model your problem as a sort of video game. That's why I love Unity for simulations. Your simulation will generate data pairs on which you can train on
2. There are interesting links between Bayesian optimisation and reinforcement learning (RL). Specifically, Bayesian optimisation is a sequential decision problem where the decisions (choices of x to
evaluate) do not affect the state of the system (i.e., the actual function f). Such state-less sequential decision problems fall under the rubric of multi-arm bandits [72], a subclass of RL problems.
More broadly, important recent work takes a Bayesian approach to learning to control uncertain
systems [73] (and see the review [74]). Faithfully representing uncertainty about the future outcome
of actions is particularly important in decision and control problems. Good decisions rely on good
representations of the probability of different outcomes and their relative payoffs
3. Learning an optimal model for data is similar to compression because you can just use your model to generate your data.
4. Model the uncertainty in your prediction
5. Automatic Statistician: Replace data scientists with bayesian laerning. Are any of the prototypes here useful? My gut feel is no

# References
* Bayesian REinforcement Learning Survey https://arxiv.org/pdf/1609.04436.pdf - long but good