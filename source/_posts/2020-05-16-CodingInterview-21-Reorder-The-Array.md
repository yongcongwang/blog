---
title: CodeInterview | 21 Reorder The Array
mathjax: true
comments: true
date: 2020-05-16 01:56:17
categories: coding
---

> Input an array of integar, please reorder the array so that all the odd numbers are in the first half part, and all the even numbers are in the latter half part.
> For example, after reordering, {1, 2, 3, 4, 5} may change to {1, 3, 5, 2, 4}.

## Solution
```C++
#include <algorithm>
#include <vector>

bool IsOdd(const int& num) {
  return num & 0x01;
}

void ReorderOddEven(std::vector<int>& arr, bool (*func)(const int& num)) {
  if (arr.empty()) {
    return;
  }

  int left(0);
  int right(arr.size() - 1);

  while (left < right) {
    while (left < arr.size() && func(arr[left])) {
      left++;
    }
    while (right >= 0 && !func(arr[right])) {
      right--;
    }
    if (left < right) {
      std::swap(arr[left], arr[right]);
    }
  }
}

int main() {
  std::vector arr1{1, 2, 3, 4, 5};
  std::vector arr2{2, 3, 4, 5, 6};

  ReorderOddEven(arr1, IsOdd);
  ReorderOddEven(arr2, IsOdd);
}
```
