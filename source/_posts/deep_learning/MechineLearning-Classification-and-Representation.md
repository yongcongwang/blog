---
title: MechineLearning | Classification and Representation
mathjax: true
comments: true
categories:
  - deep_learning
date: 2020-06-29 11:19:12
---

The classification problem is just like the regression problem, except that the values we now want to predict take on only a small number of discrete values. To attempt classification, one method is to use linear regression and map all predictions greater than $0.5$ as $1$ and all less than $0.5$ as $0$. However, this method doesn't work well because classification is not really a linear function.

<!-- more -->

# Hypothesis Representation
We could approach the classification problem ignoring the fact that y is discrete value and use our old linear function to predict y with given x. However, it doesn't make sense for $h_{\theta}(x)$ to take value larger than $1$ or smaller than $0$ when we know that $y \in {0, 1}$. To fix this, we plug $\theta^Tx$ into the `Logistic Function`.

`Logistic Function`(or `Sigmoid Function`) is defined as:
$$
h_{\theta}(x) = g(\theta^Tx)
$$

$$
z = \theta^Tx
$$

$$
g(z) = \frac{1}{1 + e^{-z}}
$$

more details can be found [here](https://en.wikipedia.org/wiki/Logistic_function).
The function $g(z)$ maps any real number to the $(0, 1)$ interval, making it useful for transforming an arbitrary-valued function into a function better suited for classification.

$h_{\theta}(x)$ will give us the probability that our output is $1$. For example, $h_{\theta}(x) = 0.7$ gives us the probability of $0.7$ that our output is $1$.
$$
h_{\theta}(x) = P(y = 1 |x; \theta) = 1 - P(y = 1 | x ; \theta)
$$

$$
P(y = 1 |x; \theta) + 1 - P(y = 1 | x ; \theta) = 1
$$

# Decision Boundary
In order to get our discrete $0 or 1$, we can translate the output of the hypothesis function as follows:
$$
h_{\theta}(x) \ge 0.5 \to y = 1
$$
$$
h_{\theta}(x) \le 0.5 \to y = 0.5
$$

The way our logistic function $g$ behaves when its input is greater than or equal to zero, its output is greater than or equal to $0.5$:
$$
\begin{array}{lcl}
g(z) \ge 0.5 \\\\
\mbox{if } z \ge 0
\end{array}
$$

So if the input to $g$ is $\theta^TX$, then that means:
$$
h_{\theta}(x) = g(\theta^Tx) \ge 0.5
$$
when
$$
\theta^Tx \ge 0
$$

From these statements we can now say:
$$
\theta^Tx \ge 0 \to y = 1
$$
$$
\theta^Tx \le 0 \to y = 0
$$

The `decision boundary` is the line that separates the area where $y = 0$ and where $y = 1$. It is created by our hypothesis function.

# Cost Function
We cannot use the same cost function that we use in linear regression because the Logistic Function will cause the output to be wavy, causing many local optima. In other words, it isn't a convex function.

Instead, our cost function for logistic regression looks like:
$$
\begin{align}
J(\theta) & = \frac{1}{m}\sum_{i=1}^{m}Cost(h_{\theta}(x^i), y^i) \\\\
Cost(h_{\theta}(x^i), y^i) & = -log(h_{\theta}(x)) & \mbox{ if } y = 1 \\\\
Cost(h_{\theta}(x^i), y^i) & = -log(1 - h_{\theta}(x)) & \mbox{ if } y = 0
\end{align}
$$
When $y = 1$, we get the following plot for $J(\theta)$ vs $h_{\theta}(x)$:
```C++

^      X        y = 1
|      XX
|       X
|       XX
|        XX
|         XX
|          XX
|           XXX
|             XX
|               XX
|                XXX
|                  XXX
|                    XXX
|                      XX
|                        XXX
|                          XXX
|                             XXX 
+-------------------------------XX+----------->
0            h(x)                 1
```

Similarly, when $y = 0$, we get the following plot for $J(\theta)$ vs $h_{\theta}(x)$:

```C++
^               y = 0
|
|
|
|                             XX
|                             XX
|                            XX
|                           XX
|                          XX
|                       XXX
|                    XXXX
|                  XXX
|               XXX
|             XXX
|          XXX
|      XXXX
| XXXXX
XX--------------------------------+----------->
0            h(x)                 1
```

$$
\begin{align}
Cost(h_{\theta}(x), y) & = 0 & \mbox{if } h_{\theta}(x) = y & \\\\
Cost(h_{\theta}(x), y) & \to \infty & \mbox{if }  y = 0 \mbox{ and } h_{\theta}(x) = 1 \\\\
Cost(h_{\theta}(x), y) & \to \infty & \mbox{if }  y = 1 \mbox{ and } h_{\theta}(x) = 0
\end{align}
$$

## Simplified Cost Function 
We can compress our cost function's two conditianal cases into one case:
$$
Cost(h_{\theta}(x), y) = -ylog(h_{\theta}(x)) - (1 - y) log(1 - h_{\theta}(x))
$$

Then the entire const function is as follows:
$$
J(\theta) = -\frac{1}{m} \sum_{i = 1}^m[y^ilog(h_{\theta}(x^i)) + (1 + y^i)log(1 - h_{\theta}(x^i))]
$$

A vectorized implementation is:
$$
\begin{align}
h & = g(X\theta) \\\\
J(\theta) & = \frac{1}{m} \cdot (-y^Tlog(h) - (1 - y)^Tlog(1 - h))
\end{align}
$$

## Gradient Descent
The general form of gradient descent is:
$$
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j}J(\theta)
$$

We can work out the derivative part using calculus to get:
$$
\theta_j := \theta_j - \frac{\alpha}{m} \sum_{i=1}{m}(h_{\theta}(x^i) - y^i)x_j^i
$$
A vectorized implementation is:
$$
\theta := \theta - \frac{\alpha}{m} X^T(g(X\theta) - \overrightarrow{y})
$$

## Advanced Optimization
Instead of gradient descent,
- "Conjugate gradient",
- "BFGS",
- "L-BFGS"
are more sophisticated, faster ways to optimize $\theta$.
You can use a existed libaray to apply these mathods.

# Multiclass Classification: One-vs-all
Now we will approach the classification of data when we have more than two . Instead of $y = {0, 1}$, we will expand our definition so that $y = {0, 1, ..., n}$.

Since $y = {0, 1, ..., n}$, we divide our problem into $n+1$ ($+1$ because the index start at 0) binary classification problems. In each one, we predict the probability that $y$ is a member of one of our classes.
$$
\begin{align}
y & \in {0, 1, ..., n} \\\\
h_{\theta}^{(0)}(x) & = P(y = 0 | x; \theta) \\\\
h_{\theta}^{(1)}(x) & = P(y = 1 | x; \theta) \\\\
h_{\theta}^{(2)}(x) & = P(y = 2 | x; \theta) \\\\
\cdots \\\\
h_{\theta}^{(n)}(x) & = P(y = n | x; \theta) \\\\
prediction & = \max_i(h_{\theta}^{(i)}(x))
\end{align}
$$

We are basically choosing one class and then lumping all the others into a single second class. We do this repeatedly, applying binary logistic regression to each case, and then use the hypothesis that returned the highest value as prediction.

To sumerize:
- Train a logistic regression classifier $h_{\theta}(x)$ for each class to predict the probability that $y = i$;
- To make a prediction on a new $x$, pick the class that maximized $h_{\theta}(x)$.
