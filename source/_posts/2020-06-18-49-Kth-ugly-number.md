---
title: 49 Kth ugly number
categories: coding
tags:
  - coding
  - coding_interview
mathjax: true
comments: true
date: 2020-06-18 21:23:32
---

> The number that contains only 2, 3, 5 is called ugly number. In general, 1 is the first ugly number. For example, 6, 8 are ugly numbers but 17 not.
> Please output kth ugly number.

<!-- more -->

## Solution
```C++
int KthUglyNumber(const int k) {
  if (k < 1) {
    return -1;
  }

  int ugly_base_2 = 0;
  int ugly_base_3 = 0;
  int ugly_base_5 = 0;
  std::vector<int> ugly_list;
  ugly_list.push_back(1);
  int curr_ugly_cnt = 1;
  while (curr_ugly_cnt < k) {
    ugly_list.push_back(
        std::min(std::min(ugly_list[ugly_base_2] * 2,
                          ugly_list[ugly_base_3] * 3),
                 ugly_list[ugly_base_5] * 5));
    while (ugly_list[ugly_base_2] * 2 <= ugly_list.back()) {
      ugly_base_2++;
    }
    while (ugly_list[ugly_base_3] * 3 <= ugly_list.back()) {
      ugly_base_3++;
    }
    while (ugly_list[ugly_base_5] * 5 <= ugly_list.back()) {
      ugly_base_5++;
    }

    curr_ugly_cnt++;
  }

  return ugly_list.back();
}
```
