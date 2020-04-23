---
title: CodingInterview | 03 Duplication Number
mathjax: true
comments: true
date: 2020-04-22 23:52:24
categories: coding
---

> Find the duplicated number in a list. You are given a list with or without duplicated numbers. All the numbers in the list are positive. If there are duplicated numbers in the list, please output them; if not, return -1;

For example, `{2, 3, 5, 4, 2, 0, 1}`, the duplicated number is `2`.

## Solution 1
```C++
void swap(int &a, int &b) {
  int tmp = a;
  a = b;
  b = tmp;
}

int GetDuplicateNum(std::vector<int> &arr) {
  if (arr.empty()) {
    return -1;
  }

  for (int i = 0; i < arr.size(); ++i) {
    while (arr[i] != i) {
      if (arr[arr[i]] == arr[i]) {
        return arr[i];
      }
      swap(arr[arr[i]], arr[i]);
    }
  }

  return -1;
}
```

## Solution 2
The following method changes the input array, to protect the input array:
```C++
int NumCnt(const std::vector<int> &arr, const int start, const int end) {
  int cnt(0);
  for (auto num : arr) {
    if (num >= start && num <=end) {
      cnt++;
    }
  }
  return cnt;
}
  
int GetRangeDuplication(const std::vector<int> &arr, const int start,
                        const int end) {
  if (start == end) {
    return -1;
  }

  if (end - start == 1) {
    const int cnt_start = NumCnt(arr, start, start);
    return cnt_start > 1 ? start : end;
  }

  const int mid = (start + end) / 2;
  return NumCnt(arr, start, mid) > mid - start + 1 ? 
      GetRangeDuplication(arr, start, mid) : GetRangeDuplication(arr, mid, end);
}

int GetDuplicatedNum(const std::vector<int> &arr) {
  if (arr.empty()) {
    return -1;
  }

  return GetRangeDuplication(arr, 0, arr.size() - 1);
}

```
