---
title: Model Representation
categories: algorithm
tags:
  - algorithm
mathjax: true
comments: true
date: 2020-06-22 14:16:32
---

To establish notation for future use, we use:
- $x_i$ to denote the "input" variables(also called input features);
- $y_i$ to denote the "output" variables we are trying to predict.

<!-- more -->
A pair $(x_i, y_i)$ is called a training example and a list of training example is called a training set.

We also use:
- $X$ to denote the space of input values;
- $Y$ to denote the space of output values;

To describe the supervised learning problem more formally, our goal is, given a training set, to learn a function $h: X -> Y$ so that $h(x)$ is a "good" predictor for the corresponding value of $y$. For history reason, the function $h$ is called a hypothesis. The process is like this:
```C++
  +----------------+
  |                |
  |  Training set  |
  |                |
  +-------+--------+
          |
          |
          |
  +-------v--------+
  |                |
  |  Learning      |
  |  algorithm     |
  +-------+--------+
          |
          |
          |
       +--v--+
       |     |
x +---->  h  +-----> y
       |     |
       +-----+
```
