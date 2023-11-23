## Marketing pitch

* Integrations with PEFT, HF
* Advertised model is Qwen (probably the best oss model out there today)
* exllama q4 kernels
* Easy perplexity measurements
* Upload to hub
* Clear tok/s benchmarks on the front page

Library has nice progress bars
Triton support - haven't seen the specific kernels yet
BaseQuantizeConfig has all the parameters but no explanation
Library had some breaking changes with exllama but they seem fixed

## Progress bar

Perplexity calculations show progress bars
Quantization and loss per layer is logged verbosely by default (not bad actually)
Triton is warmed up

## UX

Load model on CPU by default so that you can then actually load the quantized version on limited VRAM - so assumption is people have generous RAM or are using some other form of disk offloading

Triton is not installed by default which only supports linux and no 3 bit quantization, triton kernels are set to false by default as well. not super clear what the benefit is


```python

# Quantization

# Load a model on CPU
model = AutoGPTQForCausalLM.from_pretrained(pretrained_model_dir, quantize_config)

# Pass in some example inputs
model.quantize(examples)

# save quantized model to disk
model.save_quantized(quantized_model_dir)

# Load model to GPU
model = AutoGPTQForCausalLM.from_quantized(quantized_model_dir, device="cuda:0")
```

To quantize a custom model you need to annotate your model with

1. Outside layers
2. Inside layers

Here's an example of how Qwen was supported https://github.com/PanQiWei/AutoGPTQ/blob/main/auto_gptq/modeling/qwen.py - presumably doing this per new language model release is not a huge deal

## Accuracy

https://github.com/PanQiWei/AutoGPTQ/blob/main/examples/benchmark/perplexity.py

As simple to run as

```bash
python examples/benchmark/perplexity.py \
    --model_name TheBloke/open-llama-7b-open-instruct-GPTQ \
    --model_basename gptq_model-4bit-128g \
    --is_quantized
    --dataset_path tiny_shakespeare
```

So you give it a base model and a a quantized model and then you compare the perplexity on some dataset like shakespear


Perplexity calculations are shown here https://github.com/qwopqwop200/GPTQ-for-LLaMa#result - they do seem also focused on consumer GPUs like 3090 and 4090

```python
@dataclass
class BaseQuantizeConfig(PushToHubMixin):
    bits: int = field(default=4, metadata={"choices": [2, 3, 4, 8]})
    group_size: int = field(default=-1)
    damp_percent: float = field(default=0.01)
    desc_act: bool = field(default=True)
    static_groups: bool = field(default=False)
    sym: bool = field(default=True)
    true_sequential: bool = field(default=True)
    model_name_or_path: Optional[str] = field(default=None)
    model_file_base_name: Optional[str] = field(default=None)
```




## Triton integration

Triton work is based off of https://github.com/fpgaminer/GPTQ-triton

Benchmarks are all ran on a 4090

Nice explanation of what all the configs mean here 

https://github.com/fpgaminer/GPTQ-triton#explanation-of-groupsize


TODO: 
* Groupsize provides a tradeoff. Lower groupsizes offer more granularity to the quantization and thus less loss of accuracy, but decrease the memory savings offered by quantization.
* num_samples, dataset: used to calibrate the model
* true_sequential: Quantize layers in the order that you would do it during a forward pass, more accurate but presumably slower
* act_order: not sure yet
* sym: symmetric activation, what's the tradeoff?
* static group: not sure yet
* damp_percent: not sure yet


API is a module swap API

```python
make_quant(model, wbits, groupsize)
```

Includes a warmup


```python
make_fused_nlp()
```


So conceptually can get Triton autotuner to work better on my 4090 for best results. So maybe don't need to worry about inductor for now

matmul_4 implemented here https://github.com/fpgaminer/GPTQ-triton/blob/main/src/gptq_triton/quant_linear.py


## Academic notes

Excellent youtube series by Prof Song Han https://www.youtube.com/watch?v=TSc_BibWRhM

* Smoothquant W8A8: insight is that quantization activation is hard because its very sensitive to outliers and magnitudes differ a lot more so idea is to move some of that variance to weights. Scaling factor can be applied offline to weights and online for activations. Most of the network is quantized except for typically the normalization and bias layers https://www.youtube.com/watch?v=U0yvqjdMfr0 so any API needs to be able to offer this kind of flexibility around which types of layers are quantized or which specific keys from the state dict are quantized

We can have several strategies like potentially quantizing earlier layers more because the features are more raw and make sure that the output isn't. So layer wise quant is a stragey and can apply it sequentially


https://www.youtube.com/watch?v=3dYLj9vjfA0&t=254s

* AWQ: W4A16 in the case of bs=1 inference where we really care about memory bandwidth we lose a lot of perplexity at w4 even with group quant (giving the same scaling factor to a X number of elements in a layer) but the insight that we can keep 1% of weights unquantized and keep most of the perplexity. So how do you find the important 1%? You can look at weight distribution similarily to sparsity but this doesnt work so instead we look at activation distribution and our goal is to preserve outlier channels. Can do a similar trick to smoothquant to multiply weight by 2 and divide activation by 2 (or more generally s) and can keep everything the same

So how do we automatically find this multiplier? We can do a grid search or learn it using gradient descent

The baseline for many of these techniques is round to the nearest


