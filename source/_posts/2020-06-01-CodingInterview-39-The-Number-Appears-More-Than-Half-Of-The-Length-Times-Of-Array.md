---
title: >-
  CodingInterview | 39 The Number Appears More Than Half Of The Length Times Of
  Array
mathjax: true
comments: true
date: 2020-06-01 22:06:19
categories: coding
---

> A number appears more than half of the length of the list times, please find it out. 
> For example, in the list `{1, 2, 3, 2, 2, 2, 5, 4, 2}`, the `2` is the number.

<!-- more -->

## Solution
```C++
int NumAppearMoreThanHalf(const std::vector<int>& arr) {
  if (arr.empty()) {
    return -1;
  }

  int base = arr.front();
  int base_cnt = 0;

  for (const auto &ele : arr) {
    if (ele == base) {
      base_cnt++;
    } else if (base_cnt > 0) {
      base_cnt--;
    } else {
      base = ele;
      base_cnt = 1;
    }
  }

  return base;
}
```
