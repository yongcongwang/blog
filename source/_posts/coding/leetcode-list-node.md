---
title: LeetCode Problems | Linked List
mathjax: true
date: 2020-08-19 00:23:27
---

# 2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

<!-- more -->
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```C++
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
## Solution
```C++
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      if (l1 == nullptr) {
        return l2;
      }
      if (l2 == nullptr) {
        return l1;
      }
      
      int carray = 0;
      ListNode* head = new ListNode();
      ListNode* curr = head;
      while (l1 != nullptr && l2 != nullptr) {
        int tmp = l1->val + l2->val + carray;
        curr->next = new ListNode(tmp % 10);
        carray = (tmp) / 10;
        curr = curr->next;
        l1 = l1->next;
        l2 = l2->next;
      }
      while (l1 != nullptr) {
        int tmp = l1->val + carray;
        curr->next = new ListNode(tmp % 10);
        carray = (tmp) / 10;
        curr = curr->next;
        l1 = l1->next;
      }
      while (l2 != nullptr) {
        int tmp = l2->val + carray;
        curr->next = new ListNode(tmp % 10);
        carray = (tmp) / 10;
        curr = curr->next;
        l2 = l2->next;
      }
      if (carray != 0) {
        curr->next = new ListNode(1);
      }
      
      return head->next;
    }
};
```

