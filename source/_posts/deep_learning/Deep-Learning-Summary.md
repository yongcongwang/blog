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
![nn](/images/2020/deep_learning/neuron.jpg)

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

## Neural Network Basics
This part we learn to set up a machine learning problem with a neural network mindset. Learn to use vectorization to speed up your models.

### Logistic regression
Algorithm is used for classification of 2 classes. We use the equation:
$$
y = wx + b
$$
to calculate the output. 
If $x$ is a vector, the equation becomes:
$$
y = w^Tx + b
$$
If we need $y$ to be in $[0, 1]$(probability):
$$
y = sigmoid(w^Tx + b)
$$

### Logistic regression cost function
The cost function can be the square root error:
$$
L(\hat{y}, y) = \frac{1}{2} \cdot (\hat{y} - y)^2
$$
but we won't use this notation because it leads to optimization problem which is non convex, means it contains local optimum points.

Alternately, we use the function:
$$
L(\hat{y}, y) = - (y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y}))
$$
this leads to two case:
- if $y = 1$, $L(\hat{y}, 1) = -log(\hat{y})$, we want $\hat{y}$ to be the largest, and the largest value of $\hat{y}$ is $1$;
- if $y = 0$, $L(\hat{y}, 1) = -log(1 - \hat{y})$, we want $1 - \hat{y}$ to be the largest, and the smallest value of $\hat{y}$ is $0$;

Then the cost function will be:
$$
J(w, b) = \frac{1}{m}\sum^{m}\_{i=1}{(L(\hat{y}^{[i]}, y^{[i]}))}
$$
The difference between loss function and cost function:
- the loss function calculates the error for a single training example;
- the cost function calculates the average of the loss function of the entire training set.

### Gradient Descent
Our target is to predict $w$ and $b$ that minimize the cost function while the cost function itself is convex.

The gradient descent repeats:
$$
w = w - \alpha \cdot dw
$$
$$
b = b - \alpha \cdot db
$$
to reach the minimum of cost function, while the $\alpha$ is the `learning rate` and $dw$ is the derivative of $w$, $db$ is the derivative of $b$.

### Vectorization
Deep learning shines when the dataset is big. However, `for loop` will make you wait a lot for a result. That's why we need vectorization to get rid of  some of our `for loop`s.

### General steps
The main steps for building a Neural Network are:
- Define the model structure(such as number of input features and outputs);
- Initialize the model's parameters;
- Loop:
 - Calculate current loss(forward propagation);
 - Calculate current gradient(backward propagation)
 - Update parameters(gradient descent)

Tunning the learning rate(which is an example of a "hyperparameter") can make a big difference to the algorithm.

## Shallow neural network
This part we learn to build a neural network with one hidden layer, using forward propagation and backward propagation.

### Neural network overview
![shallow_nn](/images/2020/deep_learning/shallow_nn.png)

In the left logistic regression we had:
$$
z = W^TX + B \Rightarrow a = sigmoid(z) \Rightarrow L(a, Y)
$$
where $W$, $X$ and $B$ are matirx.

In neural networks with one layer we will have:
$$
Z_1 = W_1^TX + B \Rightarrow A1 = sigmoid(Z_1) \Rightarrow Z_2 = W_2^TA_1 + B_2 \Rightarrow A_2 = sigmoid(Z_2) \Rightarrow L(A2, Y)
$$

Neural Network is a stack of logistic regression objects.

### Neural network notations

#### General comments
- Superscript $(i)$ will denote the $i^{th}$ training example while the superscript $[i]$ will denote the $l^{th}$ layer.

#### Sizes
- $m$: number of examples in the dataset;
- $n_x$: input size;
- $n_y$: output size(or number of classes);
- $n_h^{[l]}$: number of hidden units of the $l^{th}$ layer;
- $L$: number of layers in the network.

