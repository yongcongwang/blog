---
title: CodingInterview | 23 Find The Entrance Of A Loop In A Node List
mathjax: true
comments: true
date: 2020-05-17 01:25:16
categories: coding
---

> If a node list contains a loop, how to find the entrance? 
> For example, the following node list has the loop entrnace of node 3.
> `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3`
<!-- more -->
## Solution
```C++
struct Node {
  Node(int val = 0) : value(val), next(nullptr) {}
  int value;
  Node* next;

  Node* set_next(int val) {
    next = new Node(val);
    return next;
  }
};

Node* GetOneLoopNode(Node* head) {
  if (head == nullptr) {
    return nullptr;
  }

  Node* slow = head;
  Node* fast = head;

  while (fast->next && fast->next->next) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) {
      return slow;
    }
  }

  return nullptr;
}

int GetLoopCnt(Node* node) {
  if (node == nullptr) {
    return 0;
  }
  int cnt(1);
  Node* head = node;
  while (head->next != nullptr) {
    if (head->next == node) {
      return cnt;
    } else {
      cnt++;
      head = head->next;
    }
  }
  return 0;
}

Node* GetLoopEntrance(Node* head) {
  if (head == nullptr) {
    return nullptr;
  }

  Node* node_in_loop = GetOneLoopNode(head);
  if (node_in_loop == nullptr) {
    return nullptr;
  }

  const int loop_cnt = GetLoopCnt(node_in_loop);

  Node* fast = head;
  Node* slow = head;
  for (auto i = 0; i < loop_cnt; ++i) {
    fast = fast->next;
  }

  while (fast != slow) {
    fast = fast->next;
    slow = slow->next;
  }

  return fast;
}
```
