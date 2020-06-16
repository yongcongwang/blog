---
title: CodingInterview | 27 The Mirror Of A BinaryTree
mathjax: true
comments: true
date: 2020-05-20 00:03:25
categories: coding
tags:
 - coding
 - coding_interview
---

> Please realize a function to output the mirror of a binary tree.
> For example, input tree is left one, and output tree is right one.

```C++
    8          8    
   / \        / \   
  6  10      10  6  
 / \ / \    / \ / \ 
5  7 9 11  11 9 7  5
```

<!-- more -->

## Solution
```C++
void MirrorBinaryTree(BinaryTreeNode* root) {
  if (root == nullptr) {
    return;
  }

  BinaryTreeNode* tmp = root->left;
  root->left = root->right;
  root->right = tmp;

  MirrorBinaryTree(root->left);
  MirrorBinaryTree(root->right);
}
```
