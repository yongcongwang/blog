---
title: CodingInterview | 22 Delete Last Kth Node In A List
mathjax: true
comments: true
date: 2020-05-16 17:26:52
categories: coding
tags:
 - coding
 - coding_interview
---

> Delete the last kth node of a list.
<!-- more -->
## Solution
```C++
#include <iostream>

struct Node {
  Node(int val = 0) : value(val), next(nullptr) {}
  int value;
  Node* next;

  Node* set_next(int val) {
    next = new Node(val);
    return next;
  }

  void output() {
    std::cout << value;
    if (next != nullptr) {
      std::cout << "->";
      next->output();
    } else {
      std::cout << std::endl;
    }
  }
};

Node* DeleteLastNthNode(Node* head, const int k) {
  if (head == nullptr || k < 1) {
    return nullptr;
  }

  int cnt(1);
  Node* kth_head = head;
  while (cnt++ < k) {
    if (kth_head->next != nullptr) {
      kth_head = kth_head->next;
    } else {
      return nullptr;
    }
  }

  Node* last_kth(head);
  Node* last_kth_front(nullptr);
  while (kth_head->next != nullptr) {
    kth_head = kth_head->next;
    last_kth_front = last_kth;
    last_kth = last_kth->next;
  }

  last_kth_front->next = last_kth->next;
  last_kth->next = nullptr;

  return last_kth;
}

int main() {
  Node* head1 = new Node(1);
  head1->set_next(2)->set_next(3)->set_next(4)->set_next(5);
  head1->output();
  DeleteLastNthNode(head1, 2)->output();
  head1->output();
}
```
