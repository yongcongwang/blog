---
title: CodingIntervew | 43 Find The Occurences Of 1 In Range 1-n
mathjax: true
comments: true
date: 2020-06-07 16:21:45
categories: coding
tags:
 - coding
 - coding_interview
---

> Find the occurences of 1 in range `1-n`.

<!-- more -->

## Solution
```
int GetNumLength(int num) {
  int cnt(0);
  while (num != 0) {
    num /= 10;
    cnt ++;
  }

  return cnt;
}

int OneAppearance(const int num) {
  if (num <= 0) {
    return 0;
  }

  const int length = GetNumLength(num);
  if (length == 1) {
    return 1;
  }

  const int tmp = std::pow(10, length - 1);
  const int first = num / tmp;
  const int top_one_cnt = first == 1 ? num % tmp + 1 : std::pow(10, length - 1);
  const int top_other_cnt = first * (length - 1) * std::pow(10, length - 2);
  const int sub_cnt = OneAppearance(num % 10);

  return top_one_cnt + top_other_cnt + sub_cnt;
}
```
