# Deep Learning and the Game of Go

* Book starts with a foreword by the alphaGo team that highly recommends the book.
* Authors built an open source engine called BetaGo that combines RL and Monte Carlo Tree Search.
* Book builds up towards one key idea, how to make ALpha Go and Alpha Go Zero work


## Chapter 1: Towards Deep Learning a Maching learing introduction
* ML vs traditional programming
* ML as a subfield of AI including logic systems, expert systems and fuzzy stems
* Don't use ML when there are other closed form solutions or simple heuristics work better or when you expect perfect accuracy
* How to model a linear function
* Brief summary of libraries like NumPy, TensorFlow, Keras
* Basic explanation of Supervised learning and examples that relate to Go
    - Given games 
    - Given a board position, how likely are you to win from that state
* Unsupervised learning
    - Find units that belong to the same group
* Reinforcement learning: attempt task, evaluate success, generate training data and improve agent
* Deep Learning: each layer models higher order concepts and allows you learn representations
* DL is a good choice when
    - Data is unstructured
    - You have large amounts of data
    - You have plenty of computing power or plenty of time
* DL is a bad choice
    - When model is essentially somehting like a spreadsheet
    - You want an interpretable model you can debug

## Chapter 2: Go as a machine learning problem