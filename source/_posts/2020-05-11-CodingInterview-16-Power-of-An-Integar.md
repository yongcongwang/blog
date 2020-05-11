---
title: CodingInterview | 16 Power of An Integar
mathjax: true
comments: true
date: 2020-05-11 23:20:52
categories: coding
---

> Realize a function to get the integar exponent of a number without the usage of library. You don't need to consider about the big number.

## Solution
```C++
double pos_power(const double base, const int exponent) {
  double result = 1;
  for (int i = 0; i < exponent; ++i) {
    result *= base;
  }
  return result;
}

double power(const double base, const int exponent) {
  if (base == 0) {
    return 0;
  }
  if (exponent == 0) {
    return 1;
  }
  if (exponent == 1) {
    return base;
  }

  const int exp = exponent > 0 ? exponent : -exponent;
  double result = pos_power(base, exp >> 1);
  result *= result;
  result *= exp & 0x01 ? base : 1;
  return exponent > 0 ? result : 1.0 / result;
}
```
