---
title: Deep Learning Summary
mathjax: true
categories:
  - deep_learning
date: 2020-08-26 19:49:55
---

# Introduce to deep learning
## What is a Neural Network
![nn](https://scx1.b-cdn.net/csz/news/800/2018/2-whyareneuron.jpg)
At a very simple level, neurons are basically computational units that take inputs(dendrites) as electrical inputs(called "spikes") that are channeled to outputs(axons). A single neuron will calculate weighted sum of input($W.T \cdot X$) and we can set a threshold to predict output in a perceptron. If weighted sum of input across the threshold, perceptron fires and if not then perceptron doesn't predict.
The disadvantage of perceptron is that it only outputs binary values. To make output of perceptron flips we add a bias, here comes: $W.T \cdot X + b$. We need some system which can modify the output slightly accordding to small change in weight and bias, here comes activation functions($g(X.T \cdot X + b)$).
`Sigmoid` is a kind of activation functions, we can make slight change in output with sigmoid function, and the single neuron with sigmoid activation function will act as `Logistic Regression`.
`ReLU` which stands for rectified linear unit, is the most popular activation function right now that makes deep neural network trains faster.

## Supervised learning with neural networks
There are different types of neural networks for supervised learning:
- `CNN`(Convolutional Neural Network) is useful in computer vision;
- `RNN`(Recurrent Neural Network) is useful in speech recognition or NLP(Nature Language Process);
- `Standard NN` is useful for structured data;
- Hybrid/custom NN or a Collection of NNs types

## Why is deep learning taking off

# Neural Network

<!-- more -->
