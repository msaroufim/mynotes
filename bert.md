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

# https://github.com/pbloem/former
Code is made up of 9 files for a total of 500 LOC (vs popart example is closer to 10K lines of code)
Good habit is setup ```environment.yml``` file https://github.com/pbloem/former/blob/master/environment.yml

1. We want to learn a weight from each input state to each output state
2. Each weight represents a correlation of each input state to each other input state
3. We want the weights to sum up to 1

After we come up with these weights we can jsut do forward or backward propagation without thinking about it too much.

Attention is something you can do without learning the weights but you can learn them from data in a self supersivesed way using various methodologies like next sentence prediction.

Query: compute meaning vector for your own output
Key: compute relationship between word_i in input and word_j in output
Value: compute relationship between word_i and all outputs

We're gonna learn a matrix for eahc of Q, K, V

And then we take a dot product between all of them and do a softmax

Since embeddings are so big then we scale them by ```sqrt_root(embedding_dimension)```

We do this operation with multiple values of Q,K, V and append all the representations together. Multihead attention, I wonder how necessary is this? Aggregation always helps

There's 2 ways to do self attention
* Keep full size for each head
* Scale head size

Depends on how much memory and compute you can afford

It's not obvious how to apply batch normalization to sequences which is where layer normalization comes in https://arxiv.org/pdf/1607.06450.pdf

## Code Walkthrough
/former

### Modules

#### Attention
The only difference between wide and narrow attention is the size of the head
Key, Query, Value which we've defined earlier

#### Transformer Block
1. Attention layer
2. Layer normalization

Attention is just a bunch of stacked dot products with a fotmax

```python
# Attention layer
#That's it
dot = F.softmax(dot, dim=2)
# - dot now has row-wise self-attention probabilities

# apply the self attention to the values
out = torch.bmm(dot, values).view(b, h, t, s)

# swap h, t back, unify heads
out = out.transpose(1, 2).contiguous().view(b, t, s * h)

return self.unifyheads(out)

```

### Transformer module
* Generating Transformer
* Classification Transformer

### Classification Transformer

#### Init
1. Create token and position embedding
2. add a bunch of transformer blocks in sequence in a list and then we turn this into a pytorch sequential model
3. Turn into propabilities by using # of classes
4. Dropout

#### Forward pass
1. append token to position
2. Pas intput to model which is a lsit of transformers
3. Get probabilities via softmax

```python
tblocks = []
for i in range(depth):
    tblocks.append(
        TransformerBlock(emb=emb, heads=heads, seq_length=seq_length, mask=False, dropout=dropout, wide=wide))

self.tblocks = nn.Sequential(*tblocks)
```


Classification usig Transformer
1. Setup data using torchtext
2. Setup model from parameters in CLI
3. Make prediction, look at actual label and backrpopagate
4. no_grad measure accuracy

```python
print(f'-- {"test" if arg.final else "validation"} accuracy {acc:.3}')
```

## Hugging face implementations
It also uses token embeddings and otherwise looks identical to the previous codebase

It uses the narrow attention by default

More complicated than the other codebase and unclear to me why at this point

## Graphcore implementation

Code feels almost impossible to understand, I need a few more days to get this.

There's a bunch of custom poplar ops
* Group pattern
* Sparse SGD
* Disable dropout for inference


All the configs for models are in JSON files

Data is created
* Sampler in Python, includes a distribute dsampler which uses MPI
* Custom tokenization
* Custom data downloaders for squad and wikipedia


Base
* What's up with the optimizer factory?
* Why is ONXX used so much?
* Model is in ```bert_model.py``` and the task specific implementations are in ```bert.py```

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
