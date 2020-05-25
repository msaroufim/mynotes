# Hugging Face BERT

Plan for today
1. Basics of BERT and transformers Math
2. Look at Hugging Face implementation
3. Bonus goal: Look at Poplar implementation



## References
https://jalammar.github.io/illustrated-transformer/
https://jalammar.github.io/illustrated-bert/
https://amaarora.github.io/2020/02/18/annotatedGPT2.html
http://www.peterbloem.nl/blog/transformers
https://github.com/pbloem/former





# Embeddings summary

Cove
Bidirectional LSTM with attention layer

Word2vec
Encoder Decoder
Continuous bag of words: given context predict word
Skip Gram: given word predict context (harder)

BERT
Attention without RNN. Faster to train
Same as GPT but uses bidirectional encoders
Mask or next sentence prediction as training
Transformer encoder. Uses masking to look at both parts of the sentence. Not autoregressive

Elmo
Bidirectional LSTM

GPT
Same as ELMO but fine tuned on downstream task
Uses attention

GPT-2
Transformer decoder
