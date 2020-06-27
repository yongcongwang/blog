---
title: CodingInterview | 52 First Public Node
categories: coding
tags:
  - coding_interview
mathjax: true
comments: true
date: 2020-06-27 21:16:00
---

> Input two node list, please find their first public node.
<!-- more -->

## Solution
```C++
struct Node {
  Node(int val = 0) : value(val), next(nullptr) {}
  int value;
  Node* next;
};

Node* FirstPublicNode(Node* first, Node* second) {
  if (first == nullptr || second == nullptr) {
    return nullptr;
  }

  int first_length(0);
  Node* tmp = first;
  while (tmp != nullptr) {
    first_length++;
    tmp = tmp->next;
  }

  int second_length(0);
  tmp = second;
  while (tmp != nullptr) {
    second_length++;
    tmp = tmp->next;
  }

  Node* head_first = first;
  Node* head_second = second;
  if (first_length > second_length) {
    int skip_cnt = first_length - second_length;
    while (skip_cnt > 0) {
      head_first = head_first->next;
      skip_cnt--;
    }
  } else {
    int skip_cnt = second_length - first_length ;
    while (skip_cnt > 0) {
      head_second = head_second->next;
      skip_cnt--;
    }
  }

  while (head_first != nullptr && head_second != nullptr) {
    if (head_first->value == head_second->value) {
      return head_first;
    }
    head_first = head_first->next;
    head_second = head_second->next;
  }
  return nullptr;
}
```
