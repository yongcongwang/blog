---
title: CodingInterview | 26 Subtree Of A Tree
mathjax: true
comments: true
date: 2020-05-19 23:40:24
categories: coding
---

> Input two binary trees A and B, please check if B is a subtree of A

<!-- more -->

## Solution
```C++
struct Tree {
  Tree(int value = 0) : value(value), left(nullptr), right(nullptr) {}

  int value;
  Tree* left;
  Tree* right;
};

bool IsSubTreeMatched(Tree* root, Tree* sub) {
  if (sub == nullptr) {
    return true;
  }

  if (root == nullptr) {
    return false;
  }

  return root->value == sub->value &&
         IsSubTreeMatched(root->left, sub->left) &&
         IsSubTreeMatched(root->right, sub->right);
}

bool IsSubTree(Tree* origin, Tree* sub) {
  if (origin == nullptr || sub == nullptr) {
    return false;
  }

  bool result = false;
  if (origin->value == sub->value) {
    result = IsSubTreeMatched(origin, sub);
  }

  return result || IsSubTree(origin->left, sub) ||
         IsSubTree(origin->right, sub);
}
```
