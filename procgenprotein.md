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

## Other video summaries
## AI coffee break
https://www.youtube.com/watch?v=pFf4PltQ9LY&list=WL&index=2&t=0s

* BERT can be used on text or images
* What about analyzing protein structures
* Uses masked word prediction
* Self attention compute simportant scores in the same sequence, attention tokens from different sequences
* Learns coreference, part of speech etc..
* 3 important pieces in how cells live DNA, RNA, Protein - DNA is blueprint and protein is machinery - DNA has letter A - T - C - G. Proteins have 20 amino acids
* Proteins are 2d sequences of amino acids but they live in 3d space and these structures can be understand via secondary srtructure, tertiary structure and quaternary structure
* Proteins interact at binding sites - partner protein is called a ligand
* In NLP we have words that we build into sentence
* Take amino acid sequence mask it and then figure out MLM - english vocab is 10K vs vocab here is 20
* For detecting interesting properties like binding sites they look at attention patterns to look at properties of amino acids
* Find attention heads that align with contact map, heads attention is highly correlated with binding site 


## Yannic Kilcher
https://www.youtube.com/watch?v=q6Kyvy1zLwQ&list=WL&index=3&t=0s

* Jesse Vig the visualize attention layers guy
* Trained to perform language modeling
* Can inspect the BERT model using attention heads 
* Yannic keeps calling this investigative work
* Both mention to make sure you subscribe
* DNA an encoding of all biological functions are realized through proteins -> DNA -> RNA polymerase -> Protein which is a chain of amino acids - 20 diffferent amino acids
* 3d shape is very important, shape determines function - proteins can cut, some can hold stuff 
* Amino acids can be substituted and if the shape doesn't change then the function doesn't change
* Spans form helixes or sheets - nice to show them on the video directly - tertiary structure is the whole thing for e.g doulbe ring
* Does BERT solves 2 problems?
    * Does BERT know which amino acids are going to end up in contact with each other and where the binding sites are
    * which amino acids can bind to other molecules - hemoglobyn traps oxygen in blood
* If molecule 1 and 3 are contact sites or binding sites then there should be one layer where the connection is strong between them 
* To validate where those connections are you need a seperate software stack to predict them and then you're not training on this supervised data but just checking if it makes sense
* Probing task: take a layer and run it through a linear classifier, is this a binding site
* THey took a pretrained BERT model, find attention heads that correlate with some specific amino acids
* Because vocab is small then you can have attention on single tokens especially in first layer and in the last layer it would specialize to the last token
* You can substitute an amino acid and nothing really happens this is represented as BLOSUM62 substitution matrix - it's litterally a 20 x 20 matrix where high values mean you can substitute
* For 2 amino acids get the attention matrix and then calculate correlation of 2 - the more correlated patterns are the more likely we are to substitute them
* I like this idea a lot of thinking of an example as all its attention examples and taking correlations between them
* Attention is largely consistent with blosum62 scores
* Attention is strongly correlated with contact location
* For tertiary structure binding site comes in later layers but problem is harder - this makes intuitive sense since tertiary is harder than secondary
* Are there limitations to this model? Should we add more data? Make the model bigger or capture more information besides just sequences

## Additional references

May need to read the BERTology paper as well https://arxiv.org/pdf/2006.15222.pdf
Dani channel is a good model for combining humor into the episodes https://www.youtube.com/watch?v=nR9UfOueJPU
I wonder if I should also buy a greenscreen
Need to make sure we implement VIG mechanism to visualize attention layer
After the MLM model is done need to take a look at attention layers with vig then do the correlation study with blosum. See which heads are aligned with contact prediction (find a dataset that has information about this)