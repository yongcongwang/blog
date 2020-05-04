---
title: CodingInterview | 14 Cut Line
mathjax: true
comments: true
date: 2020-05-03 23:31:06
categories: coding
---
> If there is a line with the length of $n$, please cut the line into $m$ sections($m$ and $n$ are int, and $n > 1$, $m > 1$) and the product of all sections is maximum.
> For example, the line is $18$ long, and we cut it into 3 sections: $2, 3, 3$, the product is maximum: $18$.

## Solution 1
```C++
int GetMaxCuttingDP(const int length) {
  if (length < 2) {
    return 0;
  }

  if (length == 2) {
    return 1;
  }

  if (length == 3) {
    return 2;
  }

  std::vector<int> product;
  product.push_back(0);
  product.push_back(1);
  product.push_back(2);
  product.push_back(3);

  for (int i = 4; i <= length; ++i) {
    int max(0);
    for (int j = 1; j <= i / 2; ++j) {
      int curr_product = product[j] * product[i - j];
      max = max > curr_product ? max : curr_product;
    }
    product.push_back(max);
  }

  return product.back();
}
```
There are two loops in the code, and the time complexity is $O(n^2)$.

## Solution 2
```c++

int GetMaxCuttingGreed(const int length) {
  if (length < 2) {
    return 0;
  }

  if (length == 2) {
    return 1;
  }

  if (length == 3) {
    return 2;
  }

  int ThreeCnt = length / 3;
  if (length % 3 == 1) {
    ThreeCnt--;
  }

  const int TwoCnt = (length - ThreeCnt * 3) / 2;
  return std::pow(3, ThreeCnt) * std::pow(2, TwoCnt);
}
```
This is the solution with the time complexity of $O(n)$.