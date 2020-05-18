---
title: CodingInterview | 12 Path in 2D Matrix
mathjax: true
comments: true
date: 2020-05-03 00:54:02
categories: coding
---

> Please design a function to check if a path exists in a 2D matrix. Path can start from any position, and it can expend to up/down/left/right cell. If the path passes by a cell, it can not do that again.
> For example, following 2d matrix contains the path `bfce`, but the path `abfb` is not in it.
```
a b t g
c f c s
j d e h
```
<!-- more -->
## Solution
```C++
bool IsPathInMatrixCore(
    const std::vector<std::vector<char>> &matrix,
    const int row, const int col, std::vector<std::vector<bool>> &map,
    const std::vector<char> &path, const int index) {
  if (index == path.size()) {
    return true;
  }

  bool result = false;
  // up
  int row_up = row - 1;
  if (row_up >=0 && map[row_up][col] && matrix[row_up][col] == path[index]) {
    auto temp = map;
    temp[row_up][col] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row_up, col, temp, path, index + 1);
  }
  // down
  int row_down = row + 1;
  if (row_down <= matrix.size() - 1 && map[row_down][col] &&
      matrix[row_down][col] == path[index]) {
    auto temp = map;
    temp[row_down][col] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row_down, col, temp, path, index + 1);
  }
  // left
  int col_left = col - 1;
  if (col_left >=0 && map[row][col_left] &&
      matrix[row][col_left] == path[index]) {
    auto temp = map;
    temp[row][col_left] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row, col_left, temp, path, index + 1);
  }

  // right
  int col_right = col + 1;
  if (col_right <= matrix.front().size() - 1 && map[row][col_right] &&
      matrix[row][col_right] == path[index]) {
    auto temp = map;
    temp[row][col_right] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row, col_right, temp, path, index + 1);
  }

  return result;
}

bool IsPathInMatrix(const std::vector<std::vector<char>> &matrix,
                    const std::vector<char> &path) {
  if (matrix.empty() || path.empty()) {
    return false;
  }

  std::vector<std::vector<bool>> map(
      matrix.size(), std::vector<bool>(matrix.front().size(), true));

  std::vector<char> path_to_find(path);

  for (int row = 0; row < matrix.size(); ++row) {
    for (int col = 0; col < matrix.front().size(); ++col) {
      if (matrix[row][col] == path.front()) {
        auto temp = map;
        temp[row][col] = false;
        return IsPathInMatrixCore(matrix, row, col, temp, path_to_find, 1);
      }
    }
  }

  return false;
}
```
