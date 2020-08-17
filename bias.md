# Bias in ML

## Fair ML class
https://fairmlclass.github.io/
https://fairmlbook.org/

Topics covered include: causality, sources of unfairness, statistical measures of disparity, criminal justice, impossibility results, causality, measurement sampling,, unsupervised learning, legal and privacy, 

Privacy != Fairness -> https://www.stanfordlawreview.org/online/privacy-and-big-data-its-not-privacy-and-its-not-fair/
Many definitions of fairness are not mutually compatible -> https://arxiv.org/abs/1609.07236

https://medium.com/@mrtz/how-big-data-is-unfair-9aa544d739de
* Even with more data, smaller group will not get classifications that are as good as big groups (there is less data)
* Features that are rare in large groups may not be rare in small groups
* 5% error on aggregate may be 50% error on a small group


Weapons of Math destruction: Cathy O’Neil reveals in this urgent and necessary book, the opposite is true. The models being used today are opaque, unregulated, and uncontestable, even when they’re wrong. Most troubling, they reinforce discrimination: If a poor student can’t get a loan because a lending model deems him too risky (by virtue of his zip code), he’s then cut off from the kind of education that could pull him out of poverty, and a vicious spiral ensues. Models are propping up the lucky and punishing the downtrodden, creating a “toxic cocktail for democracy.” Welcome to the dark side of Big Data.

Approaching fairness http://blog.mrtz.org/2016/09/06/approaching-fairness.html
* Blindness doesn't work since other features can leak stuff like race
* Demogaphic parity: classificaiton should be independent of protected feature
* Demographic parity is fundamentally not aligned with accuracy: For e.g: If I'm Lebanese I'm more likely to enjoy hummus than the general population

So we need to look at other definitions

## Fair ML book

#### Intro
Intro: It's unlikely that we'll get a stamp of approval to say some algorithm is fair
Diversity has different definitions - (filter bubble, diversity of ideas)
There is a difference between fairness in selection and fairness in treatment
Feedback loops - e.g: most content online becomes written by GPT-3 - good luck fixing bias issues hten

#### Classification
Impossibility results of several classification criterion

#### Causality and counterfactuals
Counterfactual easy to understand, the rest of causality (to me not so much)
Remove/change examples or features in the dataset and see if the model output is significantly different

#### Testing discrimination in practice
Most existing disrimnation audits are about testing blindness
Need to pay attention to our causal models to see if there's any sort of unintended spillover actions

##### Discrimnation in NLP in English for African Americans
However, a 2016 study showed that a widely used tool, langid.py, which incorporates a pre-trained model, had substantially more false negatives for tweets written in African-American English (AAE) compared to those written in more common dialectal forms: 13.2% of AAE tweets were classified as non-English compared to 7.6% of “white-aligned” English tweets. AAE is a set of English dialects commonly spoken by black people in the United States (of course, there is no implication that all black people in the United States primarily speak AAE or even speak it at all)For a treatise on AAE, see L.J. Green, African American English: A Linguistic Introduction (Cambridge University Press, 2002). The linguistic study of AAE highlights the complexity and internal consistency of its grammar, vocabulary, and other distinctive features, and refutes the basis of prejudiced views of AAE as inferior to standard English.. The authors’ construction of the AAE and white-aligned corpora themselves involved machine learning as well as validation based on linguistic expertise; we will defer a full discussion to the Measurement chapter. The observed error rate disparity is likely a classic case of underrepresentation in the training data.

This is particularly important if an NLP is deployed in the context of a news ranker, job application screening etc..

#### Measurement
No statistics textbook even talks about this


## General Bias topic

### kate Crawford talk https://www.youtube.com/watch?v=fMym_BKWQzk&t=698s
Technical responses to bias
* Improve accuracy
* Blacklist
* Scrub to neutral
* Demographics or equal representation
* Awareness

2 forms of bias
* Allocation bias: income, easily quantifiable
* Representation: difficult to characterize


