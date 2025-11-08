# PyTorch APIs for High performance MoE training and inference

Notes from the youtube talk


MoE model -> router decides which expert is most suitable to deal with a token, experts are smaller, computation is lighter and models can generally store more information than a single linear layer

Goals
1. Support EP
2. Efficient routing
3. Have an option to avoid host sync points (important to support cuda graphs and avoid cpu overhead). Involves token dropping
4. Support block-sclaed formats for Blackwell, rowwise scaling on Hopper

Token shuffling: token splits are determined by router which is a dynamic computation done as a matmul on a gpu
Non contiguous token chunks: if using 1D all-all, tokens are interleaved. Can use sym memmory to make this fast

PyTorch shuffle API all_all_vdev_2d and all_to_all_vdev_2d_offset

Expert computation gemm kernel

grouped_mm(Tensor self, Tensor mat2, Tensor offs=None)

self all the tokens that came to this device

Group gemm is a linear op so a lot of the existing formulas in backprop work just fine in pytorch, just have to take offsets into account

Implementation: precompiled CUTLASS template with hardcoded heuristics supports sm90 and sm100

In torch.compile use triton template and also have a cuteDSL template for blackwell. Uses TMA loads

MXFP8 training for MoE. Scaling factor is `[1x32]` - uses dynamic quantization

`to_mxfp8_and_scaled_grouped_mm()`

