---
title: CodingInterview | 03 Duplication Number
mathjax: true
comments: true
date: 2020-04-22 23:52:24
categories: coding
---

> Find the duplicated number in a list. You are given a list with or without duplicated numbers. All the numbers in the list are positive. If there are duplicated numbers in the list, please output them; if not, return -1;

## Solution
```C++
void swap(int &a, int &b) {
  int tmp = a;
  a = b;
  b = tmp;
}

int GetDuplicateNum(std::vector<int> &arr) {
  if (arr.empty()) {
    return -1;
  }

  for (int i = 0; i < arr.size(); ++i) {
    while (arr[i] != i) {
      if (arr[arr[i]] == arr[i]) {
        return arr[i];
      }
      swap(arr[arr[i]], arr[i]);
    }
  }

  return -1;
}
```
