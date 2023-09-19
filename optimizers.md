# Optimizers

In general this is a tricky field since most results don't reproduce, probably less than 1% because very sensitive to hyperparams. A lot of papers on lack of reproducibility particularly apply here

## Adam
https://arxiv.org/pdf/1412.6980.pdf

Ergo adam which has fairly standard hyperparams which don't really change
* https://github.com/pytorch/pytorch/blob/main/torch/optim/adam.py
* https://github.com/torch/optim/blob/master/adam.lua

The intuition behind close to 1 beta_1 and beta_2 is that the past will matter more, then there's an \epsilon to remove 0 values from the formula, debiasing (see trick below), a learning rate (standard stuff)

The main problem with ADAM is it 3x's your model size. Other techniques like adafactor are similar but don't have 2 extra paramters per gradient but instead have a single value for an entire row an another for a column so it's O(m+n) instead of O(2m^2)

It's a first order technique in that it only depends on the average of past gradients and specifically their first moment (mean) and second moment (variance)

The formula has a couple of tricks but the notable ones are
* Values are init'd close to 0 so they debias them away from 0 by doing value / (1 - \beta) where beta is is close to 1
* Most gradient updates will be sparse for NLP specifically the input is sparse because of one hot encoding
* The moving average is a form of simulated annealing because the learning rate effectively changes

![image](https://github.com/msaroufim/mynotes/assets/3282513/c176ca2b-1f28-4f3a-8ef3-65317a718c1e)

alpha will be small for sparse updates so need a high SNR to move  

![image](https://github.com/msaroufim/mynotes/assets/3282513/e53c0d81-fd76-4424-91a2-ed696f160a18)

ADAM's steps are also more conservative than SGD so it seems like risk of divergence is lower but it might be slower, you can analyze this by analyzing the curvature of a space and seeing how ADAM behaves by using the Fischer
information matrix


## Adam in PyTorch

https://pytorch.org/docs/stable/optim.html

Optimizers in PyTorch have 3 implementations
1. The for loop one
2. Foreach which is a form of horizontal fusion because you fuse optimzizer steps across parameters
3. Fused which would fuse the update so its a form of vertical fusion

I believe torch.compile makes 3 not useful anymore, 1 makes sense and I'm still getting confused as to what 2 is relative to something like vmap


```python

# for loop
for w in parameters:
    gradient = compute_gradient(w)
    w -= learning_rate * gradient

# for each
gradients = compute_gradients_for_all(parameters)
parameters -= learning_rate * gradients

# fused
parameters = compute_and_update_gradients_for_all(paramters, learning rate)
```

fused is great to reduce memory bandwidth, foreach seems faster but increases the risk of OOMs, there are probably sharded versions of foreach we could use
```

RMSprop and adagrad both don't have bias correction so the steps can often be too big and they will diverge

The method combines the advantages of the ability of AdaGrad to deal with sparse gradients and the ability of RMSProp to deal with non-stationary objectives.
* Adagrad will more aggresively update weights that get updated less frequently
* RMSProp uses a decaying lookback window which makes it deal well with non stationary objectives
