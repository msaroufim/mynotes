# Unified Framework for modeling multivariate distributions in biological sequences

## Problem definition
Multiple Sequence Alignment (MSA) is generally the alignment of three or more biological sequences (protein or nucleic acid) of similar length. From the output, homology can be inferred and the evolutionary relationships between the sequences studied.


## Abstract
* Reveal functional site of biological sequences such evolutionary conserved structurally interacting or co-evolving protein sites
* Past approaches involved position specific scoring matrices (PSSM), Markov random fields (MRF), multi variate gaussian models (MG) and auto encoders (AE)
* Works proposes a unified framework for all of the above and enhances interpretability of prediction process

## Intro
* Function of RNA or protein is encoded in as equence itself, very hard to predict function from a single sequence. 
* Instead leverage pwoer of evolution and comaprison to identify which postions are conserved and which pairs of positions are coevolving, supporting their relative importance
* Statistical properties are infered from MSA via some generative model
* One body: evolutonary conservation accross species - vs two body: coevolving positions
* MRF and Gaussians are unified in this framework

## Results
* Homologous sequences in MSA in X \in N x L x K
    * where N is the number of sequences
    * L is the length of the sequences
    * and K is the alphabet size
* Which positions are conserved and which subsets of positions are coevolving?

### PSSM 
* Categorical Cross Entropy between each position character and predicted summed over whole sequence length L over all sequences N
* Captures 1 body information, also called site independent patterns also called evolutionary conservation

### MRF
* Model parameters are R ^ [L x K x L x K], model pairwise interactions, matrix is reshaped into W in R [LX x LK] is symmetric and has zero values on diagonal

## MG
* Multivariate gaussian can be reformulated as mean squared error

### Unifying
* maximizing pseudo likelihood of MRF is like minimized CCE and maximizing likelihood of GM has the same global otpima as minimzing eman squared error
* This means that both models can be formulated as a single dense layer that maps input data onto itself. MRF explicitly removes connection to itself but MG keeps it

### Application: Protein Contact Prediction
* In MRF the two body term is used for graph or contact map inference

## Useful references (some are behind a paywall)
* THe original paper studying this topic: Stormo, G. D., Schneider, T. D., Gold, L., and Ehrenfeucht,
A. Use of the Perceptron algorithm to distinguish translational initiation sites in E. coli.
* There are a billion MSA tools https://www.ebi.ac.uk/Tools/msa/
* Benchmarking needs to be done vs a GPU since this work is replaced by a single dense map, should be faster on an IPU if layer is small
* Generative models for protein fold families http://www.stat.cmu.edu/~siva/Papers/Proteins11.pdf
* Hidden Markov Models for Protein Generation https://www.researchgate.net/publication/8102028_Recent_Applications_of_Hidden_Markov_Models_in_Computational_Biology/link/0c96052777c9b52f1d000000/download

# Learning generative models for protein fold families

## Introduction

This is the original GREMLIN paper, implementation is simplified by using a dense neural network using the work above

GREMLIN (Generative REgularized MOdels of Proteins)
* Learn an unidrected probablisitic graphical model of amino acid composition within MSA - e.g: PFAM contains 11K HMM models learned from MSA
* Graphical model can then be used for structure and function classification and to design new protein sequences
* Graphical model where
    * Node is column of MSA
    * Edge is conditional independencies between columns, correlated mutation statitics between pairs of residues
* It's necessary to model pairs of residues and it can be done efficiently with an MRF 

## How it works
* MRF is an undirected graph 
* probability of a sequence is a function of potential of the individual nodes and pairwise potential between edges
* Instead of computing max likelihood, can approximate it with CCE loss
* Use L1 regularization to encourage sparsity