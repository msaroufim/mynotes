SFT memorizes and RL generalizes https://www.alphaxiv.org/abs/2501.17161
* Catchy title but reality is closer to failure mode of SFT is memorization and failure mode of RL is reward hacking
* Regardless an SFT is often needed as a prereq otherwise the models don’t converge at all and don’t have the ability of following new instructions

Deep delta learning https://www.alphaxiv.org/abs/2601.00417 
* Similar to regular rnn formulation but updating state has a learnable function that isn’t just additive so can do nothing, update or delete old memories. That’s why it’s called delta rule which is neuroscience inspired
* Transformers without normalization, just use a simple tanh trick https://www.alphaxiv.org/abs/2503.10622 - seems lovely, exactly the kind of thing id like to have in a simple repo


Read next
* On the interplay of pretraining, midtraining, RL on reasoning models https://www.alphaxiv.org/abs/2512.07783: RL yields gains when task difficulty slightly exceeds pre training but if task is too hard then nothing happens. In mid training there needs to be some sparse examples of the task we'll post train on, 0 exposure is bad
* Beyond the 80-20 rule high entropy tokens https://www.alphaxiv.org/abs/2506.01939: the core trick in this paper is that when doing RL, we are only influencing entropy of a few high entropy tokens so what we do is we first calculate entropy over the entire Vocab by running softmaxa and then getting shannon entropy. Once we do that we apply a mask to keep the top 20% highest entropy tokens so we only do PPO loss over the unmasked tokens. TODO: read about DAPO
* SWE-RL: Advancing LLM reasoning via RL: https://www.alphaxiv.org/abs/2502.18449: basically the "trick" is they have a dataset of code edits and then a model is meant to  emulate the full trajectory of that edits and a reward at each step is a similarity score to the human baseline. This should work well for kernelbot data
* DAPO: An OSS RL system at scale: https://www.alphaxiv.org/abs/2503.14476
* Does RL really incentivize reasoning beyond the base model https://www.alphaxiv.org/abs/2504.13837 : cool paper its a simple ablation that shows you get better success doing a large pass @ k on a base model relative to using a reasoning model. so reasoning model just biases solutions better at small k values but that's otherwise it
* Reasoaning with exploration https://www.alphaxiv.org/abs/2506.14758?chatId=019b9c22-0657-7a08-83be-3056e78c0e55 : high entropy tokens are rewarded for exploration not just random ones. You need to get the entropy over all tokens but its not slow because its just a simple pointwise op you can fuse, (Cool! I wonder which reward functions need to be written vs are e asy to compile)
Not super RL related but really enjoyed  reading this https://x.com/marksaroufim/status/2009121076153094611?s=20 on how if you zoom in enough on a curve you can almost fit a power law

Maybe we don't need "new tricks" maybe most innovation in the world is about using innovations from related problems or fields https://x.com/marksaroufim/status/2009096176789016600?s=20 wisdom from Ion

TODO: 
* Write myself a simple DPO, PPO and GRPO programs