---
title: CodingInterview | 36 Convert A Binary Search Tree To A Doubly Linked List
mathjax: true
comments: true
date: 2020-06-01 00:11:01
categories: coding
---

> Please convert a binary search tree to a doubly linked list. Creating new space is not allowed, and the doubly linked list should be sorted.
> For example, the binary search tree:
```C++
    10
   / \
  6   14
 / \ / \
4  8 12 16
```
> should be converted to:
```C++
  ->   ->   ->    ->    ->    -> 
4    6    8    10    12    14
  <-   <-   <-    <-    <-    <-
```
<!-- more -->

## Solution
```C++
struct Node {
  Node(int value = 0) : value(value), left(nullptr), right(nullptr) {}

  int value;
  Node* left;
  Node* right;
};

void Convert(Node* root, Node*& list_last) {
  if (root->left != nullptr) {
    Convert(root->left, list_last);
  }

  if (list_last == nullptr) {
    list_last = root;
    return;
  }

  list_last->right = root;
  root->left = list_last;
  list_last = root;

  if (root->right != nullptr) {
    Convert(root->right, list_last);
  }
}

Node* ConvertBinTreeToNodeList(Node* root) {
  if (root == nullptr) {
    return nullptr;
  }

  Node* list_last = nullptr;
  Convert(root, list_last);

  Node* result = root;
  while (result->left != nullptr) {
    result = result->left;
  }
  return result;
}
```
