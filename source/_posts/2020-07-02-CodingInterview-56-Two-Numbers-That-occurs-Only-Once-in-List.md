---
title: CodingInterview | 56 Two Numbers That occurs Only Once in List
categories: coding
tags:
  - coding interview
mathjax: true
comments: true
date: 2020-07-02 00:36:50
---

> In an integar array, all numbers appears twice except two, please output them.
> You should realize the function within time complexity of $O(n)$ and space complexity of $O(1)$.

<!-- more -->

## Solution
```C++
int FirstOneDigit(int num) {
  int result(0);
  while((num & 1) == 0 && result < 8 * sizeof(int)) {
    num = num >> 1;
    result++;
  }

  return result;
}

bool IsDigitKOne(int num, int k) {
  num = num >> k;
  return num & 1;
}

std::pair<int, int> TwoTimesNumber(const std::vector<int>& arr) {
  if (arr.empty()) {
    return {-1, -1};
  }

  int result_or(0);
  for (auto num : arr) {
    result_or ^= num;
  }

  int digit_one = FirstOneDigit(result_or);

  int result1(0);
  int result2(0);

  for (auto num : arr) {
    if (IsDigitKOne(num, digit_one)) {
      result1 ^= num;
    } else {
      result2 ^= num;
    }
  }

  return {result1, result2};
}
```
