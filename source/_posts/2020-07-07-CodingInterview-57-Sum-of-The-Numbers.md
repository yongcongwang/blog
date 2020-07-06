---
title: CodingInterview | 57 Sum of The Numbers
categories: coding
tags:
  - coding interview
mathjax: true
comments: true
date: 2020-07-07 00:19:44
---

> With a sorted array and a number `s`, please output two numbers in the array whose sum is `s`.

<!-- more -->

## solution
```C++
std::pair<int, int> SumNumbers(const std::vector<int>& arr, const int num) {
  if (arr.empty()) {
    return {0, 0};
  }

  int start = 0;
  int end = arr.size() - 1;
  while (end > start) {
    if (arr[start] + arr[end] > num) {
      end--;
    } else if (arr[start] + arr[end] < num) {
      start++;
    } else {
      return {arr[start], arr[end]};
    }
  }

  return {0, 0};
}
```

> With a positive integar `s`, please output all the positive continuous integar sequences whose sum is `s`. For example, with the input of `15`, the output would be `1, 2, 3, 4, 5`, `4, 5, 6` and `7, 8`.

## Solution
```C++
void PrintVec(int start, int end) {
  while (start < end) {
    std::cout << start << " ";
    start++;
  }
  std::cout << end << std::endl;
}

void SumSequence(const int num) {
  if (num < 2) {
    return;
  }

  int start = 1;
  int end = 2;
  int sum = 3;

  while (end < num) {
    if (sum > num) {
      sum -= start;
      start++;
    } else if (sum < num) {
      end++;
      sum += end;
    } else {
      PrintVec(start, end);
      end++;
      sum += end;
    }
  }
}
```
