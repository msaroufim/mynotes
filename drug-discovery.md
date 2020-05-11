# Biology and ML

## Drug Discovery

## Protein Folding

### Problem definition
https://www.technologyreview.com/2018/12/03/138830/deepminds-ai-system-will-accelerate-drug-discovery-by-predicting-how-proteins/

* predict shape of protein by looking at sequence of amnio acids
* relevant for drug discovery

This means that it should be possible in principle to predict the shape without too much domain knowledge, similarly to the molecular fingerprinting work

Compute pairwise distances between amino acids which are present in the protein? A protein is just a long amino acid

Given Sequence and MSA features -> DNN -> predict distance and torsion -> minimize protein specific potential in loss function

Bond lengths are known so can fully characterize the geometry with the angles between amino acids
The problem is also constrained to the backbone not so much the superficial bonds? But open question is how do you know what's backbone and what is not

Two core problems
1. Blind prediction, predict shape of protein without data
2. Template predicition, use data from similar amino sequences to predict shape of protein

Alphafold does 1 not 2. 2 is much easiser. Alphafold beats all techniques that do 2 by doing 1.

Main model uses Resnet.

Contact prediction: is the angle less than x?
Alphafold: the angle is x which is a harder problem
Covariation: signal that tells you where residue will be in contact

Deep Learning is generally useful for protein prediction because the dataset and loss function are clear and well understood and the sequences are very long

Visualzie the distances in a 2d matrix, [i,j] pixel is the distance between amino acid with index i and acid with index j

Predicting the actual distances and torsion angles can be solved using 2 deep residual networks. Structure of each network follows batchnorm, ELU, 3x3 dilated convolutions which skip some points

Data augmentation they use is to crop proteins into 64x64 chunks

End level precision @ L is just %50 

https://en.wikipedia.org/wiki/Ramachandran_plot

### Basic definitions
* When a polypeptide contains more than fifty amino acids it is known as a protein
* What is MSA?
* How is the data used exactly?
* Get some sort of basic biochemistry reference


### Related applications
* Protein to protein interaction
* Small molecule binding
* protein design
* experimentally assisted structure prediction


### References
* Code: https://github.com/deepmind/deepmind-research/tree/master/alphafold_casp13
* Paper: https://www.nature.com/articles/s41586-019-1923-7.epdf?author_access_token=Z_KaZKDqtKzbE7Wd5HtwI9RgN0jAjWel9jnR3ZoTv0MCcgAwHMgRx9mvLjNQdB2TlQQaa7l420UCtGo8vYQ39gg8lFWR9mAZtvsN_1PrccXfIbc6e-tGSgazNL_XdtQzn1PHfy21qdcxV7Pw-k3htw%3D%3D
* Dataset: CASP, Protein Data Bank 
* Talk: https://www.youtube.com/watch?v=uQ1uVbrIv-Q



## Molecules

A popular library for workin with molecules is DeepChem but it looks like it's UNIX only so will need to install the Windows Linux Subsystem to get it working on this PC.

TODO: the maintainers of this library are great to meet https://github.com/deepchem/deepchem/tree/master/examples

DeepChem community has about 400 people https://gitter.im/deepchem/Lobby

* We can identify the molecules in a sample via mass spectroscopy but as far as software is concerned we can abstract away this part
* How to featurize a molecule?
    * Featurize it as a string using SMILES format, there is a python library for this - https://pypi.org/project/pysmiles/ and then can use the library to display the string as a networkx graph. Given a string representation we can use sequence models like RNN to do some classification or prediction. DeepChem uses RDKit for this
    * 

#### Some use cases of DeepChem that I care about
* Modeling solubility: how likely some substance is to dissolve
* Synthentic feasibility scoring: measure of complexity of manufacturing of some chemical substance
* Using NLP for toxicity predictions?

