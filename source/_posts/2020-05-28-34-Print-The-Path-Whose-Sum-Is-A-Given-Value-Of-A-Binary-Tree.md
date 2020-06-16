---
title: >-
  CodingInterview | 34 Print The Path Whose Sum Is A Given Value Of A Binary
  Tree
mathjax: true
comments: true
date: 2020-05-28 00:07:17
categories: coding
tags:
 - coding
 - coding_interview
---

> Input a binary tree and an integar, please print all the paths whose sum is the integar.
> For example, with the binary tree:
```C++
     10
    / \
   5  12
  / \ 
 4  7 
```
> and the sum integar 12, the path is `10 12` and `10 5 7`.
<!-- more -->

## Solution
```C++
struct BinNode {
  BinNode(int val = 0) : value(val), left(nullptr), right(nullptr) {}

  int value;
  BinNode* left;
  BinNode* right;
};

int SumStack(const std::vector<int>& path) {
  return std::accumulate(path.begin(), path.end(), 0);
}

void PrintStack(const std::vector<int>& path) {
  std::for_each(path.begin(), path.end(), 
                [](int ele) { std::cout << ele << " "; });
  std::cout << std::endl;
}

void PrintBinTreePathSum(
    const BinNode* root, const int sum, std::vector<int>& path) {
  path.push_back(root->value);
  if (root->left == nullptr && root->right == nullptr && SumStack(path) == sum) {
    PrintStack(path);
  }

  if (root->left != nullptr) {
    PrintBinTreePathSum(root->left, sum, path);
  }

  if (root->right != nullptr) {
    PrintBinTreePathSum(root->right, sum, path);
  }
  path.pop_back();
}

void PrintBinTreeSum(const BinNode* root, const int sum) {
  if (root == nullptr) {
    return;
  }

  std::vector<int> path;
  PrintBinTreePathSum(root, sum, path);
}
```
