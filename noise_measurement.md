## Timing experiments

What are some considerations that affect timing results

Might be capturing driver overhead
Wrong measurement methodology



## First run

What happens if you use perf timer instead of cuda.event()

Detailed Statistics:
       Shape  Mean (ms)   Std (ms)   CV (%) 95% CI (ms)
------------------------------------------------------------
         4x4     14.144      0.090      0.6      0.006
         8x8     14.144      0.069      0.5      0.004
       16x16     14.149      0.061      0.4      0.004
       32x32     14.146      0.065      0.5      0.004
       64x64     14.194      0.468      3.3      0.029
     128x128     14.192      0.663      4.7      0.041
     256x256     14.154      0.326      2.3      0.020
     512x512     14.232      0.655      4.6      0.041
   1024x1024     14.174      0.171      1.2      0.011
   2048x2048     14.252      0.718      5.0      0.044


## Second run

Go through all shapes until OOM
Covariance decreases as shape increases

Detailed Statistics (cuda_event):
       Shape  Mean (ms)   Std (ms)   CV (%) 95% CI (ms)       GB/s
----------------------------------------------------------------------
         4x4      0.007      0.000      1.7      0.000        0.0
         8x8      0.007      0.000      2.0      0.000        0.1
       16x16      0.007      0.000      2.2      0.000        0.3
       32x32      0.007      0.000      1.6      0.000        1.2
       64x64      0.007      0.000      2.0      0.000        4.6
     128x128      0.008      0.000      1.9      0.000       17.2
     256x256      0.008      0.000      1.7      0.000       69.0
     512x512      0.009      0.000      1.5      0.000      239.6
   1024x1024      0.011      0.000      1.4      0.000      741.6
   2048x2048      0.032      0.000      0.5      0.000     1048.5
   4096x4096      0.080      0.000      0.4      0.000     1687.6
   8192x8192      0.276      0.001      0.3      0.000     1944.0
 16384x16384     15.744      0.451      2.9      0.028      136.4
 32768x32768     48.362      0.452      0.9      0.028      177.6
 65536x65536    195.480      0.451      0.2      0.028      175.8


## General perf considerations
* Temperature control: Lock fan to high value rather than using automatic curves
* Lock power below maximum so I'm not throttled: Meta 500W otherwise max allowed is 700W by NVIDIA SMI
* Disable automatic overclocking
* Lock core clock


One idea is we track
* Runtime variations
* Clock speed changes
* Power draw variation
* Number of processes on this GPU


And if either are anomolous we invalidate the results


(softmax) > python event_overhead.py
Measuring CUDA event overhead...
Event Overhead Statistics (microseconds):
Average: 3.57
Std Dev: 0.08
Min: 3.52
Max: 3.97

Operation with minimal overhead: identity (6.66 microseconds)

For identity event overhead is substantial

## Read about cuda events
* cuda events are mostly useful for timing
* they allow stream synchronization and memory ordering

## Fun stuff

If you run perf.counter you'll get a noisy estimate of cuda launch overhead which eventually converges to 14ms


NVIDIA has a few reasons why they throttle and you can check query for thos

CPU has tons more consideration around thread affinity if we're doing CPU benchmarks


Sensitity to warmups


```
(softmax) > python discard.py

Statistics for different warmup values:
Warmup  Mean    Std     CV(%)
----------------------------------------
     0  32.959  1.414   4.29
     1  32.817  0.013   0.04
     2  32.817  0.013   0.04
     3  32.817  0.013   0.04
     4  32.817  0.013   0.04
     5  32.817  0.013   0.04
     6  32.817  0.013   0.04
     7  32.817  0.013   0.04
     8  32.817  0.013   0.04
     9  32.817  0.013   0.04
    10  32.817  0.013   0.04

```


```python
def get_nvidia_throttle_reasons(device_ids: typing.List[int] = None):
    """See 'nvidia-smi --help-query-gpu for explanation of throttle reasons"""
    queries = [
        "gpu_idle",
        "applications_clocks_setting",
        "sw_power_cap",
        "hw_slowdown",
        "hw_thermal_slowdown",
        "hw_power_brake_slowdown",
        "sw_thermal_slowdown",
        "sync_boost",
    ]
```

Things like clock speed you can get with nvidia-smi -q -d CLOCK but might not need to set it

Per Xu GPU throttling is rare but sometimes happens on cloud instancess

## ncu internals

Per Erik, ncu averages 40 times?

Uses hardware counters like clock64 and implements clock domain correlation between gpu and cpu stamp
Does warp synhcronization and ensure start end for blocks
Minimize thread scheduling variance
Tracks different betwen clocks on GPU vs CPU
USes weighted least squares wher recent samplees have higher weights
Clock monotic raw to avoidd system time adjustments
Actively finds the minimal reliable time interval

## triton.do_bench

They use it in their autotuner

They have some nice utilities to get dram gbps, max tensorcore tflops

They also set the gpu clock setter but its unused

atol and rtol is hard set to 1e-2 and 0 respectively

do_bench() - empty cache for benchmark otherwise just uses regular cuda event with warmup no secret sauce

For cuda graph they warmup with an empty cuda graph first
