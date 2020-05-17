---
title: CodingInterview | 24 Reverse Node List
mathjax: true
comments: true
date: 2020-05-18 00:51:15
categories: coding
---

> Realize a function to reverse a node list. Input a head pointer of a node list, please output a pointer of the reversed node list head.

## Solution
```C++
struct Node {
  Node(int val = 0) : value(val) {}

  int value;
  Node* next;
};


Node* ReverseNodeList(Node* head) {
  if (head == nullptr || head->next == nullptr) {
    return head;
  }

  Node* prev_node = head;
  Node* curr_node = head->next;

  Node* next_node(nullptr);
  prev_node->next = nullptr;
  while (curr_node != nullptr) {
    next_node = curr_node->next;
    curr_node->next = prev_node;

    prev_node = curr_node;
    curr_node = next_node;
  }

  return prev_node;
}
```
