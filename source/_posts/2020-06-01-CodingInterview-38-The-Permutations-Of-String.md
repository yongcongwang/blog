---
title: CodingInterview | 38 The Permutations Of String
mathjax: true
comments: true
date: 2020-06-01 22:02:37
categories: coding
---

> Please print all the permutations of a string. For example, "abc" can be:
> abc, acb, bac, bca, cab and cba.

<!-- more -->

## Solution
```C++
void PrintPermutations(std::string& str, const int curr_index) {
  if (curr_index == str.size() - 1) {
    std::cout << str << std::endl;
  } else {
    for (int i = curr_index; i < str.size(); ++i) {
      std::swap(str[curr_index], str[i]);
      PrintPermutations(str, curr_index + 1);
      std::swap(str[curr_index], str[i]);
    }
  }
}

void PrintAllPermutations(const std::string& str) {
  if (str.empty()) {
    return;
  }

  std::string tmp(str);
  PrintPermutations(tmp, 0);
}
```
