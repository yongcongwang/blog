---
title: CodingInterview | 32 Print A Binary Tree From Top To Bottom
mathjax: true
comments: true
date: 2020-05-24 01:03:35
categories: coding
---

## Print Binary Tree Without Line Split
> Print all nodes of a binary tree whithout line split, for the nodes in the same level, print them from left to right.
> For example, a binary tree:
```C++
       8
      / \
     6  10 
    / \ / \
   5  7 9 11
```
> should be printed as `8, 6, 10, 5, 7, 9, 11`.
<!-- more -->

### Solution
```C++
struct BinNode {
  BinNode(int val = 0) : value(val), left(nullptr), right(nullptr) {}

  int value;
  BinNode* left;
  BinNode* right;
};

void PrintBinTree(const BinNode* root) {
  if (root == nullptr) {
    return;
  }

  std::deque<const BinNode*> out;
  out.push_back(root);
  while (!out.empty()) {
    const BinNode* parrent = out.front();
    out.pop_front();
    std::cout << parrent->value << " ";

    if (parrent->left != nullptr) {
      out.push_back(parrent->left);
    }
    if (parrent->right != nullptr) {
      out.push_back(parrent->right);
    }
  }

  std::cout << std::endl;
}
```
