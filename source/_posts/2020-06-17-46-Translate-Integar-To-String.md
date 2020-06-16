---
title: 46 Translate Integar To String
categories: coding
tags:
 - coding
 - coding_interview
mathjax: true
comments: true
date: 2020-06-17 01:11:06
---

> With an integar given, we translate the number digits to string with the rule: 0 to "a", 1 to "b", ..., 11 to "l", ..., 25 to "z". An integar may have more than one translation, for example, 12248 has 5 different translations: "bccfi", "bwfi", "bczi", "mcfi" and "mzi". Please find the number of translation methods of an integar.

<!-- more -->

```C++
std::size_t TransNumberToString(const std::size_t num) {
  const std::string num_str = std::to_string(num);

  const std::size_t length = num_str.size();
  std::vector<int> sum(length + 1, 0);
  sum[length - 1] = 1;
  sum[length] = 1;
  for (int i = length - 2; i >= 0; --i) {
    sum[i] = sum[i + 1];
    const int tmp = std::stoi(std::string(1, num_str[i]) +
                              std::string(1, num_str[i + 1]));
    if (tmp < 26) {
      sum[i] += sum[i + 2];
    }
  }

  return sum.front();
}
```
