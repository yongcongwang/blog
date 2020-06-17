---
title: 47 Maximum Gift Value
categories: coding
tags:
  - coding
  - coding_interview
mathjax: true
comments: true
date: 2020-06-17 22:11:44
---

> Every grid of a 2d vector has a gift, and every gift has a value(bigger than 0). You start from the top left of vector exit from right bottom. So what's the maximum gift value you can get?
> For example, a 2d vector like:
```C++
1 10 3 8
12 2 9 6
5 7 4 11
3 7 16 5
```
> you can get the maximum git value if you go through: `1 -> 12 -> 5 -> 7 -> 7 -> 16 -> 5`.

<!-- more -->

## Solution
```C++
int MaxGiftValue(const std::vector<std::vector<int>>& map) {
  if (map.empty()) {
    return 0;
  }

  const int row_cnt = map.size();
  const int col_cnt = map.front().size();
  std::vector<std::vector<int>> gift_values(
      row_cnt, std::vector<int>(col_cnt, 0));

  for (int i = 0; i < row_cnt; ++i) {
    for (int j = 0; j < col_cnt; ++j) {
      const int left = j - 1 >= 0 ? gift_values[i][j - 1] : 0;
      const int up = i - 1 >= 0 ? gift_values[i - 1][j] : 0;

      gift_values[i][j] = std::max(left, up) + map[i][j];
    }
  }

  return gift_values.back().back();
}
```
