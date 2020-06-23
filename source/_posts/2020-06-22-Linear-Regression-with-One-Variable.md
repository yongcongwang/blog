---
title: Linear Regression with One Variable
categories: algorithm
tags:
  - mechine_learning
mathjax: true
comments: true
date: 2020-06-22 17:08:26
---

## Model Representation
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

## Cost Function
we can measure the accuracy of our hypothesis function by using a **cost function**. The most common cost function is "Squared error function" or called "Mean squared error":
$$
J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i = 1}^{m}(\hat{y_i} - y_i)^2 = \frac{1}{2m} \sum_{i = 1}^{m}(h_{\theta}(x_i) - y_i)^2
$$
The mean is halved $(\frac{1}{2})$ as a convenience for the computation of the gradient descent, as the derivative term of the square function will cancel out the $\frac{1}{2}$ term.

We should try to minimize the cost function to find the best $h$ to predict the output data.

## Gradient Descent
So we have our hypothesis function and we have a way of measuring how well it fits into the data. Now we need to estimate the parameters in the hypothesis function. That's where gradient descent comes in.

We put $\theta_0$ on the $x$ axis and $\theta_1$ on the $y$ axis, with the cost function on the vertical $z$ axis. The points on our graph will be the result of the cost function using our hypothesis with those specific $\theta$ parameters. The goal is to find the very bottom point of the graph.

The gradient descent algorithm is:
$$
\theta_j = \theta_j - \alpha \frac{\partial}{\partial\theta_j}J(\theta_0, \theta_0)
$$

where:
- $j = 0, 1$ represents the feature index number.
- $\alpha$ is called "learning rate" to ensure that the gradient descent algorithm converges in a reasonable time.

## Gradient Descent For Cost Function
We can substitute our cost function and our actual hypothesis function and modify the equation to:
$$
\theta_{0} := \theta_{0} - \alpha\frac{1}{m}\sum_{i = 1}^{m}(h_{\theta}(x_{i}) - y_{i})
$$
$$
\theta_{1} := \theta_{1} - \alpha\frac{1}{m}\sum_{i = 1}^{m}((h_{\theta}(x_{i}) - y_{i})x_{i})
$$
where:
- $m$ is the size of the training set;
- $\theta_{0}$ is a constant that will be changing simultaneously with $\theta_{1}$
- $x_{i}, y_{i}$ are values of the given training set.

With the equation, we can repeat calculating $\theta_{0}$ and $\theta_{1}$ until vonvergence.

This method looks at every example in the entire training set on every step, and is called `batch gradient descent`.
