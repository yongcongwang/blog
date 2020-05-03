---
title: CodingInterview | 13 Moving Count
mathjax: true
comments: true
date: 2020-05-03 10:57:54
categories: coding
---

> There is a $m * n$ matrix. A robot moves from $(0, 0)$ and it can move to left/right/up/down cell, but not the cell whose digital sum of row index and column index is bigger than k.
> For example, $k = 18$, robot can move to $(35, 37)$, because $3 + 5 + 3 + 7 = 18$. But it cannot move to $(35, 38)$, because $3 + 5 + 3 + 8 = 19 > 18$.
> How many cells the robot can reach?

## Solution
```C++
int GetDigitalSum(const int num) {
  int tmp = num;
  int sum = 0;
  while (tmp != 0) {
    sum += tmp % 10;
    tmp = tmp / 10;
  }
  return sum;
}

bool IsReachable(
    const int threshold, const int rows, const int cols, const int row,
    const int col, const std::vector<std::vector<bool>> &visited) {
  if (row >= 0 && row <= rows && col >= 0 && col <= cols &&
      GetDigitalSum(row) + GetDigitalSum(col) <= threshold &&
      !visited[row][col]) {
    return true;
  }
  return false;
}

int GetMovingCountCore(
    const int threshold, const int rows, const int cols, const int row,
    const int col, std::vector<std::vector<bool>> &visited) {
  int count = 0;
  if (IsReachable(threshold, rows, cols, row, col, visited)) {
    visited[row][col] = true;
    count = 1 + 
            GetMovingCountCore(threshold, rows, cols, row - 1, col, visited) +
            GetMovingCountCore(threshold, rows, cols, row + 1, col, visited) +
            GetMovingCountCore(threshold, rows, cols, row, col - 1, visited) +
            GetMovingCountCore(threshold, rows, cols, row, col + 1, visited);
  }
  return count;
}

int GetMovingCount(const int threshold, const int rows, const int cols) {
  if (threshold < 0 || rows < 0 || cols < 0) {
    return 0;
  }

  std::vector<std::vector<bool>> visited(
      rows + 1, std::vector<bool>(cols + 1, false));
  return GetMovingCountCore(threshold, rows, cols, 0, 0, visited);
}
```
