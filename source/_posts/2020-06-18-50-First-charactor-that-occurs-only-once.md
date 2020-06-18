---
title: 50 First charactor that occurs only once
categories: coding
tags:
  - coding
  - coding_interview
mathjax: true
comments: true
date: 2020-06-18 21:27:37
---

> Find the charactor that only occurs once in a string. For example, in "abaccdeff", 'b' occurs only once.

<!-- more -->

## Solution
```C++
char FirstNoRepeatChar(const std::string& str) {
  if (str.empty()) {
    return ' ';
  }

  std::unordered_map<char, int> map_char_cnt;
  for (const auto& c : str) {
    if (map_char_cnt.find(c) == map_char_cnt.end()) {
      map_char_cnt[c] = 1;
    } else {
      map_char_cnt[c] += 1;
    }
  }

  for (const auto& c : str) {
    if (map_char_cnt[c] == 1) {
      return c;
    }
  }

  return ' ';
}
```
