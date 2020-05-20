---
title: CodingInterview | 28 The Symmetry Of A Binary Tree
mathjax: true
comments: true
date: 2020-05-20 21:18:35
categories: coding
---

> Check a symmetric binary tree. For example, the left is symmetric and the right is not.
```
    8          8    
   / \        / \   
  6   6      6   9
 / \ / \    / \ / \ 
5  7 7  5   5 7 7 5
```

<!-- more -->

## Solution
```C++
struct BinTreeNode {
 BinTreeNode(int val = 0) : value(val), left(nullptr), right(nullptr) {}

 int value;
 BinTreeNode* left;
 BinTreeNode* right;
};

bool IsSymmetryTwo(BinTreeNode* root1, BinTreeNode* root2) {
  if (root1 == nullptr && root2 == nullptr) {
    return true;
  }

  if (root1 == nullptr || root2 == nullptr) {
    return false;
  }

  if (root1->value != root2->value) {
    return false;
  }

  return IsSymmetryTwo(root1->left, root2->right) &&
         IsSymmetryTwo(root1->right, root2->left);
}

bool IsSymmetry(BinTreeNode* root) {
  return IsSymmetryTwo(root, root);
}
```
