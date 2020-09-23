---
title: Algorithm Analysis
mathjax: true
categories: []
date: 2020-09-23 00:20:48
---

An `algorithm` is a clearly specified set of simple instructions to be followed to solve a problem. The important step of algorithm analysis is to determine how much in the way of resource, such as time or spaces, the algorithm requires.

<!-- more -->

# Mathematical definitions

We use following definitions to estimate the resource use of an algorithm:
- $T(N) = O(f(N))$, if there are positive constants $c$ and $n_0$ such that $T(N) <= c \cdot f(N)$ when $N >= n_0$.
- $T(N) = \Omega(g(N))$, if there are positive constants $c$ and $n_0$ such that $T(N) >= c \cdot g(N)$ when $N >= n_0$.
- $T(N) = \Theta(h(N))$, if $T(N) = O(h(N))$ and $T(N) = \Omega(h(N))$.
- $T(N) = o(p(N))$, if for all positive constant $c$, there exists an $n_0$ such that $T(N) < c \cdot p(N)$ when $N > n_0$. In other words, $T(N) = o(p(N))$ if $T(N) = O(p(N))$ and $T(N) \ne \Theta(p(N))$

When we say that $T(N) = O(f(N))$, we are guaranteeing that the function $T(N)$ grows at a rate no faster than $f(N)$, $f(N)$ is an `upper bound` on $T(N)$; since this implies that $f(N) = \Omega(T(N))$, we say that $T(N)$ is a `lower bound` on $f(N)$.

Here are some important rules to know:

1. If $T_1(N) = O(f(N))$ and $T_2(N) = O(g(N))$, then:
 - $T_1(N) + T_2(N) = O(f(N) + g(N))$
 - $T_1(N) * T_2(N) = O(f(N) * g(N))$
2. If $T(N)$ is a polynomial of degree $k$, then $T(N) = \Theta(N^k)$
3. $\log^k(N) = O(N)$ for any constant $k$.

