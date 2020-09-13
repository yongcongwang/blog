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
Input: (2 -4 -3) + (5 -6 -4)
Output: 7 -0 -8
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
```C++
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
```

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
      
      while (n 0 && front != nullptr) {
        front = front->next;
        --n;
      }
      if (n 0) {
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

# 21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:
```C++
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
      if (l1 == nullptr) {
        return l2;
      }
      if (l2 == nullptr) {
        return l1;
      }
      
      ListNode* head = nullptr;
      if (l1->val < l2->val) {
        head = l1;
        l1 = l1->next;
      } else {
        head = l2;
        l2 = l2->next;
      }
      
      ListNode* curr = head;
      while (l1 != nullptr && l2 != nullptr) {
        if (l1->val < l2->val) {
          curr->next = l1;
          curr = curr->next;
          l1 = l1->next;
        } else {
          curr->next = l2;
          curr = curr->next;
          l2 = l2->next;
        }
      }
      if (l1 != nullptr) {
        curr->next = l1;
      }
      if (l2 != nullptr) {
        curr->next = l2;
      }
      
      return head;
        
    }
};
```

# 23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
```C++
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```
Example 2:
```C++
Input: lists = []
Output: []
```
Example 3:
```C++
Input: lists = [[]]
Output: []
```

Constraints:

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length won't exceed 10^4.

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
      if (lists.empty()) {
        return nullptr;
      }
      int min_val = numeric_limits<int>::max();
      int min_idx = 0;
      for (size_t i = 0; i < lists.size(); ++i) {
        if (lists[i] != nullptr && lists[i]->val < min_val) {
          min_val = lists[i]->val;
          min_idx = i;
        }
      }
      if (min_val == numeric_limits<int>::max()) {
        return nullptr;
      }
      
      ListNode* head = lists[min_idx];
      lists[min_idx] = lists[min_idx]->next;
      head->next = mergeKLists(lists);
      return head;
    }
};
```

# 1171. Remove Zero Sum Consecutive Nodes from Linked List
Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.

Example 1:
```C++
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
```

Example 2:
```C++
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
```

Example 3:
```C++
Input: head = [1,2,3,-3,-2]
Output: [1]
```

Constraints:
- The given linked list will contain between `1` and `1000` nodes.
- Each node in the linked list has `-1000 <= node.val <= 1000`.

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  ListNode* removeZeroSumSublists(ListNode* head) {
    if (head == nullptr) {
      return head;
    }
    
    ListNode dump(0);
    dump.next = head;
    
    int sum = 0;
    unordered_map<int, ListNode*sum_node{{0, &dump}};
    while (head != nullptr) {
      sum += head->val;
      sum_node[sum] = head;
      head = head->next;
    }
    
    sum = 0;
    head = &dump;
    while (head != nullptr) {
      sum += head->val;
      ListNode* matching_node = sum_node[sum];
      if (matching_node != head) {
        head->next = matching_node->next;
      }
      head = head->next;
    }
    
    return dump.next;
  }
};
```

# 1290. Convert Binary Number in a Linked List to Integer
Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
```C++
1 -> 0 -> 1

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
```
Example 2:
```C++
Input: head = [0]
Output: 0
```

Example 3:
```C++
Input: head = [1]
Output: 1
```

Example 4:
```C++
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
```

Example 5:
```C++
Input: head = [0,0]
Output: 0
```

Constraints:
- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.
