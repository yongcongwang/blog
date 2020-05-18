---
title: CodingInterview | 16 The Integar exponent of a Double Number
mathjax: true
comments: true
date: 2020-05-05 22:27:37
categories: coding
---

> Realize a function to calculate the exponent of a double number. Don't use library and no need to care about big number.
<!-- more -->
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
