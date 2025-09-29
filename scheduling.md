https://www.usenix.org/conference/osdi24/presentation/choudhury

Mast has a few key interesting principles
1. Temporal decoupling: ie. monitor patterns over time, which datasets are used, where, which jobs are periodic to figure out in which region to allocate data and compute
2. Scope decoupling: Allow scheduling decisions to be at the tenant or regional level
3. For both 1-2 you can use some version of integer programming to ensure proper scheduling of data. GPU over-subsricption is OK because we can just queue jobs to a GPU and we can preempt low priority jobs

