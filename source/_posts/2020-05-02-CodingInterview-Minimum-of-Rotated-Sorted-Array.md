---
title: CodingInterview | Minimum of Rotated Sorted Array
mathjax: true
comments: true
date: 2020-05-02 00:23:50
categories: coding
---

> The rotation is that putting a few elements ahead of the array to the end. With a rotated sorted array, please output the minimum of the array.
> For example, `{3, 4, 5, 1, 2}` is a rotation of `{1, 2, 3, 4, 5}` and its min value is `1`.

## Solution 1
Loop to find the minimum, and the time complexity is $O(n)$
```C++
int GetMinimumTravesal(const std::vector<int> &arr) {
  if (arr.empty()) {
    return 0;
  }

  int min = arr[0];
  for (auto &num : arr) {
    if (num < min) {
      min = num;
    }
  }

  return min;
}
```

## Solution 2
As we know the array is sorted, we can use the binary search to find the minimum, and the time complexity is $O(log(n))$
```C++
int GetMinimumBin(const std::vector<int> &arr, const int start_index, const int end_index) {
  if (start_index == end_index) {
    return arr[start_index];
  }

  if (end_index - start_index == 1) {
    return arr[start_index] < arr[end_index] ? arr[start_index] : arr[end_index];
  }

  int mid_index = (start_index + end_index) / 2;


  if (arr[start_index] == arr[mid_index] && arr[mid_index] == arr[end_index]) {
    return GetMinimumTravesal(arr);
  }

  if (arr[mid_index] >= arr[start_index]) {
    return GetMinimumBin(arr, mid_index, end_index);
  } else {
    return GetMinimumBin(arr, start_index, mid_index);
  }
}

int GetMinimumBinary(const std::vector<int> &arr) {
  if (arr.empty()) {
    return 0;
  }

  return GetMinimumBin(arr, 0, arr.size() - 1);
}
```
