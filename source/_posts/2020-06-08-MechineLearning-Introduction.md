---
title: MechineLearning | Introduction
mathjax: true
comments: true
date: 2020-06-08 21:08:57
categories: algorithm
---

## Defination
A Computer program is said to learn from experience `E` with respect to some task `T` and some performance measure `P`, if its performance on `T`, as measured by `P`, improves with experience `E`.
There are two common types of Machine Learning: Supervised Learning and Unsupervised Learning.

<!-- more -->

## Supervised Learning
The term Supervised Learning refers to the fact that we gave the algorithm a data set which we call "right answer", and the task of the algorithm was to produce more of these right answers.
The problem is called a
- regression problem, if the algorithm should predict a **continuous** valued output;
- classification problem, if the algirhtm should predict a **discrete** valued output.

For example, you have a large inventory of identical items and want to predict how many of these items will sell over the next 3 months, this is a regression problem. 
If you would like to examine individual customer accounts, and for each account decide if it has been hacked/compromised, this is a classification problem.

## Unsupervised Learning
Unsupervised Learning allows us to approach problems whith little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.

We can derive this structure by clustering the data based on relationships among the variables in the data.

With unsupervised learning there is no feedback based on the prediction results.

For example,
- Clustering: Take a collection of 1000000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles and so on.
- Non-Clustering: The "Cocktail Party Problem", allows you to find structure in a chaotic environment.
