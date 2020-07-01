---
title: CodingInterview | 55 Depth of Binary Search Tree
categories: coding
tags:
  - coding interview
mathjax: true
comments: true
date: 2020-07-02 00:34:40
---

> Please ouput the maximum depth of a BST.

<!-- more -->

## Solution
```C++
struct Node {
  int value;
  Node* left;
  Node* right;

  Node(int val = 0) : value(val), left(nullptr), right(nullptr) {}
};

int DepthBinarySearchTree(Node* root) {
  if (root == nullptr) {
    return 0;
  }

  int left = DepthBinarySearchTree(root->left);
  int right = DepthBinarySearchTree(root->right);

  return left > right ? left + 1 : right + 1;
}
```
