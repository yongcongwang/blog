---
title: CodingInterview | 06 Print the Reverse of a Linked List
mathjax: true
comments: true
date: 2020-04-25 22:15:53
categories: coding
tags:
 - coding
 - coding_interview
---

> Please print the reverse of a linked list, for example, the linked list is `3->5->7->9`, then the output should be `9<-7<-5<-3`.
<!-- more -->
## Solution
```C++
void reverse_print(Node *node) {
  if (node == nullptr) {
    return;
  }

  if (node->next == nullptr) {
    std::cout << node->value << "<-";
    return;;
  }

  reverse_print(node->next);
  std::cout << node->value << "<-";
```
}
