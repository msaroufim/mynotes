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


