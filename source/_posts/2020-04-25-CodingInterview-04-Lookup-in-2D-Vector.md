---
title: CodingInterview | 04 Lookup in 2D Vector
mathjax: true
comments: true
date: 2020-04-25 00:55:39
categories: coding
---
> In a 2D vector, all the rows and colums are sorted. Please write a function to check if a number is in the vector.

For example, the following vector contains the number `7`, then the function returns true; as for `5`, the functions returns false;
<!-- more -->
## Solution
```C++
bool IsVectorContainNum(
    const std::vector<std::vector<int>> &arr, const int num) {
  if (arr.empty()) {
    return false;
  }

  int row = 0;
  int col = arr.front().size() - 1;

  while (row < arr.size() && col >=0) {
    if (arr[row][col] == num) {
      return true;
    } else if (arr[row][col] > num) {
      col--;
    } else {
      row++;
    }
  }

  return false;
}
```
