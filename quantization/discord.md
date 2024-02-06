## Mojo

Claims they support quantization in their docs but I can't find any details online https://docs.modular.com/engine/faq.html#functionality

## Lit-gpt

https://github.com/Lightning-AI/lit-gpt/blob/main/tutorials/quantize.md

Quantization is delegated to bits and bytes with supported dtypes being
* nf4
* nf4-dq (double quantization)
* fp4 ants its dq variants
* int8


## Tinygrad

Unclear if tinygrad supports tensor corres

Some people did try to get a llama.cpp loader working but it was never merged https://github.com/tinygrad/tinygrad/pull/1892

## Nous Research
Papers mentioned
* Smoothquant https://arxiv.org/abs/2211.10438
* gguf or gptq quantized seemed to work best for folks as formats

miqu = quantized mistral medium

## llama.cpp
Look at how ggfu quantization format apis look like

## Open access AI collective (axolotl)
* LoftQ https://arxiv.org/abs/2310.08659
* Quantization types like awq, gptq, squeezellm
* More researchy: partially binarized LLMs https://github.com/hahnyuan/PB-LLM
* Tim Dettmers trick: quantize base model, merge, convert to bf16 then do further conversion like gptq https://discord.com/channels/1131084849432768614/1139035605616042085/1144306185885982831
* Deepspeed and FSDP dont support quantizaiton

## Skunkworks ai
* RMKV format?
* Reorder based post training quantization for LLMs https://github.com/hahnyuan/RPTQ4LLM
* exllama uses quantized weights https://github.com/turboderp/exllama
* https://github.com/ggerganov/ggml/blob/master/docs/gguf.md this specification describes how llama.cpp supports quantiztaion


## The bloke
* Many many requests for quantization to work with vLLM
* Not too much references to academic work but a lot of references to applied repos like AWQ, AutoGPTQ and GGUF

## Yannic Kilcher
Best discord for papers
https://github.com/Vahe1994/AQLM
* Lattice cookbooks 2 bit quantization https://cornell-relaxml.github.io/quip-sharp/
* 8 bit optimizers paper https://arxiv.org/abs/2110.02861
* Interesting old intuition by shawn on why quantizing optimizers is rare https://twitter.com/theshawwn/status/1318668210338672644
* Post training quantization does not work out of the box for diffusion models https://arxiv.org/abs/2302.04304
* Vector quantization library https://github.com/archinetai/bitcodes-pytorch not sure how popular this approach is
* Extreme compression by deepspeed folks https://arxiv.org/abs/2206.01859
* 8 bit optimizers with block wise quantization https://arxiv.org/abs/2110.02861

## TPU podcast
* Interesting paper on working through batchnorm issues for quantization https://arxiv.org/abs/2101.08430 (I believe issues are batchnorm typically does need very high precision)

## Eleuther
* High fidelity neural audio compression https://arxiv.org/abs/2210.13438
* Interesting use case of someone running llama.cpp on a switch https://discord.com/channels/729741769192767510/730095596861521970/1200705597268566027
* Interesting dequant kernels https://github.com/casper-hansen/AutoAWQ_kernels/blob/main/awq_ext/quantization/dequantize.cuh (should API basically be quantize, dequantize?)
* From zippy again, sad that he can't load the model unless he can quantize it https://discord.com/channels/729741769192767510/730095596861521970/1194556382947573941 feels like we should make it easier for people to quantize a model with limited VRAM on CPU