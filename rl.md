SFT memorizes and RL generalizes https://www.alphaxiv.org/abs/2501.17161
* Catchy title but reality is closer to failure mode of SFT is memorization and failure mode of RL is reward hacking
* Regardless an SFT is often needed as a prereq otherwise the models don’t converge at all and don’t have the ability of following new instructions

Deep delta learning https://www.alphaxiv.org/abs/2601.00417 
* Similar to regular rnn formulation but updating state has a learnable function that isn’t just additive so can do nothing, update or delete old memories. That’s why it’s called delta rule which is neuroscience inspired
* Transformers without normalization, just use a simple tanh trick https://www.alphaxiv.org/abs/2503.10622 - seems lovely, exactly the kind of thing id like to have in a simple repo


Read next
* On the interplay of pretraining, midtraining, RL on reasoning models https://www.alphaxiv.org/abs/2512.07783
* Beyond the 80-20 rule high entropy tokens https://www.alphaxiv.org/abs/2506.01939
* SWE-RL: Advancing LLM reasoning via RL: https://www.alphaxiv.org/abs/2502.18449
* DAPO: An OSS RL system at scale: https://www.alphaxiv.org/abs/2503.14476
* Does RL really incentivize reasoning beyond the base model https://www.alphaxiv.org/abs/2504.13837