#### Objects
- $X$: the input matrix
- $x^{(i)}$: the $i^{th}$ example represented as a column vector;
- $Y$: the label matrix;
- $y^{(i)}$: the output label for the $i^{th}$ example;
- $W^{[l]}$: the $l^{th}$ lyaer weight matrix;
- $b^{[l]}$: the bias vector of $l^{th}$ layer;
- $\hat{y}$: the predicted output vector. It can also be denoted $a^{[L]}$ where $L$ is the number of layers in the network.

#### Forward propagation
- $a = g^{[l]}(W_xx^{(i)} + b_1) = g^{[l]}(z_1)$, where $g^{[l]}$ denotes the $l^{th}$ layer activation function;
- $J(x, W, b, y)$ or $J(\hat{y}, y)$ denotes the cost function.

### Activation functions
![activation functions](/images/2020/deep_learning/activation.png)

#### sigmoid
So far we are using sigmoid, but it works not so well:
- sigmoid can lead us to gradient decent problem where the updates are so slow;
- the range of function is $[0, 1]$.

#### tanh
`tanh` is a shifted version of sigmoid with the range $[-1, 1]$. It usually works better than sigmoid activation for hidden units because the mean of its outputs is closer to $0$, and so it centers the data better for the next layer.

#### ReLU
`sigmoid` or `tanh` function disadvantage is that if the input is too small or too high, the slope will be near zero which will cause the gradient decent problem.

One of the popular activation functions that solved the slow gradient decent is the ReLU function.

#### Leaky ReLU
The difference between Leaky ReLU and ReLU is that if the input is negtive the slope will be so small. It works as ReLU but most people use ReLU.

### Why we need non-linear activation functions
Linear activation will output linear activations, that means whatever hidden layers you add, the activation will be always linear like logistic regression, so it's useless in a lot of complex problems.

You might use linear activation function in one place, the output layer, if the output is real number(regression problem). But even in this case if the output value is non-negtive you could still use ReLU instead.

### Derivative of activation functions

- Derivation of sigmoid activation function:

$$
g(z) = \frac{1}{1 + e^{-z}}
$$

$$
g'(z) = \frac{1}{1 + e^{-z}} \cdot (1 - \frac{1}{1 + e^{-z}}) = g(z) \cdot (1 - g(z))
$$

- Derivation of tanh activation function:

