---
title: CodingInterview | 18 Delete A Node In A List With The Time Complexity Of O(1)
mathjax: true
comments: true
date: 2020-05-13 00:12:21
categories: coding
tags:
 - coding
 - coding_interview
---

> With a head node pointer and a node pointer of a singly linked node, delete the node in $O(1)$ time.
<!-- more -->
## Solution
```C++
struct ListNode {
  ListNode(int value = 0) : value(value) {}

  int value;
  ListNode *next;
};

void DeleteLastNode(ListNode* header) {
  ListNode* curr_node = header;
  while (curr_node != nullptr) {
    if (curr_node->next->next == nullptr) {
      curr_node->next = nullptr;
      return;
    }
    curr_node = curr_node->next;
  }
}

void DeleteNode(ListNode* header, ListNode* del_node) {
  if (header == nullptr) {
    return;
  }
  if (header->next == nullptr) {
    header = nullptr;
    return;
  }

  if (del_node->next == nullptr) {
    DeleteLastNode(header);
    return;
  }

  ListNode* curr_node = header;
  while (curr_node != nullptr) {
    if (curr_node->next == del_node) {
      curr_node->next = del_node->next;
      return;
    }
    curr_node = curr_node->next;
  }
}
```
