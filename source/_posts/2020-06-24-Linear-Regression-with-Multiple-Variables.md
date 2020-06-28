---
title: Linear Regression with Multiple Variables
categories: algorithm
tags:
  - mechine_learning
mathjax: true
comments: true
date: 2020-06-24 14:00:03
---

# Multiple Features
Linear regression with multiple variables is also known as `multivariate linear regression`.
The notation for equations where we can have any number of input variables is as below:
- $x_{j}^i$ is the value of feature $j$ in the $ith$ training example;
- $x^{i}$ is the input (features) of the $ith$ training exmaple;
- $m$ is the number of training examples;
- $n$ is the number of features.

<!-- more -->

The multivariable form of the hepothesis function with multiple features is as follows:
$$
h_{\theta}(x) = \theta_{0} + \theta_{1}x_{1} + \theta_{2}x_{2} + \theta_{3}x_{3} + ... + \theta_{n}x_{n}
$$

Using the definition of matrix multiplication, our multivariable hypothesis function can be concisely represented as:
$$
h_{\theta}(x) = \begin{bmatrix} \theta_0 \theta_1 \cdots \theta_n \end{bmatrix} \begin{bmatrix} x_0 \\\\ x_1 \\\\ \vdots \\\\ x_n \end{bmatrix} = \theta^Tx
$$

# Gradient Descent for Multiple Variables
The gradient descent equation is the same form, we just have to repeat it for our $n$ feature:
$$
\begin{cases}
\theta_{0} := \theta_0 - \alpha\frac{1}{m}\sum_{i=1}^m(h_{\theta_0}(x^i) - y^i) \cdot x_0^i \\\\
\theta_1 := \theta_1 - \alpha\frac{1}{m}\sum_{i=1}^m(h_{\theta_1}(x^i) - y^i) \cdot x_1^i \\\\
\theta_2 := \theta_2 - \alpha\frac{2}{m}\sum_{i=2}^m(h_{\theta_2}(x^i) - y^i) \cdot x_2^i \\\\
...
\end{cases}
$$
In other words:
$$
\theta_j := \theta_j - \alpha\frac{1}{m}\sum_{i=1}^m(h_{\theta}(x^i) - y^i) \cdot x_j^i
$$
where:
- $j = 0, 1, ..., n$

## Feature Scaling to Speed up Gradient Descent
We can speed up gradient descent by having each of our input values in roughly the same range. This is because $\theta$ will descend quickly on small ranges and slowly on large ranges, and so will oscillate inefficiently down to the optimum when the variables are very uneven.
The way to prevent this is to modify the ranges of our input variables so that they are all roughly the same. Ideally:
$$
-1 <= x_i <= 1
$$
or
$$
-0.5 <= x_i <= 0.5
$$

These are not exact requirements, we are only trying to speed things up. The goal is to get all input variables into roughly one of these ranges, give or take a few.

Two techiques to help with this are:
- feature scaling: involves diving the input values by the range of the input variable, resulting in a new range of just $1$;
- mean normalization: involves subtracing the average value for an input variable from the values for that input variable, resulting in a new average value for the input variable of just zero.
To impliment both of these techniques, adjust your input values as shown in this formula:
$$
x_i := \frac{x_i - \mu_i}{s_i}
$$
where:
- $\mu_i$ is the average of all the values for feature;
- $s_i$ is the range of values($max - min$).  

## Choosing Correct Learning Rate
To debug gradient descent, we can make a plot with number of iterations on the x-axis. Now plot the cost function $J(\theta)$ over the number of iterations of gradient descent. If $J(\theta)$ increases, then you probably need to decrease $\alpha$.
The learning rate effects the convergence of the $J(\theta)$:
- $\alpha$ is too small: slow convegence;
- $\alpha$ is too large: may not decrease on every iteration and shus may not converge.

## Improve features and hypothesis
We can improve our features and the form of our hypothesis function in a couple different ways.

### Feature
We can combine multiple features into one. For example, we can combine $x_1$ and $x_2$ into a new feature $x_3$ by taking $x_3 = x_1 * x_2$.

### Hypothesis Function
Our hypothesis function need not to be linear (a straight line) if that does not fit the data well.
We can change the behavior or curve of our hypothesis function by making it a:
- quadratic;
- cubic;
- square root
function.

One important thing to keep in mind is, if you choose your features this way, the feature scaling becomes very important.

# Normal Equation for Multiple Variables
Gradient descent gives one way to solve the minimizing $J$, the `normal equation` method is another way of doing so. In this way, we will minimizing $J$ by explicitly taking its derivatives with respect to the $\theta_j$ and set them to $0$. This allows us to find the optimum theta without iteration. The normal equation is given below:
$$
\theta = (X^TX)^{-1}X^Ty
$$

Following is a comparison of gradient descent and the normal equation:

| Gradient Descent | Normal Equation |
| ---------------- | --------------- |
| Need to choose $\alpha$ | No need to choose $\alpha$ |
| Need many iterations | No need to iterate |
| Time complexity $O(kn^2)$ | Time complexity $O(n^3)$, need to calculate inverse of $X^TX$ |
| Works well when $n$ is large | Slow if $n$ is very large |

With the normal equation, computing the inversion has comlexity $O(n^3)$. So if we have a very large number of features, the normal equation will be slow. In practice, when $n$ exceeds $10000$ it might be a good time to go from normal solution to an iterative process.

## Noninvertibility
The normal equation used $X^TX$ to calculate variables, but $X^TX$ might be "noninvertible", the common causes may be:
- Redundant features, where two features are very closely related;
- Too many features(e.g. $m <= n$), in this case, delete some featues or use "regularization".
