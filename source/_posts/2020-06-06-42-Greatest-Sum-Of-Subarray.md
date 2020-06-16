---
title: CodingInterview | 42 Greatest Sum Of Subarray
mathjax: true
comments: true
date: 2020-06-06 18:31:19
categories: coding
tags:
 - coding
 - coding_interview
---

> Input a integar array, elements of the array can be positive or negtive, please output the maximum sum of its subarray. 

<!-- more -->

## Solution
```
int MaxSubarray(const std::vector<int>& arr) {
  if (arr.empty()) {
    return -1;
  }

  int max= std::numeric_limits<int>::min();
  int sum = 0;
  for (const auto& ele : arr) {
    sum += ele;
    max = std::max(sum, max);
    sum = sum < 0 ? 0 : sum;
  }

  return max;
}
```
