---
title: CodingInterview | 33 Check Binary Search Tree Post Order
mathjax: true
comments: true
date: 2020-05-27 00:30:42
categories: coding
---

> Please check if the list is a post order travesal result of a binary search tree.
> Assume that there are no repeated numbers in the list.
> For example, `{5, 7, 6, 9, 11, 10, 8}` is a post order travesal result of the binary search tree:
```C++
       8
      / \
     6  10 
    / \ / \
   5  7 9 11
```
> and, `{7, 4, 6, 5}` is not a post order travesal result of any binary search tree.

<!-- more -->

## Solution
```C++
bool IsBinSearchTreePostOrder(
    std::vector<int>::iterator it_begin, std::vector<int>::iterator it_end) {
  if (it_begin == it_end) {
    return true;
  }

  auto left_child = it_begin;
  while (left_child != it_end) {
    if (*left_child > *it_end) {
      break;
    }
    left_child++;
  }

  auto right_child = left_child;
  while (right_child != it_end) {
    if (*right_child < *it_end) {
      return false;
    }
    right_child++;
  }

  return IsBinSearchTreePostOrder(it_begin, left_child - 1) &&
         IsBinSearchTreePostOrder(left_child, it_end - 1);
}
```
