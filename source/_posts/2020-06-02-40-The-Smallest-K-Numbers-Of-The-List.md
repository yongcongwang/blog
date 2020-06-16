---
title: CodingInterview | 40 The Smallest K Numbers Of The List
mathjax: true
comments: true
date: 2020-06-02 00:28:59
categories: coding
tags:
 - coding
 - coding_interview
---

> Input a list of n numbers, please find the smallest k numbers.
> For example, the smallest `4` numbers of the list `4, 5, 1, 6, 2, 7, 3, 8` is:
> `1, 2, 3, 4`.

<!-- more -->

## Solution
```C++
bool GetMinKNumbers(
    const std::vector<int>& arr, const int k,
    std::multiset<int, std::greater<int>>* const result) {
  if (k > arr.size() || k <= 0) {
    return false;
  }

  std::multiset<int, std::greater<int>> tmp(arr.begin(), arr.begin() + k);
  result->swap(tmp);

  auto it = arr.begin() + k;
  while (it != arr.end()) {
    if (*it < *result->begin()) {
      result->erase(result->begin());
      result->insert(*it);
    }

    it++;
  }

  return true;
}
```
