---
title: CodingInterview | 45 Rerange The List To Min Number
mathjax: true
comments: true
date: 2020-06-11 21:56:50
categories: coding
tags:
 - coding
 - coding_interview
---

> Rerange all the numbers in a list, please print the minimum number of reranged list. For example, input the list `{3, 32, 321}`, you should print `321323`.

<!-- more -->

## Solution
```C++
void PrintMinArray(std::vector<int>& arr) {
  if (arr.empty()) {
    return;
  }
  std::sort(arr.begin(), arr.end(),
            [](int a, int b) {
              return std::stoi(std::to_string(a) + std::to_string(b)) < 
                     std::stoi(std::to_string(b) + std::to_string(a));
            });

  for (auto ele : arr) {
    std::cout << ele;
  }
  std::cout << std::endl;
}
```
