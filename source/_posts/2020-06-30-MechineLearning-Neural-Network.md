---
title: MechineLearning | Neural Networks
categories: algorithm
tags:
  - mechine_learning
  - neural network
mathjax: true
comments: true
date: 2020-06-30 10:36:21
---

# Model Representation
![neuron](https://scx1.b-cdn.net/csz/news/800/2018/2-whyareneuron.jpg)
In this chapter, we will represent a hypothesis function using neural networks. At a very simple level, neurons are basically computational units that take inputs(dendrites) as electrical inputs(called "spikes") that are channeled to outputs(axons). In our model, our dendrites are like the input features $x_1 \cdots x_n$ and the output is the result of our hypothesis function. In this model our $x_0$ input node is sometimes called the "bias unit". It is always euqal to $1$. In neural networks, we use the same logistic function as in classification, $\frac{1}{1+e^{-\theta^Tx}}$, yet we sometimes call it a sigmoid(logistic) activation function. In this situation, our "theta" parameters are sometimes called "weights".
<!-- more -->
![neural network](https://www.oracle.com/a/tech/img/art-neural-network-image001.png)

Visually, a simplistic representation looks like:
$$
\begin{bmatrix}
x_0 \\\\
x_1 \\\\
x_2
\end{bmatrix}
\to \mbox{[ ]} \to h_{\theta}(x)
$$

Our input nodes(layer 1), also known as the "input layer", go into another node(layer 2), which finally outputs the hypothesis function, known as "output layer".
We can have intermediate layers of nodes between "input layers" and "output layers" called the "hidden layers".
In this example, we label these intermediate or "hidden" layer nodes $a_0^2 \cdots an_n^2$ and call them "activation units".
$$
a_i^{(j)} = \mbox{"activation" of unit i in layer j}
$$
$$
\Theta^{(j)} = \mbox{matrix of weights controlling function mapping from layer j to layer j + 1}
$$

If we have hidden layer, it would like:
$$
\begin{bmatrix} x_0 \\\\ x_1 \\\\ x_2 \\\\ x_3 \end{bmatrix} \to 
\begin{bmatrix} a_0^{(2)} \\\\ a_1^{(2)} \\\\ a_2^{(2)} \\\\ a_3^{(2)} \end{bmatrix} \to
h_{\theta}(x)
$$

The values for each of the "activation" nodes is obtained as follows:
$$
\begin{bmatrix}
\Theta_{10}^{(1)} & \Theta_{11}^{(1)} & \Theta_{12}^{(1)} & \Theta_{13}^{(1)} \\\\
\Theta_{20}^{(1)} & \Theta_{21}^{(1)} & \Theta_{22}^{(1)} & \Theta_{33}^{(1)} \\\\
\Theta_{30}^{(1)} & \Theta_{31}^{(1)} & \Theta_{32}^{(1)} & \Theta_{33}^{(1)} 
\end{bmatrix}
\begin{bmatrix}
x_0 \\\\
x_1 \\\\
x_2 \\\\
x_3
\end{bmatrix}
=
\begin{bmatrix}
a_1^{(2)} \\\\
a_2^{(2)} \\\\
a_3^{(2)}
\end{bmatrix}
$$
$$
h_{\Theta}^{(x)} = a_1^{(3)} = g(
\begin{bmatrix}
\Theta_{10}^{(2)} & \Theta_{11}^{(2)} & \Theta_{12}^{(2)} & \Theta_{13}^{(2)} 
\end{bmatrix}
\begin{bmatrix}
a_0^{(2)} \\\\
a_1^{(2)} \\\\
a_2^{(2)} \\\\
a_3^{(2)}
\end{bmatrix}
)
$$

This is saying that we compute our activation nodes by using a $3 \times 4$ matrix of parameters. We apply each row of the parameters to our inputs to obtain the value for one activation node.
Our hypothesis output is the logistic function applied to the sum of the values of our activation nodes, which have been multiplied by yet another another parameter matrix $\Theta^{(2)}$ containing the weights for our second layer of nodes.
Each layer gets its own matrix of weights, $\Theta^{(j)}$.
The dimension of these marices of weights is determined as follows:
> If network has $s_j$ units in layer $j$ and $s_{j + 1}$ in layer $j + 1$, then $\Theta_0^{j}$ will be of dimension $s_{j + 1} \times (s_j + 1)$.

The $+1$ comes from the addition in $\Theta^{(j)}$ of the "bias node" $x_0$ and $\Theta_0^{(j)}$. In other words, the output nodes will not include the bias node while the input nodes will.

# Application

## Implement A Logical Operator
A simple example of applying neural networks is by predicting $x_1 \mbox{ AND } x_2$ which is the logical `and` operator and is only true if both $x_1$ and $x_2$ are $1$.
The graph of our functions will look like:
$$
\begin{bmatrix}
x_0 \\\\
x_1 \\\\
x_2
\end{bmatrix}
\to 
\begin{bmatrix}
g(z^{(2)})
\end{bmatrix}
\to
h_{\Theta}^{(x)}
$$

Remember that $x_0$ is our bias variable and is always $1$.
Let's set our first $\Theta$ matrix as:
$$
\Theta^{(1)} = \begin{bmatrix} -30 & 20 & 20 \end{bmatrix}
$$

This will case the output of our hypothesis to only be positive if both $x_1$ and $x_2$ are $1$. In other words:
$$
h_{\Theta}(x) = g(-30 + 20x_1 + 20x_2)
$$
And $g(z)$ is the sigmoid fucntion, it's $1$ if $z > 0$, and $0$ if $z < 0$.
So the result is:

| $x_1$ | $x_2$ | g(z) | $h_{\Theta}(x)$ |
| ----- | ----- | ---- | --------------- |
| 0     | 0     | g(-30) | 0             |
| 0     | 1     | g(-10) | 0             |
| 1     | 0     | g(-10) | 0             |
| 1     | 0     | g(10) | 1              |

So we have constructed one of the fundamental operation in computers by using a small neural network rather than an actual `AND` gate. Neural network can also be used to simulate all the other logical gates.

## Implement A Complex Logical Operator
The $\Theta^{(1)}$ matrices for `AND`, `NOR` and `OR` are:
- AND:
$$
\Theta^{(1)} = \begin{bmatrix} -30 & 20 & 20 \end{bmatrix}
$$

- NOR:
$$
\Theta^{(1)} = \begin{bmatrix} 10 & -20 & -20 \end{bmatrix}
$$

- OR:
$$
\Theta^{(1)} = \begin{bmatrix} -10 & 20 & 20 \end{bmatrix}
$$

We can combine these to get the `XNOR` logical operator(which gives 1 if $x_1$ and $x_2$ are both 0 or both 1).
$$
\begin{bmatrix}
x_0 \\\\
x_1 \\\\
x_2
\end{bmatrix}
\to
\begin{bmatrix}
a_1^{(2)} \\\\
a_2^{(2)}
\end{bmatrix}
\to
\begin{bmatrix}
a^{(3)}
\end{bmatrix}
\to
h_{\Theta}(x)
$$
For the transition between the second and third layer, we'll use a $\Theta^{(2)}$ matrix that combines the values for AND and NOR:
$$
\Theta^{(1)} = 
\begin{bmatrix}
-30 & 20 & 20 \\\\
10 & -20 & -20
\end{bmatrix}
$$

For the transition between the second and third layer, we'll use a $\Theta^{(2)}$ matrix that uses the value for OR:
$$
\Theta^{(2)} = \begin{bmatrix} -10 & 20 & 20 \end{bmatrix}
$$

Let's write out the values for all our nodes:
$$
a^{(2)} = g(\Theta^{(1)} \cdot x)
$$
$$
a^{(3)} = g(\Theta^{(2)} \cdot a^{(2)})
$$
$$
h_{\Theta}(x) = a^{(3)}
$$
The neural networks is like this:
![xnor](http://assets.processon.com/chart_image/5efb329f07912929cb67f6e1.png)
