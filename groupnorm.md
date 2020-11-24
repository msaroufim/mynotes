If 0 mean and variance 1 is good for input its good for each layer

Features spread more for deep neural networks - become too big or too small

If you just have a mini batch then you can't know the true mean and variance, you can guesstimate it - the larger the batch, the better the mean estimation will be

 Since the mean and variance of each batch differs it's also common to have a learnt linear layer to automatically correct data

 For distributed ML with small batches this causes issues since your estimate of the mean will be poor OR at every layer you do a synchronization step where you track a global mean and variance

Types of normalization
* Batch norm: Batch norm t  akes 1 channel and calculates mean and stdev of that channel and uses that to do centering scaling operation. In non convolutional net you would basically normalize per feature on all examples in a batch [np.mean(x)/np.stdv(x) for x in batch(tensors) ]
* layer norm: Look at all channels and get mean accross all pixels and all channels - np.mean(whole_tensor). This is kind of drastic
* instance norm: Normalize each channel individually - [np.mean(x)/np.stdv(x) for x in tensor.channel]
* group norm: Mix between layer norm and instance norm - pick contiguous channels and normalize accross them

Good summary in code https://twitter.com/marksaroufim/status/1331123335833370626

Batch-norm: [(np.mean(y), np.std(y)) for y in x for x in batch()]
Layer-norm: (np.mean(x), np.std(x))
Instance-norm: [(np.mean(x), np.std(x)) for x in tensor.channels]
Group-norm: [(np.mean(x), np.std(x)) for x in tensor.groups]  

x_i^ = (x_i - np.mean()) / np.std()