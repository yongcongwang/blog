---
title: LeetCode Problems | Linked List
mathjax: true
categories:
  - coding
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
# 19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
> Given linked list: 1->2->3->4->5, and n = 2.
> After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
> Given n will always be valid.
Follow up:
> Could you do this in one pass?

## Solution
```C++
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
      if (head == nullptr || n < 1) {
        return nullptr;
      }
      
      ListNode* back = head;
      ListNode* front = head;
      
      while (n > 0 && front != nullptr) {
        front = front->next;
        --n;
      }
      if (n > 0) {
        return nullptr;
      }
      if (front == nullptr) {
        return back->next;
      }
      
      while (front->next != nullptr) {
        front = front->next;
        back = back->next;
      }
      
      back->next = back->next->next;
      return head;
    }
};
```
