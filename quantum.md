## Background 

Good high level article on what supremacy is about https://www.quantamagazine.org/john-preskill-explains-quantum-supremacy-20191002/

Long blog post on challenges for quantum computing https://medium.com/@jackkrupansky/the-greatest-challenges-for-quantum-computing-are-hardware-and-algorithms-c61061fa1210

Still need way more qubits for quantum cryptanalysis or quantum crypto because right now we can do at most 52 bits and we need closer to 1,000 for crypto and quantum ML 

Quantum ML specifically is interesting because matrix sizes dont matter so we can do really fast matrix multiply - related to optical computing work from Stanford lab

Linera cross entropy benchmark

Supremacy results by Google are on a contrived problem but still shows experimentatlly that QC can be better than classical. IBM rebutted them with a proposal for a classical speedup and over time we can also expect classical computers to get better so benchmark target will change over time

Adiabatic computing uses annealing to find results. Dwave has shown no evidence of quantum advantage yet https://en.wikipedia.org/wiki/Adiabatic_quantum_computation

Debugger in QC is not possible but classical simulations in a web browser are definitely possible but will just be slow. Lots of cloud providers provide 5 or 9 bit real quantum machines to simulate via the internet with their own APIs - lots of books too, even oreilly ones

Aaronson wrote a bunch of comments https://www.scottaaronson.com/blog/?p=4317 

Studies use sampling methods to figure out whether the results of classical and quantum match and then take cross entropy between two distributions to assess differences in results.

Google effort is the first generally programmable one. Physical processes that do some computation generally don't work well for arbitrary computation

Next big steps will be around quantum error correction and more qubits which are both hard problems and using less samples to verify correctness

There's a strong tension between extended church turing (being able to simulate problems efficiently) and quantum mechanis - relationship has been known since 1980s

Boson sampling - perform arbitrary computations by sampling bosons scattered by interferometer - actually invented by Aaronson

## Characterising Quantum Supremacy in Near Term Devices
* Provide a proof that a problem would take a long time (10,000 years)
, IBM rebutted that they could do it in 2.5 days instead on a classical computer
* Comes up with method to measure difference between quantum output and classical output when classical output takes exponential time
* Simulates random quantum circuits


## A blueprint for demonstrating quantum supremacy with superconduction qubits
* 50-100 qubit would revolutionize scientific research and let us solve many exponential problems in physics, chemistry and material sciences

## Great older references I used
* Vazirani course notes
* Scott Aarom QC since Democritus book
* Computational complexity book by Barak (he wrote a new intro to CS math book which is also great)
* There are so many more released since last time I checked
* Nielsen from YC research also wrote a theory book should check it out https://www.amazon.com/Quantum-Computation-Information-10th-Anniversary/dp/1107002176/ref=pd_bxgy_14_2/131-3331144-0774962?_encoding=UTF8&pd_rd_i=1107002176&pd_rd_r=e14d8808-0be0-4b53-ae68-2df6b81fc348&pd_rd_w=l1l4n&pd_rd_wg=Pu9Cn&pf_rd_p=09627863-9889-4290-b90a-5e9f86682449&pf_rd_r=RBK4MTBH545RJQTDXDW2&psc=1&refRID=RBK4MTBH545RJQTDXDW2
* Oreilly book more programming heavy - assume interface exists, how would you program algorithms
