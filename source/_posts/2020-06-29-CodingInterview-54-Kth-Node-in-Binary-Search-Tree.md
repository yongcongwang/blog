---
title: CodingInterview | 54 Kth Node in Binary Search Tree
categories: coding
tags:
  - coding_interview
mathjax: true
comments: true
date: 2020-06-29 00:30:34
---

> Please find the kth node of the binary search tree. For example, in the below tree:
```C++
    5
   / \
  3   7
 / \ / \
2  4 6  8
```
> the 3th node is 4
<!-- more -->

## Solution
```C++
struct Node {
  int value;
  Node* left;
  Node* right;

  Node(int val = 0) : value(val), left(nullptr), right(nullptr) {}
};

const Node* KthNodeRecurse(const Node* root, int& k) {
  if (root == nullptr) {
    return nullptr;
  }

  const Node* target = KthNodeRecurse(root->left, k);

  if (k == 1) {
    if (target != nullptr) {
      return target;
    }

    return root;
  }

  k--;
  target = KthNodeRecurse(root->right, k);

  return k == 1 && target != nullptr ? target : nullptr;
}

const Node* KthNode(const Node* root, int num) {
  if (root == nullptr || num < 1) {
    return nullptr;
  }

  return KthNodeRecurse(root, num);
}
```