$$
g(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$

$$
g'(z) = 1 - tanh^2(z) = 1 - g^2(z)
$$

- Derivation of ReLU activation function:

$$
g(z) = max(0, z)
$$

$$
g'(z) = 
\begin{cases}
0, \quad \mbox{if} \quad z < 0 \\\\
1, \quad \mbox{if} \quad z >= 0
\end{cases}
$$

- Derivation of leaky ReLU activation function:

$$
g(z) = max(0.01 \cdot z, z)
$$

$$
g'(z) = 
\begin{cases}
0.01, \quad \mbox{if} \quad z < 0 \\\\
1, \quad \mbox{if} \quad z >=0
\end{cases}
$$

### Random initialization
In logistic regression it wasn't important to initialize the weights randomly, while in neural network we have to initialize them randomly.

While initializing bias with $0$ is OK, neural network won't work if we initialize all weights with zeros:

- all hidden units will be completely identical(symmetric) and compute exactly the same function;
- on each gradient descent iteration all the hidden units will always update the same.

We need small values because in sigmoid(or tanh) activation function, for example, if the weights is too large you are more likely to end up with very large values of $Z$. Which causes your tanh or sigmoid activation function to be saturated, thus slowing down learning. If you don't have any sigmoid or tanh activation function throughout your neural network, this is less of an issue.

## Deep neural network
Shallow Neural Network is a Neural Network with $1$ or $2$ layers.
Deep Neural Network is a Neural Network with $3$ or more layers.

### Getting your matrix dimensions right
With the equation:
$$
Z = W^TX + B
$$
where $X$ has the shape of $(x, n^{[l-1]})$.

- Dimension of $W$ is $(n^{[l]}, n^{[l-1]})$;
- Dimension of $B$ is $(n^{[l]}, 1)$;
- $dw$ has the same shape as $W$;
- $db$ has the same shape as $B$;
- Dimension of $Z^{[l]}$, $A^{[l]}$, $dZ^{[l]}$, $dA^{[l]}$ is $(n^{[l]}, m)$.

### Hyperparameters
The main parameters of Neural Network is:
- $w$;
- $b$.

Hyperparameters are the parameters that control the algorithm:
- learning rate;
- Number of iteration;
- Number of hidden layers;
- Number of hidden units;
- Choice of activations.

# Improving Deep Neural Networks: Hyperparameter Tuning, Regularition and Optimization

## Practical aspects of deep learning

### Train/dev/test Sets
It's impossible to get all your hyperparameters right on a new application from the first time, so, the idea is to go through the loop:
```C++
   Idea --> Code --> Experiment
    ^                     |
    |                     |
    -----------------------
```
You can go through the loop many times to figure out your hyperparameters.

Generally, we divid the data into three parts:
- Train set, which used to train the neural network and is usually the largest set;
- Develop(dev) set, which is used to validate the traing result;
- Testi set, which is used to test the trained neural network.

You will try to build a model upon `train set` then try to optimize hyperparamters on `dev set` as much as possible. After your model is ready, you can evaluate the model with `test set`.

The ratio of splitting the models is:
- `6:2:2`, if the size of the dataset is $100$ to $1000000$;
- `98:1:1 or 99.5:0.25:0.25`, if the size of the dataset is $> 1000000$.

You should make sure the `dev set` and `test set` comes from the same distribution.

### Bias/variance
Bias and variance techiques are easy to learn but difficult to master.
Generally, your model is:
- `underfitting`, if it has a `high bias`;
- `overfitting`, if it has a `high variance`.
![bias and variance](/images/2020/deep_learning/bias_and_variance.png)

You can plot the result as the figure above, but if this is not possible, another idea to get bias/ variance is to check the error:
- High variance(overfitting):
 - Training error: 1%;
 - Dev error: 11%.
- High bias(underfitting):
 - Training error: 15%;
 - Dev error: 14%.
- High bias (underfitting) && High variance(overfitting):
 - Training error: 15%;
 - Test error: 30%.
- Best:
 - Training error: 0.5%;
 - Test error: 1%.

These conclusions come from the assumption that human has $0%$ error. If the problem isn't meeting this assumption, you will need to use human error as baseline.

### Basic recipe for high bias and variance
If your algorithm has a high bias, you can:
- Try to make your neural network bigger(more hidden units or more layers);
- Try a different model that fits your data well;
- Try more batches;
- Try difference(advanced) optimization algorithms.

If your algorithm has a high variance, you can:
- Use more data;
- Try regularization;
- Try a different model that is suitable for your data.

No matter what the problem is, training a bigger neural network never hurts, although this may lead to longer runing time.

## Regularizing your neural network
For variance(overfitting) problems, we can try a bigger training data to fix it. But some times you can't just get more training data, or it would be quite expensive to get more data. In this case regularization will often help to prevent overfitting, or reduce the errors in your network.

### Regularization

#### Regularization for logistic regression
- $L_1$ regularization
$$
J(w,b) = \frac{1}{m} \sum_{i = 1}^mL(\hat{y^{(i)}}, y^{(i)}) + \frac{\lambda}{2m} \lVert w \rVert_2^2
$$
$$
\lVert w \rVert_2^2 = \sum_{j = i}^{n_x}|w_j|
$$
where $\lambda$ is called regularization parameter(hyperparameter), you can try different value and choose the one with best performance.

- $L_1$ regularization(for arcane technical math, this is called `Frobenius norm`)
$$
J(w,b) = \frac{1}{m} \sum_{i = 1}^mL(\hat{y^{(i)}}, y^{(i)}) + \frac{\lambda}{2m} \lVert w \rVert_1
$$
$$
\lVert w \rVert_1 = \sum_{j = i}^{n_x}w_j^2 = w^Tw
$$

#### Regularization for neural network
The normal cost function that we want to minimize is:
$$
J(w^{[1]}, b^{[1]}, ..., w^{[L]}, b^{[L]}) = \frac{1}{m} \sum_{i = 1}^{m}L(\hat{y^{(i)}}, y^{(i)})
$$

Then the $L_2$ regularization is:
$$
J(w^{[1]}, b^{[1]}, ..., w^{[L]}, b^{[L]}) = \frac{1}{m} \sum_{i = 1}^{m}L(\hat{y^{(i)}}, y^{(i)}) + \frac{1}{2m} \sum_{l = 1}^{L} \lVert w^{[l]} \rVert^2
$$

The old way we do back propagation is:
$$
dw^{[l]} = (back propagation)
$$
$$
w^{[l]} = w^{[l]} - \alpha \cdot dw^{[l]}
$$
Then we change to:
$$
dw^{[l]} = (back propagation) + \frac{\lambda}{m} \cdot w^{[l]}
$$
So:
$$
\begin{align}
w^{[l]} 
& = w^{[l]} - \alpha \cdot dw^{[l]} \\\\
& = w^{[l]} - \alpha * ((back propagation) + \frac{\lambda}{m} \cdot w^{[l]}) \\\\
& = w^{[l]} - \alpha * (back propagation) - \alpha * (\frac{\lambda}{m} \cdot w^{[l]}) \\\\
& = (1 - \frac{\alpha\lambda}{m}) \cdot w^{[l]} - \alpha * (back propagation)
\end{align}
$$

In practice this will penalize large weights and effectively limits the freedom in your model, because the them $(1 - \frac{\alpha\lambda}{m}) \cdot w^{[l]}$ causes the `weight to decay` in propartion to its size.

#### Why regularization reduces overfitting
Here are some intuitions:
- If $\lambda$ is too large: a lot of $w$ part will be close to $0$, which makes the neural network more simple;
- If $\lambda$ is good enough: it will reduce some weights that makes the neural network overfitting.

And for $tanh$ activation function:
- If $\lambda$ is too large, $w$ part will be small(close to $0$), which will use the linear part of the $tanh$ activation function, so we will go from non-linear activation to roughly linear which would make the neural network a roughly linear classifier.
- If $\lambda$ is good enough, it will just make some of $tanh$ activations roughly linear which will prevent overfitting.

### Dropout regularization
In most case, we use $L_2$ regularization. The dropout regularization eliminates some neurons/weights on each iteration based on a probability. A most common techinque to implement dropout is called `Inverted dropout`:
```Python
keep_prob = 0.8   # 0 <= keep_prob <= 1
l = 3  # this code is only for layer 3
# the generated number that are less than 0.8 will be dropped. 80% stay, 20% dropped
d3 = np.random.rand(a[l].shape[0], a[l].shape[1]) < keep_prob

a3 = np.multiply(a3,d3)   # keep only the values in d3

# increase a3 to not reduce the expected value of output
# (ensures that the expected value of a3 remains the same) - to solve the scaling problem
a3 = a3 / keep_prob
```

#### Understanding dropout

- Dropout knocks out units in neural network randomly, so it works like on every iteration you're working with a smaller neural network which has a regulizing effect.
- Neural network can not rely on any one feature because it may be knocked out, so it has to spread out weights.
- Dropout can have different `keep_prob` per layer.
- The input layer dropout has to be near $1$(or just $1$) because you don't want to eliminate a lot of featrues.
- A lot of researchers are using dropout with Computer Vision(CV), bacause they have a very big input size and almost nerver have enough data, so overfitting is the usual problem. And dropout is a regularization technique to prevent overfitting.

### Other regularization methods

#### Data augmentation
- In a computer vision data, you can:
 - flip all your pictures horizontally which will give you more data instances;
 - apply a random position and rotation to an image to get more data.
- In OCR you can impose random ratation and distortions to digits/letters.
- New data obtained using this technique isn't as good as the real independent data, but still can be used as a regularization techniques.

#### Early stopping
We plot the `training set cost` and the `dev set cost` together for each iteration. At some iteration the `dev set cost` will stop decreasing and will start `increasing`. We will pick the point at wich the training set error and dev set error are best(lowest training cost with lowest dev cost).
![](/images/2020/deep_learning/early_stop.png)

We prefer to use $L_2$ regularization instead of early stop because this technique simultaneously tries to mimimize the cost function and not to overfit which contradicts the orthogonalization approch. But its advantage is that you don't need to search a hyperparameter.

#### Model ensembles
You can train multiple independent models and average their results, this can get you extra 2% performance and reduces the generalization error.

## Setting up your optimization problem

### Normallizing inputs
Normalizing inputs will speed up the training process a lot.
![normalize](/images/2020/deep_learning/normalize_trainning_set.png)

Normalization are going on these steps:

1. Get the mean of the training set: $mean = \frac{1}{m} * \sum_{i=1}^mx^{(i)}$
2. Subtract the mean from each input: $X = X - mean$, this will make your inputs centered around $0$.
3. Get the variance of the training set: $variance = \frac{1}{m} * \sum_{i = 1}^m(x^{(i)})^2$
4. Normalize the variance: $X = X / variance$

So why we normalize our inputs?
- If we don't normalize the inputs our cost function will be deep and its shape will be inconsistent(elongated), then optimizing it will take a long time.
- If we normalized the inputs, the shape of the cost function will be consistent(look more symmetric like circle in 2D exmaple) and we can use a larger learning rate $\alpha$, the optimization will be faster.

### Vanishing/exploding gradients
The vanishing/exploding gradients occurs when your derivates becomes very small or very big. To understand the problem, suppose that we have a deep neural network with number of layer $L$, and all the activation functions are `linear` and each $b = 0$, then:
$$
\hat{y} = w^{[L]}w^{[L - 1]}w^{[L - 2]} \cdots w^{[2]} w^{[1]} x
$$
and if we have 2 hidden units per layer and $x_1 = x_2 = 1$, we will result in:
$$
\hat{y} = w^{[L]} \begin{bmatrix}x & 0 \\\\ 0 & x \end{bmatrix}^{L-1} = x^L \\\\
$$
as:
$$
w^{[L]} = \begin{bmatrix}x & 0 \\\\ 0 & x \end{bmatrix}^{L-1}
$$

If $x < 1$, $\hat{y}$ will be very small; if $x > 1$, $\hat{y}$ will be really big.
This example explains that the activations (and similarly derivatives) will be decreased/increased exponentially as a function of number of layers.

### Weight initialization for deep networks
A partial solution to the vanishing/exploding gradients in neural network is better or more careful choice of the random initialization of weights.
In a simgle neuron: $Z = w_1x_1 + w_2x_2 + \cdots + w_nx_n$, if the number of node $n_x$ is large, we want $w$ to be smaller to not explode the cost, which turns out that we need the variance(equal to $\frac{1}{n_x}$) to be the range of $W$.
So we initialize $W$ like this(better to use with `tanh` activation):
```Python
np.random.rand(shape) * np.sqrt(1/n[l-1])
```
or variation of this:
```Python
np.random.rand(shape) * np.sqrt(2/(n[l-1] + n[l]))
```
Setting initialization part inside sqrt to `2/n[l-1]` for `ReLU` is better:
```Python
np.random.rand(shape) * np.sqrt(2/n[l-1])
```
This is one of the best way of partially solution to Vanishing / Exploding gradients (ReLU + Weight Initialization with variance) which will help gradients not to vanish/explode too quickly.
