---
title: CodingInterview | 08 Next Node of Binary Tree in Inorder
mathjax: true
comments: true
date: 2020-04-29 00:51:16
categories: coding
---

> Given a binary tree and a node, please find the next node in inorder. The binary tree node has a pointer to its parent.

## Solution
```C++
struct BinaryTree {
  BinaryTree(int value = 0) 
      : value(value), parent(nullptr), left(nullptr), right(nullptr) {}
  int value;
  BinaryTree *parent;
  BinaryTree *left;
  BinaryTree *right;
};

BinaryTree *GetNextInorder(BinaryTree *node) {
  if (node == nullptr || node->parent == nullptr) {
    return nullptr;
  }

  if (node->right != nullptr) {
    BinaryTree *tmp = node->right;
    while (tmp->left != nullptr) {
      tmp = tmp->left;
    }
    return tmp;
  } else if (node == node->parent->left) {
    return node->parent;
  } else {
    BinaryTree *tmp = node;
    while (tmp->parent != nullptr && tmp != tmp->parent->left) {
      tmp = tmp->parent;
    }
    return tmp->parent == nullptr ? nullptr : tmp->parent;
  }
}
```