### Rachel Thomas talk https://www.youtube.com/watch?v=S-6YGPrmtYc
Image recgognition algorithms don't do well on black people or women
Evaluation bias: SOTA algorithms won't deal well with these bias issues
Using ML to predict prison sentence
Using ML to predict school grades or job recruiting
Racist or Gendered ads and newsfeed content
Measurement bias
Even if bias exists humans, ML bias is even more harmful because its' more scalable
Checklist approach is really what this is getting at, can't really build automated solution for this need to audit
* Accuracy of simple rule based model
* Error rates for different subgroups
* Can the data be audited?
* What bias is in the data


## Model checklist
So recognize that this will be an iterative process, consult with people often and audit often. Follow this checklist for reasonable advice https://arxiv.org/pdf/1803.09010.pdf - of particular interest is making sure that there's diverse representation among scholars who can be best aware of sources of biases that existing scholars may not be

The categories of things to look at are
1. Motivation
2. Composition 
3. Collection process
4. Preprocessing
5. Uses
6. Distribution
7. Maintenace

This problem is made even more challenging since race isn't a static concept over time https://arxiv.org/abs/1912.03593

These bias issues are prevalent accross companies not just a single one https://www.youtube.com/watch?time_continue=262&v=TWWsW1w-BVo&feature=emb_logo


### https://www.callingbullshit.org/case_studies/case_study_criminal_machine_learning.html
Analyzing faces to predict if someone is going to be a criminal is dangerous pseudoscience


## 21 definitions of fairness
https://shubhamjain0594.github.io/post/tlds-arvind-fairness-definitions/


#### Definitions covered
Statistical Bias
Group Fairness
Demographic Parity
Equal Pos. Pred. Value
Equal Neg. Pred Value
Equal FPR
Equal FNR
Accuracy equity
Blindness
Individual fairness
Equal thresholds
Similarity metric
Process fairness (feature rating)
Diversity (various definitions)
Representational harms
Stereotype mirroring/exaggeration
Cross-dataset generalization
Bias in representation learning
Bias amplification

#### There are this many definitions because
Different contexts/applications
Different stakeholders
Impossibility theorems
Any overarching definitions will be inevitably be vacuous
Allocative vs representational harms

Takeaway: think of hte purpose of using some algorithm in production, work with stakeholders to figure out what they really want

## Bias in Healthcare
* https://www.boozallen.com/c/insight/blog/ai-bias-in-healthcare.html

Yet, this advancement brings with it the very real possibility that AI tools, trained with data that reflects historical and contemporary cognitive and societal biases, could unwittingly perpetuate or even amplify bias in healthcare delivery.

Treatment may differ based on race for e.g: people of color are less likely to receive pain medicaiton
Doctors are less likely to do due diligence on a diagnosis if the patient is obese

Academic data tends to be biased toward students that are in academic institutions and are not representative of the wider population

Even though some features are not explicitly racist they could be indirectly racist by normalizing accross features like income. For e.g: the less money spent on your healthcare solution the less likely you are to survive

Regulators are asking healthcare providers for proof that their algorithms are not discrimanotory  or not use them.

There's many competing hypotheses for how to solve this but at a high level you can do counterfactual analysis.
* Train an algorithm on dataset with income
* Train an algorithm on dataset without income
* Look at the diff and see if the racist predictions go away

**Problem Definition**: If the goal is to ensure that AI creates more equitable healthcare solutions than what we have today, then we need better mechanisms to balance its risks and benefits. It will require collaboration between data scientists, healthcare providers, consumers, and regulators to address the complex issues of AI bias; algorithm fairness and accuracy; ethics and safety; and governance and oversight.

In the case of healthcare you want to make sure that people get the best treatment regardless of their race, gender, religious beliefs etc..


## https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6347576/
Some issues around bias in healthcare
1. Some conditions may only exist on some populations
2. Predicting values around hte mean will hurt small populations
3. Certain features may be racist like socioeconomic status

