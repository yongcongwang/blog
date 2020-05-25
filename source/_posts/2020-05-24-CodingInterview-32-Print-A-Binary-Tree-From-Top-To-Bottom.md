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

## Print Binary Tree With Line Split
> Please print the binary tree with line split, the output of the tree is:
```C++
8
6 10
5 7 9 11
```

### Solution
```C++
void PrintBinTreeLineSplit(const BinNode* root) {
  if (root == nullptr) {
    return;
  }

  std::deque<const BinNode*> out;
  out.push_back(root);
  std::size_t curr_level_cnt = 1;
  std::size_t next_level_cnt = 0;
  while (!out.empty()) {
    const BinNode* parrent = out.front();
    out.pop_front();
    std::cout << parrent->value << " ";
    curr_level_cnt--;

    if (parrent->left != nullptr) {
      out.push_back(parrent->left);
      next_level_cnt++;
    }
    if (parrent->right != nullptr) {
      out.push_back(parrent->right);
      next_level_cnt++;
    }

    if (curr_level_cnt == 0) {
      std::cout << std::endl;
      curr_level_cnt = next_level_cnt;
      next_level_cnt = 0;
    }
  }

  std::cout << std::endl;
}
```

## Print Binary Tree in z order
> Please print the binary tree with line split in z order, the output of the tree is:
```C++
8
6 10
5 7 9 11
```

### Solution
```C++
void PrintBinTreeLineZ(const BinNode* root) {
  if (root == nullptr) {
    return;
  }

  std::array<std::stack<const BinNode*>, 2> out;
  std::size_t curr_index = 0;
  std::size_t next_index = 1;
  out[curr_index].push(root);
  while (!out[0].empty() || !out[1].empty()) {
    const BinNode* parrent = out[curr_index].top();
    out[curr_index].pop();
    std::cout << parrent->value << " ";

    if (curr_index == 0) {
      if (parrent->left != nullptr) {
        out[next_index].push(parrent->left);
      }
      if (parrent->right != nullptr) {
        out[next_index].push(parrent->right);
      }
    } else {
      if (parrent->right != nullptr) {
        out[next_index].push(parrent->right);
      }
      if (parrent->left != nullptr) {
        out[next_index].push(parrent->left);
      }
    }

    if (out[curr_index].empty()) {
      std::cout << std::endl;
      curr_index = 1 - curr_index;
      next_index = 1 - next_index;
    }
  }

  std::cout << std::endl;
}
```