## Modeling solubility
* Using DeepChem to module solubility
* Data format is in a CSV but the most important columns are the SMILE format which is a string that represents a molecule and then solubility
* RDKit has a helper function to visualize a molecule as a graph png from the SMILES string format
* Solubility of the dataset is centrered around -3
* Very similarly to NLP, ML algorithms do not understand what string is. So you need to transform this string into a vector. Hashing would probably work but I'm guessing some hashing mechanisms would preserve more information. They use a featurizer, NLP uses the exact same kind of API
* Once featurization is ready you have a supervised learning problem where given a molecule as a vector predict solubility which is a real number. This is an example of a regression problem.
* Typically in ML problems your features will have different magnitudes and variance which will skew your results so you wanna normalize them. This is done for any sort of tabular data example
* Can use any off the shelf supervised learning example to do the regression and you output root mean square error
* Featurization is done via a circularfingerprint ECFP4 featurization https://docs.chemaxon.com/display/docs/Extended+Connectivity+Fingerprint+ECFP which is basically a way to embed molecules into a datastructure where similar molecules will have similar ECFP4 characterization. TODO: Read more about this format

This looks really interesting, I'll read up some more about this later

```xml
<IdentifierConfiguration>
        <Property Name="AtomicNumber" Value="1"/>
        <Property Name="HeavyNeighborCount" Value="1"/>
        <Property Name="HCount" Value="1"/>
        <Property Name="FormalCharge" Value="1"/>
        <Property Name="IsRingAtom" Value="1"/>
    </IdentifierConfiguration>
```


## Synthetic feasibility scoring
* Ranking algorithm to measure relative complexity of molecules. What does it mean for a molecule to be complex?
* In the real world you could use purchase cost, or number of reaction steps required as your complexity score. 
    * Purchase cost is public information, apparently you can buy molecules online https://www.peprotech.com/en/small-molecules
    * Is there a way to algorithmically determine the number of reaction steps?
* The ranking in the repo is done by creating a dataset where you have a pair of molecules ```[molecule_1, molecule_2]``` and then the prediciton is which one is more complex ```[0,1]``` which is binary classification and to decide which label we have we need to use publicly available purchase cost or number of reaction steps

## Convolutional Networks on Graphs for Learning Molecular Fingerprints
https://papers.nips.cc/paper/5954-convolutional-networks-on-graphs-for-learning-molecular-fingerprints.pdf

Benefits
1. Features are more interpretable
2. Better performance on downstream tasks
3. Vectors are smaller if learnt via a neural network
4. Similar molecules or submolecules will have similar structure

Based of circular fingerprint technique

Past work has has custom designed features to turn a molecule of arbitrary size into a fixed length vector and then feed that vector to a deep neural network

They call the work convolutional because you first compute local features on each atom and then aggregate them globally across all atoms via the edges/bonds

Applications
1. Solubility: Regression
2. Drug efficacy: Predict the dose/response
3. Organic photovoltaic efficiency: regression, given a substance how effectively does it turn light into electricity. Main application is consumer electronics

> Circular fingerprints are analogous to convolutional networks in that they apply the same operation locally everywhere, and combine information in a global pooling step.

Let's say we start at some submolecule, give it a vector representation and then we concatenate this representation with the representation of its neighbors.

Softmax is a differentiable version of an index 

We don't our encoding to change depending on which neighborhood we started with. Neighborhood invariant.

We can visualize which subparts of a molecule most activate a certain prediction (e.g: toxicity or solubility) by looking at the subgraph with the highest activation

Experimental setup Our pipeline takes as input the SMILES [30] string encoding of each
molecule, which is then converted into a graph using RDKit [20]. We also used RDKit to produce
the extended circular fingerprints used in the baseline. 

Training used batch normalization

Experiments whshowo about 5x improvement

Training took at most an hour

Molecules tested were mostly small but for large molecules we'd need to perhaps use hierarchical techinques

# Open questions
* Related work, can topolically sort a molecule as a tree and then input that tree to a recursive neural network - can this be made faster?
* Does multitask learning help here
* Implementation uses a CPU but it also uses batch normalization which means we can expect 100x speedups on a GPU 






https://github.com/HIPS/neural-fingerprint


## References from Mazen
https://en.wikipedia.org/wiki/Coherent_Accelerator_Processor_Interface