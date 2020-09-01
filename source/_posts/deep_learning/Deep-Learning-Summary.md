---
title: Deep Learning Summary
mathjax: true
categories:
  - deep_learning
date: 2020-08-26 19:49:55
---

This page contains my personal notes and summaries on [DeepLearning.ai](https://deeplearning.ai) specialization courses. [DeepLearning.ai](https://deeplearning.ai) contains five courses which can be taken on [Coursera](https://www.coursera.org/specializations/deep-learning):
- Neural Network and Deep Learning;
- Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization;
- Structuring Machine Learning Projects;
- Convolutional Neural Networks;
- Sequence Models.
<!-- more -->
# Neural Network and Deep Learning
## Introduce to deep learning
### What is a Neural Network
![nn](https://scx1.b-cdn.net/csz/news/800/2018/2-whyareneuron.jpg)

At a very simple level, neurons are basically computational units that take inputs(dendrites) as electrical inputs(called "spikes") that are channeled to outputs(axons). A single neuron will calculate weighted sum of input($W.T \cdot X$) and we can set a threshold to predict output in a perceptron. If weighted sum of input across the threshold, perceptron fires and if not then perceptron doesn't predict.

The disadvantage of perceptron is that it only outputs binary values. To make output of perceptron flips we add a bias, here comes: $W.T \cdot X + b$. We need some system which can modify the output slightly accordding to small change in weight and bias, here comes activation functions($g(X.T \cdot X + b)$).

`Sigmoid` is a kind of activation functions, we can make slight change in output with sigmoid function, and the single neuron with sigmoid activation function will act as `Logistic Regression`.

`ReLU` which stands for rectified linear unit, is the most popular activation function right now that makes deep neural network trains faster.

### Supervised learning with neural networks
There are different types of neural networks for supervised learning:
- `CNN`(Convolutional Neural Network) is useful in computer vision;
- `RNN`(Recurrent Neural Network) is useful in speech recognition or NLP(Nature Language Process);
- `Standard NN` is useful for structured data;
- Hybrid/custom NN or a Collection of NNs types

### Why is deep learning taking off
![scale drives deep learning progress](/images/2020/deep_learning/scale_drive_deep_learning_progress.png)

Deep learning is taking off for 3 reasons:
1. Data scale:
 - For small data NN can performs as traditional algorithms like Linear regression or SVM(Support vector mechine);
 - For bigger data a small NN performs better than traditional algos;
 - For really big data, a large NN is better than middle NN that is better than small NN;
 - Hopefully we have a lot of data because the world is uing the computer a little bit more.
2. Computation:
 - GPUs;
 - Powerful CPUs;
 - Distributed computing;
 - ASICs.
3. Algorithm:
 - Creative algorithms have appeared that changed the way NN works: For example, using `ReLU` is so much better than using `Sigmoid` function in training a NN because it helps with the vanishing gradient problem.




## Neural Network

