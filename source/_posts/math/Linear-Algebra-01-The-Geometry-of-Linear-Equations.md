---
title: Linear Algebra | 01 The Geometry of Linear Equations
mathjax: true
comments: true
date: 2020-05-06 22:43:56
categories:
  - math
---
Linear algebra is used to get the solution of multiple equations. Let's look at an exmple:
$$
2x - y = 0 
$$
$$
-x + 2y = 3
$$
<!-- more -->
The equations can be written as:
$$
\begin{bmatrix}2 & -1 \\\\ -1 & 2\end{bmatrix} \begin{bmatrix} x \\\\ y \end{bmatrix} = \begin{bmatrix} 0 \\\\ 3 \end{bmatrix} \tag1
$$

And if we use $A$, $x$ and $b$ replace the three matrices, we'll get the normal format:
$$
Ax = b
$$

## Row Picture
If we draw the picture of the two equations, it's as following:
![](/images/2020-05-07-geometry-linear-equations/row_space_2d.png)

As we alll know that the point that two lines meet is the solution. In this situation, it's the point $(1, 2)$.

## Column Picture
We can regard the $(1)$ equation as a **linear combination of columns**, which means:
$$
x \begin{bmatrix} 2 \\\\ 1 \end{bmatrix} + y \begin{bmatrix} -1 \\\\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\\\ 3 \end{bmatrix}
$$
There are three vectors on the picture:
![](/images/2020-05-07-geometry-linear-equations/column_space_2d.png)

And if we take $x = 0$ and $y = 3$ into the equation, we'll get the result that one of the vector $(2, -1)$ add two of the vector $(-1, 2)$ is the result vector$(0, 3)$.

## Row Picutre and Column Picture in High Dimensions
If we take the following equations into consider, the 