Note to self: As of 2015, about 4.4 million people have sickle cell disease, while an additional 43 million have sickle cell trait.[7][10] About 80% of sickle cell disease cases are believed to occur in Sub-Saharan Africa.[11] It also occurs relatively frequently in parts of India, the Arabian Peninsula, and among people of African origin living in other parts of the world.[

Proposed solutions
1. make sure there's a human in the middle
2. take care in curating datasets and features
3. Impose human values in algorithms at the cost of efficiency - add loss functions for bias and make sure the tradeoff is explicit





## Bias in Language models

## The below debiasing approaches don't raelly work
https://arxiv.org/abs/1903.03862

d is some distance function in embedding space
d(woman, nurse) < d(man, nurse)
man, woman or nurse are all in embedding space

So how we do solve this?

### https://www.aclweb.org/anthology/N19-3002.pdf

Code here https://github.com/BordiaS/language-model-bias

Author proposal
1. Propose a metric to measure bias
2. Propose a regularization strategy to reduce bias

Some notable forms of bias
* Male candidates are preferred in resume screens
* Face detection algorithms work better on white males
* Coreference resolution favors male pronouns

In language a sentence can be biased in two ways
1. Framing bias: This is bad
2. Epistemlogical bias: people *claim* this is good

Both are about describing something or a group of people negatively but one is more subtle

Past approaches
1. Change the dataset: Could randomly change gendered pronouns in dataset or make genders balanced but this work for e.g for stuff like the doctor or nurse distance problem
2. Regularize the model: to remove bias
3. Change embedding: to remove bias (similar to 1)


bias(w) = log(P(w|f) / P(w|m))

We take gendered pairs and the take embedding difference between them in a matrix C then we take the singular value decompsition of this matrix and take the first K columns of the right hand matrix which is claled the gender subspace

Caveat: We additionally observe a perplexity bias tradeoff as a result of the additional bias regularization term. In order to reduce bias, there is a compromise on perplexity. Intuitively, as we reduce bias the perplexity is bound to increase due to the fact that, in an unbiased model, male and female words will be predicted with an equal probability

## Gender subspace
http://papers.nips.cc/paper/6228-man-is-to-computer-programmer-as-woman-is-to-homemaker-debiasing-word-embeddings.pdf
Grandfather and Grandmother have different meanings that you want to keep
Other times, man is used as a verb - e.g: man the ship

So can't do a hard equalize need to soften bias

Note to self: i don't get the first k rows argument for gender subbspace


### https://www.aclweb.org/anthology/P14-2002.pdf
There's all sorts of weird biases in datasets not just race and gender. For e.g, google n-grams predicts more familiarity with technology than other kinds of datasets

# Software
* Google What if tool: https://colab.research.google.com/github/pair-code/what-if-tool/blob/master/WIT_Toxicity_Text_Model_Comparison.ipynb


``` python
config_builder = WitConfigBuilder(test_examples[0:num_datapoints]).set_estimator_and_feature_spec(
    classifier, feature_spec).set_compare_estimator_and_feature_spec(
    classifier2, feature_spec).set_label_vocab(['Under 50K', 'Over 50K'])
a = WitWidget(config_builder, height=tool_height_in_px)
```

# References
* https://fairmlclass.github.io/
* https://fairmlbook.org/
* https://www.aclweb.org/anthology/N19-3002.pdf
* https://medium.com/@eirinimalliaraki/toward-ethical-transparent-and-fair-ai-ml-a-critical-reading-list-d950e70a70ea
* https://www.youtube.com/watch?v=S-6YGPrmtYc
* https://www.youtube.com/watch?v=jIXIuYdnyyk
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6347576/
* https://www.boozallen.com/c/insight/blog/ai-bias-in-healthcare.html
* https://www.aclweb.org/anthology/P14-2002.pdf
* https://twimlai.com/twiml-talk-336-trends-in-fairness-and-ai-ethics-with-timnit-gebru/

