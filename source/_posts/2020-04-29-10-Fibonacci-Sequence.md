---
title: CodingInterview | 10 Fibonacci Sequence
mathjax: true
comments: true
date: 2020-04-29 23:59:05
categories: coding
tags:
 - coding
 - coding_interview
---

> Write a function to get the nth number of Fibonacci sequence. The Fibonacci sequence is defined as following:
$$
f(n) = 
\begin{cases}
0, & if & n = 0 \\\\
1, & if & n = 1 \\\\
f(n - 1) + f(n - 2), & if & n > 1
\end{cases}
$$
<!-- more -->
## Solution 1
```C++
int FibonacciRecursion(const int n) {
  if (n <= 0) {
    return 0;
  }

  if (n == 1) {
    return 1;
  }

  return FibonacciRecursion(n - 1) + FibonacciRecursion(n - 2);
}
```

This solution is simple, but its time complexity is $O(2^n)$, which is usually unacceptable.

## Solution 2
```C++
int FibonacciLoop(const int n) {
  if (n <= 0) {
    return 0;
  }

  if (n == 1) {
    return 1;
  }

  int result = 0;
  int fibo_minus_two = 0;
  int fibo_minus_one = 1;
  for (int i = 2; i <= n; ++i) {
    result = fibo_minus_two + fibo_minus_one;
    fibo_minus_two = fibo_minus_one;
    fibo_minus_one = result;
  }

  return result;
}
```

This solution use loop to calculate the result, and its time complexity is $O(n)$
