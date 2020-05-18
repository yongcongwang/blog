---
title: CodingInterview | 25 Merge Two Sorted Lists
mathjax: true
comments: true
date: 2020-05-18 23:26:07
categories: coding
---

> Please merege two sorted lists, the new list should also be sorted.
> For example, input node1: `1->3->5->7` and `2->4->6->8`, the new list should be `1->2->3->4->5->6->7->8`.

<!-- more -->

## Solution
```C++
Node* MergeTwoSortedLists(Node* head1, Node* head2) {
  if (head1 == nullptr) {
    return head2;
  }
  if (head2 == nullptr) {
    return head1;
  }

  Node* head;
  Node* curr_list1 = head1;
  Node* curr_list2 = head2;
  if (curr_list1->value < curr_list2->value) {
    head = curr_list1;
    curr_list1 = curr_list1->next;
  } else {
    head = curr_list2;
    curr_list2 = curr_list2->next;
  }

  Node* result = head;

  while (curr_list1 != nullptr && curr_list2 != nullptr) {
    if (curr_list1->value < curr_list2->value) {
      head->next = curr_list1;
      head = head->next;
      curr_list1 = curr_list1->next;
    } else {
      head->next = curr_list2;
      head = head->next;
      curr_list2 = curr_list2->next;
    }
  }

  if (curr_list1 != nullptr) {
    head->next = curr_list1;
  }
  if (curr_list2 != nullptr) {
    head->next = curr_list2;
  }

  return result;
}
```
