---
title: MechineLearning | Neural Networks
categories: algorithm
tags:
  - mechine learning
  - neural network
mathjax: true
comments: true
date: 2020-06-30 10:36:21
---

# Model Representation
![neuron](https://scx1.b-cdn.net/csz/news/800/2018/2-whyareneuron.jpg)
In this chapter, we will represent a hypothesis function using neural networks. At a very simple level, neurons are basically computational units that take inputs(dendrites) as electrical inputs(called "spikes") that are channeled to outputs(axons). In our model, our dendrites are like the input features $x_{1} \cdots x_{n}$ and the output is the result of our hypothesis function. In this model our $x_{0}$ input node is sometimes called the "bias unit". It is always euqal to $1$. In neural networks, we use the same logistic function as in classification, $\frac{1}{1+e^{-\theta^Tx}}$, yet we sometimes call it a sigmoid(logistic) activation function. In this situation, our "theta" parameters are sometimes called "weights".
<!-- more -->
![neural network](https://www.oracle.com/a/tech/img/art-neural-network-image001.png)

Visually, a simplistic representation looks like:
$$
\begin{bmatrix}
x_{0} \\\\
x_{1} \\\\
x_{2}
\end{bmatrix}
\to \mbox{[ ]} \to h_{\theta}(x)
$$

Our input nodes(layer 1), also known as the "input layer", go into another node(layer 2), which finally outputs the hypothesis function, known as "output layer".
We can have intermediate layers of nodes between "input layers" and "output layers" called the "hidden layers".
In this example, we label these intermediate or "hidden" layer nodes $a_{0}^2 \cdots an_{n}^2$ and call them "activation units".
$$
a_{i}^{(j)} = \mbox{"activation" of unit i in layer j}
$$
$$
\Theta^{(j)} = \mbox{matrix of weights controlling function mapping from layer j to layer j + 1}
$$

If we have hidden layer, it would like:
$$
\begin{bmatrix} x_{0} \\\\ x_{1} \\\\ x_{2} \\\\ x_{3} \end{bmatrix} \to 
\begin{bmatrix} a_{0}^{(2)} \\\\ a_{1}^{(2)} \\\\ a_{2}^{(2)} \\\\ a_{3}^{(2)} \end{bmatrix} \to
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
x_{0} \\\\
x_{1} \\\\
x_{2} \\\\
x_{3}
\end{bmatrix}
=
\begin{bmatrix}
a_{1}^{(2)} \\\\
a_{2}^{(2)} \\\\
a_{3}^{(2)}
\end{bmatrix}
$$
$$
h_{\Theta}^{(x)} = a_{1}^{(3)} = g(
\begin{bmatrix}
\Theta_{10}^{(2)} & \Theta_{11}^{(2)} & \Theta_{12}^{(2)} & \Theta_{13}^{(2)} 
\end{bmatrix}
\begin{bmatrix}
a_{0}^{(2)} \\\\
a_{1}^{(2)} \\\\
a_{2}^{(2)} \\\\
a_{3}^{(2)}
\end{bmatrix}
)
$$

This is saying that we compute our activation nodes by using a $3 \times 4$ matrix of parameters. We apply each row of the parameters to our inputs to obtain the value for one activation node.
Our hypothesis output is the logistic function applied to the sum of the values of our activation nodes, which have been multiplied by yet another another parameter matrix $\Theta^{(2)}$ containing the weights for our second layer of nodes.
Each layer gets its own matrix of weights, $\Theta^{(j)}$.
The dimension of these marices of weights is determined as follows:
> If network has $s_{j}$ units in layer $j$ and $s_{j + 1}$ in layer $j + 1$, then $\Theta_{0}^{j}$ will be of dimension $s_{j + 1} \times (s_{j} + 1)$.

The $+1$ comes from the addition in $\Theta^{(j)}$ of the "bias node" $x_{0}$ and $\Theta_{0}^{(j)}$. In other words, the output nodes will not include the bias node while the input nodes will.

# Application

## Implement A Logical Operator
A simple example of applying neural networks is by predicting $x_{1} \mbox{ AND } x_{2}$ which is the logical `and` operator and is only true if both $x_{1}$ and $x_{2}$ are $1$.
The graph of our functions will look like:
$$
\begin{bmatrix}
x_{0} \\\\
x_{1} \\\\
x_{2}
\end{bmatrix}
\to 
\begin{bmatrix}
g(z^{(2)})
\end{bmatrix}
\to
h_{\Theta}^{(x)}
$$

Remember that $x_{0}$ is our bias variable and is always $1$.
Let's set our first $\Theta$ matrix as:
$$
\Theta^{(1)} = \begin{bmatrix} -30 & 20 & 20 \end{bmatrix}
$$

This will case the output of our hypothesis to only be positive if both $x_{1}$ and $x_{2}$ are $1$. In other words:
$$
h_{\Theta}(x) = g(-30 + 20x_{1} + 20x_{2})
$$
And $g(z)$ is the sigmoid fucntion, it's $1$ if $z > 0$, and $0$ if $z < 0$.
So the result is:

| $x_{1}$ | $x_{2}$ | g(z) | $h_{\Theta}(x)$ |
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

We can combine these to get the `XNOR` logical operator(which gives 1 if $x_{1}$ and $x_{2}$ are both 0 or both 1).
$$
\begin{bmatrix}
x_{0} \\\\
x_{1} \\\\
x_{2}
\end{bmatrix}
\to
\begin{bmatrix}
a_{1}^{(2)} \\\\
a_{2}^{(2)}
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
![xnor](https://github.com/yongcongwang/images/blob/master/blog/2020/3layer_network.png?raw=true)

## Multiclass Classification
To classify data into multiple classes, we let our hypothesis function return a vector of values. We still use the `One-vs-all` method.
For example, if we want to classify our data into one of four categories, we can define our set of resulting classes as:
$$
y^{(i)} = 
\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \end{bmatrix}, 
\begin{bmatrix} 0 \\\\ 1 \\\\ 0 \\\\ 0 \end{bmatrix}, 
\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 0 \end{bmatrix}, 
\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 1 \end{bmatrix}
$$

Each $y^{(i)}$ represents a different image conrresponding to either class 1, class 2, class 3 or class 4. The inner layers, each provide us with some new information which leads to our final hypothesis function. The step looks like:

$$
\begin{bmatrix} x_{0} \\\\ x_{1} \\\\ x_{2} \\\\ \cdots \\\\ x_{n} \end{bmatrix} \to
\begin{bmatrix} a_{0}^{(2)} \\\\ a_{1}^{(2)} \\\\ a_{2}^{(2)} \\\\ \cdots \\\\ x_{n}^{(2)} \end{bmatrix} \to
\begin{bmatrix} a_{0}^{(3)} \\\\ a_{1}^{(3)} \\\\ a_{2}^{(3)} \\\\ \cdots \\\\ x_{n}^{(3)} \end{bmatrix} \to
\cdots \to
\begin{bmatrix} h_{\Theta1}(x) \\\\ h_{\Theta2}(x) \\\\ h_{\Theta3}(x) \\\\ h_{\Theta4}(x) \end{bmatrix}
$$

Our resulting hypothesis for one set of inputs may look like:
$$
h_{\Theta}(x) = 
\begin{bmatrix}
0 \\\\
1 \\\\
0 \\\\
0
\end{bmatrix}
$$

# Cost Function
Let's define a few variables that we will need to use:
- $L$: total number of layers int the network;
- $s_{l}$: number of units(not counting bias unit) in layer $l$;
- $K$: number of output units/classes.

In neural networks, we may have many output nodes, we donate $h_{\Theta}(x)\_{k}$ as being a hypothesis that results in the $k^{th}$ output.
Our cost function for neural networks is going to be a generalization of the one we used for logistic function. Recall that the cost function for regularized logistic regression was:
$$
J(\Theta) = -\frac{1}{m}\sum_{i=1}^{m}[y^{(i)}log(h_{\theta}(x^{(i)})) + (1 - y^{(i)})log(1 - h_{\theta}(x^{(i)}))] + \frac{\lambda}{2m} \sum_{j=1}^{n}\theta_{j}^{2}
$$

For neural networks, it is going to be silightly more complicated:
$$
J(\Theta) = -\frac{1}{m}\sum_{i=1}^{m}\sum_{k=1}^{K}[y_{k}^{(i)}log(h_{\Theta}(x^{(i)})\_k) + (1-y_{k}^{(i)})log(1 - (h_{\Theta}(x^{(i)})\_k)] + \frac{\lambda}{2m}\sum_{l=1}^{L-1}\sum_{i=1}^{s_{l}}\sum_{j=1}^{s_{l+1}}(\Theta_{j,i}^{(l)})^{2}
$$
We have added a few nested summations to account for our multiple output nodes. In the first part of the equation, before the square brackets, we have an additional nested summation that loops through the number of output nodes.
In the regularization part, after the square brackets, we must account for multiple theta matrices. The number of colums in our current theta matrix is equal to the number of nodes in our current layer(including the bias unit). The number of rows in our current theta matrix is equal to the nubmer of node in the next layer(excluding the bias unit). As before with logistic regression, we suqare every term.

## Backpropagation Algorithm
"BackPropagation" is neural-network terminology for minimizing our cost function, just like what we were doing with gradient descent in logistic and linear regression. Our goal is to compute:
$$
\min_{\Theta}J(\Theta)
$$

That is, we want to minimize our cost function $J$ using an optimal set of parameters in $\Theta$. In this section we'll look at the equations we used to compute the partial derivative of $J(\Theta)$:
$$
\frac{\partial}{\partial\Theta_{i,j}^{(l)}}J(\Theta)
$$

To do so:
1. Given training set ${(x^{(1), y^{(1)}}) \cdots (x^{(m)}, y^{(m)})}$,
 - Set $\Delta_{i, j}^{(l)} := 0$ for all $(l, i, j)$(hence you end up having a matrix full of zeros)
2. For training example $t = 1 \to m$:
 1. Set $a^{(1)} := x^{(t)}$
 2. Perform `forward propagation` to compute $a^{(l)}$ for $l=2,3,\cdots,L$
 ![forward propagation](https://github.com/yongcongwang/images/blob/master/blog/2020/forward_propagation.png?raw=true)
 $$
 \begin{array}{lcl}
 a^{(1)} & = & x \\\\
 z^{(2)} & = & \Theta^{(1)}a^{(1)} \\\\
 a^{(2)} & = & g(z^{(2)}) \quad (add \quad a_{0}^{(2)}) \\\\
 z^{(3)} & = & \Theta^{(2)}a^{(2)} \\\\
 a^{(3)} & = & g(z^{(3)}) \quad (add \quad a_{0}^{(3)}) \\\\
 z^{(4)} & = & \Theta^{(3)}a^{(3)} \\\\
 a^{(4)} & = & h_{\Theta}(x) = g(z^{(4)}) \\\\
 \end{array}
 $$
 3. Using $y^{(t)}$ to compute $\delta^{(L)} = a^{(L)} - y^{(t)}$.
 - Where $L$ is our total number of layers and $a^{(L)}$ is the vector of outputs of the activation units for the last layer. So our "error values" for the last layer are simply the differences of our actual results in the last layer and the correct outputs in $y$. To get the $\delta$ values of the layers before the last layer, we can use an equation that steps us back from right to left.
 4. Computing $\delta^{(L-1)},\delta^{(L-2)},\cdots,\delta^{(2)}$ using
 $$
 \delta^{(l)}=((\Theta^{(l)})^{T}\delta^{(l+1)}).\*a^{(l)}.\*(1-a^{(l)})
 $$
 We then element-wise multiple that with a function called $g'$ which is the derivative of the activation function $g$ evaluated with the input values given by $z^{(l)}$:
 $$
 g'(z^{(l)}) = a^{(l)}.\*(1-a^{(l)})
 $$
 5. $\Delta_{i,j}^{(l)} := \Delta_{i,j}^{(l)} + a_{j}^{(l)}\delta_{i}^{(l+1)}$ or with vectorization:
 $$
 \Delta^{(1)} := \Delta^{(l)} + \delta^{(l)} + \delta^{(l+1)}(a^{(l)})^T
 $$
 Hence we update our new $\Delta$ matrix:
 $$
 D_{i,j}^{(l)} =
 \begin{cases}
 \frac{1}{m}(\Delta_{i,j}^{(l)} + \lambda\Theta_{i,j}^{(l)}), & if \quad j \ne 0 \\\\
 \frac{1}{m}\Delta_{i,j}^{(l)} & if \quad j \ne 0
 \end{cases}
 $$
 The $\Delta$ matrix $D$ is used as an "accumulator" to add up our values as we go along and eventually compute our partial derivative. Thus we get:
 $$
 \frac{\partial}{\partial\Theta_{i,j}^{(l)}}J(\Theta) = D_{i,j}^{(l)}
 $$
