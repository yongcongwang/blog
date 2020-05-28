---
title: CodingInterview | 35 Copy Of Complex List Node
mathjax: true
comments: true
date: 2020-05-29 00:14:00
categories: coding
---

> Please realize a function to copy a complex list node. The defination of complex list node is as below:
```C++
struct Node {
  Node(int val = 0) : value(val), sibling(nullptr), next(nullptr) {}

  int value;
  Node* sibling;
  Node* next;
};
```

> And the picture is like this:
```C++
      +---------+
      |         |
+-+  +v+  +-+  +++  +-+
|A+-->B+-->C+-->D+-->E|
+++  +++  +^+  +-+  +^+
 |    |    |         |
 +---------+         |
      +--------------+
```
<!-- more -->

## Solution
```C++
void CopyEachNode(Node* origin) {
  Node* head = origin;
  while (head != nullptr) {
    Node* tmp = head->next;
    head->next = new Node(head->value);
    head->next->next = tmp;
    head = tmp;
  }
}

void CopySibingInfo(Node* origin) {
  Node* head = origin;
  while (head != nullptr) {
    Node* tmp = head->sibling;
    if (tmp != nullptr) {
      head->next->sibling = tmp->next;
    }
    head = head->next->next;
  }
}

Node* SplitTwoList(Node* origin) {
  Node* even_head = origin->next;
  Node* curr_odd = origin;
  Node* curr_even = even_head;
  Node* curr_node = even_head->next;
  int curr_node_cnt(1);
  while (curr_node != nullptr) {
    if (curr_node_cnt & 1) {
      curr_odd->next = curr_node;
      curr_odd = curr_odd->next;
    } else {
      curr_even->next = curr_node;
      curr_even = curr_even->next;
    }
    curr_node = curr_node->next;
    curr_node_cnt++;
  }

  return even_head;
}

Node* CopyNodeList(Node* origin) {
  if (origin == nullptr) {
    return nullptr;
  }

  CopyEachNode(origin);
  CopySibingInfo(origin);
  return SplitTwoList(origin);
}
```
