---
title: CodingInterview | 37 Serialize And Deserialize A Binary Tree
mathjax: true
comments: true
date: 2020-06-01 00:58:54
categories: coding
---

> Please realize two functions to serialize and deserialize a binary tree.

<!-- more -->

## Solution
```C++
constexpr int INVALID_INT = -255;

struct Node {
  Node(int value = 0) : value(value), left(nullptr), right(nullptr) {}

  int value;
  Node* left;
  Node* right;
};

void Serialize(Node* root, std::queue<int>& ser) {
  if (root == nullptr) {
    ser.push(INVALID_INT);
    return;
  }

  ser.push(root->value);
  Serialize(root->left, ser);
  Serialize(root->right, ser);
}

void Deserialize(Node*& root, std::queue<int>& ser) {

  if (!ser.empty() && ser.front() != INVALID_INT) {
    root = new Node(ser.front());
    ser.pop();

    Deserialize(root->left, ser);
    Deserialize(root->right, ser);
  } else {
    ser.pop();
  }
}
```
