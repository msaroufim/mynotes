# Karpathy talk notes
https://www.youtube.com/watch?v=IHH47nZ7FZU&feature=youtu.be

Scene recognition in computer division is actually many different tasks: sign detector, sign parser, moving object detector, speed predictor.

## Architecture
So there is a tradeoff between how much of a shared layer do you wanna have between these tasks and how often do you want to have them be independent.

Independent is good because each person can iterate on a model without regressing others. However, there is no cross learning between tasks, inference is slow which is relevant in real time applications like graphics or self driving cars.

Shared is good because inference is fast but tasks fight for limited capacity of weights in the network. Some tasks cooperate and help each other and others hurt each other. This interaction is often non intuitive and complex. Much harder to debug.

There are also hybrid approaches where you also need to consider the order in which you train them



## Loss function

Having a loss function that weights each task can only be solved by grid search if you have two tasks but if you have a 100 you need a different approach.

Some tasks have different scales, are more important than each other, some are easier, some have more data and some have more noise.

Within tasks you may need to oversample because yellow lights are rare for e.g.

Data is sparse and you need to oversample accross tasks and within a task as well. Assumption is you'll slowly fill up and improve your dataset, not that you are given a dense array.


## Training
Given a network of various neural networks for tasks, how do you schedule retraining. Especially if you're doing oversampling, you may affect other related tasks without intending it.

How does early stopping work? Plots for various tasks will look very different, some will overfit quickly, some not at all. What do you do? How do you change task weights, regularizations weights, oversampling to account for this

## Team considerations

Who owns which task and how do you iterate on networks when mutliple people are changing dependent networks and changing the data itself.

Oversampling for your task will make your work look better at the expense of the rest of the team. How do you avoid this? 

If you increase the total loss of your task it'll make your perf better at expense of everyone.

It's difficult to reproduce a great model if a chain of fine tunings inadertendtly had a big impact on you.

What should the etiquette be? What are the rules of thumb or organizing ML teams given how complex task interactions can look like.

# Appendix
Another great talk https://www.youtube.com/watch?v=oBklltKXtDE