# Custom Hardware

## Inference Challenges and Research Directions
https://www.arxiv.org/pdf/2601.05047

### Memory Wall
- HFM (High-capacity Flash Memory) stacks flash like HBM and enables much larger storage for less frequently accessed things like weights
- KV cache still needs to be on HBM, but costs are ballooning

### Process Near Memory (PNM)
- Fast bandwidth but limits software kernels, challenges with software sharding
- Need to shard your program to run mostly on local data and do minimal cross-bank communication (clunky for things like softmax) but it can work for things like simple reductions
- Compute near DRAM also means heat and causes reliability issues
- Fixed compute per GB ratio when some workloads want to be more dynamic
- PNM (Processing Near Memory) uses a separate die that's close, so not as badly coupled

### 3D Memory Logic Stacking
- Instead of a single connection between CPU die and DRAM, you stack them both vertically and can have multiple connections
- Improves bandwidth, not latency
- Causes thermal issues and manufacturing is more complex

### Low Latency Interconnect
- Some topologies diminish bandwidth but improve latency
- Spine-leaf seems to be one of the best for training
- For inference: hierarchical intra-node, in-rack, and inter-node fat tree
- Thin trees cause high latency, so fat trees are preferred where upper layers have more switches
- Spine topology: GPUs are connected to leaf switches and those leaf switches are connected to spine switches, so there's at most 3 hops
