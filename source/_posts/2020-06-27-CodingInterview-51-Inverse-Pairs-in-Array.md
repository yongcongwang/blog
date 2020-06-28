---
title: CodingInterview | 51 Inverse Pairs in Array
categories: coding
tags:
  - coding_interview
mathjax: true
comments: true
date: 2020-06-27 21:09:36
---

> If there are two numbers in array, the number in front is bigger than the number in back, they form an inverse pair. For example, in the list `{7, 5, 6, 4}`, there are 5 inverse pairs: `(7, 6), (7, 5), (7, 4), (6, 4), (5, 4)`. Inpu an array, please output the number of inverse pairs.

<!-- more -->

## Solution
```C+++
int GetInversePairs(std::vector<int>& arr, int start, int end) {
  if (start == end) {
    return 0;
  }

  int mid = (end + start) / 2;
  int left_cnt = GetInversePairs(arr, start, mid);
  int right_cnt = GetInversePairs(arr, mid + 1, end);

  int merge_cnt = 0;
  int left_end = mid;
  int right_end = end;
  std::vector<int> tmp;
  while (left_end >= start && right_end >= mid + 1) {
    if (arr[left_end] > arr[right_end]) {
      merge_cnt += right_end - mid;
      tmp.push_back(arr[left_end]);
      left_end--;
    } else {
      tmp.push_back(arr[right_end]);
      right_end--;
    }
  }
  while (left_end >= start) {
    tmp.push_back(arr[left_end]);
    left_end--;
  }
  while (right_end >= mid + 1) {
    tmp.push_back(arr[right_end]);
    right_end--;
  }
  for (int i = end; i >= start; --i) {
    arr[i] = tmp[end - i];
  }

  return left_cnt + right_cnt + merge_cnt;
}

int InversePairsCount(std::vector<int>& arr) {
  if (arr.empty()) {
    return 0;
  }

  return GetInversePairs(arr, 0, arr.size() - 1);
}
```
