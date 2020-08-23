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

## Attention heads visualized with VIG
This work is interesting visualizes attention layers by depth and head to get a general sense of patterns
Early layers focus on neighbors
Middle layers focus on dependency parse and part of speech
End layers focus on the whole sentence

Can also take a neuron view and seee which neurons gave the highest attention weight to which query and key and most influence softmax(q . k)


# Transcript
## More references
Mention Khan academy class
Intro to protein structure book by branden and tooze


For references on transformers the peter bloem article is great or you can see some of my vidoes on the subject, i'll put the details in the description

At every step you get a distribution over tokens


Protein engineering, making new kinds of substances, drugs, materials, gets into the realm of sci-fi very quickly

Image on page 2 is a good summary

If you found this interesting please let me know I'm considering making a series on proteins for ML engineers

0. Why is this work important - protein engineering, make new substances, uses transformers which are amazing at working with language to proteins. The only common thing these 2 problems have is that they're both sequence problems
1. What is a protein - amino acid
    * Vocab size of 23-25?
    * not much structured data lots of sequences
    * Structure determined via x-ray crystallography, nuclear magnetic resonance, electron crytoloography
    * Protein Amino Acid, Side Chain, Carboxyl group
    * Shape determines the function whether its hydrophobic or hydrophylic
    * Amino ACid is a combination of Amino and Acid molecules
    * If DNA is code then protein is an exe or bash script
    * Structure determines function, all differ in side chain
    * Several kinds of structure - primary the order, secondary (parallel, anti parallel)
    * Tertiary interaction of side chain
    * Quaternary: Multiple chains
    * The dream is to provide the function we want as a spec and get a protein that does that. This work gets pretty close to that dream
2. Transformer summary
    * Attention
    * Key, Value, Query
3. Everything is a sequence - vocab
4. Describe data - tags and proteins (Show the datasets)
5. How to measure quality and experimental results with 3 software programs



2 amino acids out of 600 are responsible for sickle cell anemia - small variations make huge changes

Primary -> chain of polypetide
Secondary -> beta and helix
Tertiary -> 3d shape of single polypetide chain
Quatternary -> 3d change of multiple polypetide chain


Figures summary
1. Lots of sequences not many structures, give desired arguments, get protein then infer shape
2. Larger models would be better, no gap between training and test accuracy
3. Token by token prediction, perplexity reduces near the end of a sequence
4. More tags the better the results
5. Less energy compared to mutation and this is maintained accross longer sequences
6. Generalizes outside of protein families its directly seen