---
title: 48 Length of the longest substring without repeated charactors
categories: coding
tags:
  - coding
  - coding_interview
mathjax: true
comments: true
date: 2020-06-18 21:20:09
---

> Please find the longest substring without repeated charactors of a string and output its length.
> Forexample, in string "arabcacfr" the longest substring without repeated charactors is "acfr", and its length is 4.

<!-- more -->

## Solution
```
int MaximumSubstringWithoutRepeat(const std::string& str) {
  if (str.empty()) {
    return 0;
  }

  std::unordered_map<char, int> substring_idxs;
  int max_length(0);
  int start_idx(0);

  for (int i = 0; i < str.size(); ++i) {
    auto it = substring_idxs.find(str[i]);
    if (it != substring_idxs.end()){
      const int new_start = it->second + 1;
      for (auto j = start_idx; j < new_start; ++j) {
        substring_idxs.erase(str[j]);
      }
      start_idx = new_start;
    }
    substring_idxs[str[i]] = i;
    max_length = std::max(max_length, i - start_idx + 1);
  }

  return max_length;
}
```
