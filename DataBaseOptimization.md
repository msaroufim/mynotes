# Database optimization
* https://arxiv.org/pdf/1808.03196.pdf
* Database join optimization is about looking at n relations/tables and deciding in which order to join them and how to sequence it. Many heurisitics exist, one of the more popular ones involve some sort of dynamic programming structure such as left deep plans
* Enumerated subplans are typically memoized to figure out the next optimal join. 
* Q learning relaxes the memoization constraint for 1 step
* Build actual software on top of apache Calcite, SparkSQL in less than 300 lines of code
* Can create training data by using current optimizers and trying out all possible join plans (I don't understand how this would generalize to new join plans though)
* Benchmarks are Join ORder Benchmark and TPC-DS. Imrpovement over SOT is 1.7-3x
* Join ordering is NP hard lol, most approximations give linear cost functions (in the input size) to study joins but real world DBs have some non linear costs like a large intermediate result that forces partitioning over multiple machines which affects physical join performance
* 1 page explaining what RL is and talking about the Bellman optimality condition
* Join cost function outputs a positive treal number
* Has a short proof of why greedy join is suboptimal
* Featurize join decision and graph state and apply the typical RL formula as ```L(Q) = \sum_i || y_i - Q_\theta(G,c)||_2^2 (they do mention that there are other algorithms but they don't use them in this paper)
* Access to an optimization oracle turns this into a sort of supervised learning problem
* Database joins have a compositional structure which doesn't show up clearly in RL
* Dataset consists of a ```List<graph, join, graph' cost>```
* Classical join optimizers give the incremental cost of each join which we can use as training data which also means that a single query generates multiple training examples because each subquery has its own cost which needs to be estimated (different than RL setting where you wait till the very end to get a reward)
* Dataset consists of the results of some random joins (epsilon random, RL has a similar idea with exploitation vs exploitation) + joins from good optimizers
* Featurizing the join has 3 components. They mostly study foreign key evaluation, they could have added stuff like index but they didn't
    1. Featurize the attributes using a 1 hot encoding
    2. Scale the attribute from 1 by its selectivity (percentage occurence in the data)
    3. Featurize physical operator (1 hot encoding on the number of physical operators)
* Training network is an MLP (vanilla NN) with just 2 layers  with training time less than 10min with SGD (which is an odd thing to see in an ML paper). Training on one query can generalize somewhat to new queries with retraining
* Also use real running time as one of the costs in RL
* Some related papers look at using Deep RL for cardinality estimation
* Appendix has more details around CM1, CM2 and CM3




## Open questions
* What does selectivity mean? (predicate selectivity estimation)
* What is Selinger optimization design exactly?
* What is meant by avoiding cartesian products? (section 2.3)
* What's an index join? What's a hash join operator?
* Look at join ordering and physical operator selection (not sure what the latter is?)
* How much time do large joins take? Is 10min nothing in comparison?
* What's the time complexity of joins? O(2^n)? The proposed algorithm in the paper is O(n^3)
* 3 cost models used CM1, CM2 and CM3 - need intuitive explanation for this
* What's the LEO optimizer? uses corrections for runtime to correct its estimates


