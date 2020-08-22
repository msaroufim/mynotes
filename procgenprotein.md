# Transcript and notes from procgen protein paper

Generative modeling for protein engineering


## De Novo protein structure prediction
De novo methods tend to require vast computational resources, and have thus only been carried out for relatively small proteins. De novo protein structure modeling is distinguished from Template-based modeling (TBM) by the fact that no solved homologue to the protein of interest is used, making efforts to predict protein structure from amino acid sequence exceedingly difficult. Prediction of protein structure de novo for larger proteins will require better algorithms and larger computational resources such as those afforded by either powerful supercomputers (such as Blue Gene or MDGRAPE-3) or distributed computing projects (such as Folding@home, Rosetta@home, the Human Proteome Folding Project, or Nutritious Rice for the World). Although computational barriers are vast, the potential benefits of structural genomics (by predicted or experimental methods) to fields such as medicine and drug design make de novo structure prediction an active research field.

# Abstract
We train a 1.2B-parameter
language model, ProGen, on ∼280M protein sequences conditioned on taxonomic and keyword
tags such as molecular function and cellular component

## Metrics
We train a 1.2B-parameter
language model, ProGen, on ∼280M protein sequences conditioned on taxonomic and keyword
tags such as molecular function and cellular component


a = [a1 ... a_n] list of amino acids
c = [c1 ... c_k] list of condtions such as taxonomic and keyword tags such as molecular function and cellular component

There are exponentialy more protein sequences than structures

Once you get a controlled generated sequeence you can infer the result

## Architecture
Variant of the Transformer (I have other tutorials on this topic) - I'll add them to the description)

We're doing masked language modeling where the tokens are amino acids and tags

## Data
* Uniparc, UniprotKB, SWISS-PROT, TrEMBL, Pfam 
* Vocabulary is 25 amino acids in IUPAC

Keyword tags: 1100 terms from cellular component, biological process and molecular functional terms
Taxonomic tags: 100K terms from NCBI across 8 ranks

# Training
Include sequence and its reverse - prepend each sequence with its condiitoning 

Amino acid designation here https://wissen.science-and-fun.de/chemistry/biochemistry/iupac-one-letter-codes-for-bioinformatics/

SWISSPROT (conditioning tags are here) https://www.uniprot.org/docs/userman.htm

So this work created their own dataset to make thing work

## How to use procgene
Generate proteins one amino acid at a time and keep doing this until you get the desire length
Use top k sampling to have more diversity

## Evaluation
1. NLP - perplexity, low perplexity is good 
2. Protein: BLOSUM block substitution matrix specifies which amino acid substitutions are more likely

### Metrics

1. Primary sequence similarity: computed with Biopython package based on Needleman Wunsch algorithm (global pairwise sequence alighment)
2. Secondary structure accuracy per residue using Psipred package
3. Conformational eenergy Rosetta Relax DB protocol

### Results
* Generalizes to test set and out of distribution protein families
* Can finetune on unseen families
* Perplexity reduces near the end of a protein sequence
* Could use even larger models 
* Learns mutational invarariances - some substitutions would be acceptable in nature according to BLOSUM62

The two charts are great in the results page conditioning tags, sequence length interval

More conditioning tags produces better generative results

More context from the sequence provides better similarity metrics
They also chart these metrics vs randomly mutating 50%

## More testing
Out of test distribution ran on VEGFR2
Tyrosine-protein kinase that acts as a cell-surface receptor for VEGFA, VEGFC and VEGFD. Plays an essential role in the regulation of angiogenesis, vascular development, vascular permeability, and embryonic hematopoiesis. Promotes proliferation, survival, migration and differentiation of endothelial cells


## Goal of protein generation
The ultimate goal of protein engineering is to engineer functional proteins. One promising avenue is via directed evolution, which iterates through rounds of mutation and screening to converge on a high-fitness (i.e. functioning) protein.
Machine learning has shown initial promise to aid in the
subsequent rounds of directed evolution by in silico screening of proteins (Wu et al., 2019), but it still relies on random
mutation in an exponentially large search space. Ideally,
a generative model, such as ProGen, that has learned the
distribution of evolutionarily-relevant proteins can directly
generate high-fitness proteins.

https://en.wikipedia.org/wiki/Epistasis#:~:text=In%20classical%20genetics%2C%20if%20genes,the%20gene%20for%20brown%20hair.

## Conclusion + Appendix

PCA embeddings project to our understanding of amino acids: aromatic, aliphatic, small, polar

They also tried generating sequeences with only conditioned tags which are then passed to the HHblits package to search for MSA (can also visualize)

Attention heads visualized with VIG







