Pure sampling/selection: Taking many model outputs, scoring them, keeping the best ones. This is more like evolutionary selection or rejection sampling - no weight updates, just filtering.
Supervised fine-tuning on selected samples: Train on the good samples you found. This is distillation disguised as "RL."
Policy gradient methods: Actually update model weights based on reward signals (like PPO, REINFORCE). This is "true" RL.
