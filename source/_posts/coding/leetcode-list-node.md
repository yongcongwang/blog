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

# 24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:
```C++
Given 1->2->3->4, you should return the list as 2->1->4->3.
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
    ListNode* swapPairs(ListNode* head) {
      if (head == nullptr || head->next == nullptr) {
        return head;
      }
      ListNode* new_head = head->next;
      head->next = head->next->next;
      new_head->next = head;
      head->next = swapPairs(head->next);
      return new_head;
    }
};
```

# 25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
```C++
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
```
Note:

- Only constant extra memory is allowed.
- You may not alter the values in the list's nodes, only nodes itself may be changed.

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
    ListNode* reverseKGroup(ListNode* head, int k) {
      if (head == nullptr) {
        return nullptr;
      }
      if (k == 1) {
        return head;
      }
      ListNode* tail = head;
      int cnt = k;
      while (tail != nullptr && cnt > 1) {
        tail = tail->next;
        --cnt;
      }
      if (tail == nullptr) {
        return head;
      }
      ListNode* behind_k = head;
      ListNode* new_head = head;
      cnt = k;
      while (cnt > 1) {
        ListNode* tmp = behind_k->next;
        behind_k->next = behind_k->next->next;
        tmp->next = new_head;
        new_head = tmp;
        --cnt;
      }
      behind_k->next = reverseKGroup(behind_k->next, k);
      return new_head;
    }
};
```

# 61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
```C++
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```
Example 2:
```C++
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
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
    ListNode* rotateRight(ListNode* head, int k) {
      if (head == nullptr || k < 1) {
        return head;
      }
      int cnt = 1;
      ListNode* curr = head;
      while (curr->next != nullptr) {
        curr = curr->next;
        ++cnt;
      }
      k = k % cnt;
      if (k < 1) {
        return head;
      }
      ListNode* front = head;
      ListNode* back = head;
      while (k > 0) {
        front = front->next;
        --k;
      }
      
      while (front->next != nullptr) {
        front = front->next;
        back = back->next;
      }
      
      ListNode* new_head = back->next;
      back->next = nullptr;
      front->next = head;
      
      return new_head;
    }
};
```

# 82. Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:
```C++
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```
Example 2:
```C++
Input: 1->1->1->2->3
Output: 2->3
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
    ListNode* deleteDuplicates(ListNode* head) {
      if (head == nullptr) {
        return nullptr;
      }
      if (head->next == nullptr) {
        return head;
      }
      if (head->val != head->next->val) {
        head->next = deleteDuplicates(head->next);
        return head;
      }
      ListNode* first_diff = head;
      while (first_diff != nullptr && first_diff->val == head->val) {
        first_diff = first_diff->next;
      }
      if (first_diff == nullptr) {
        return nullptr;
      }
      return deleteDuplicates(first_diff);
    }
};
```

# 83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
```C++
Input: 1->1->2
Output: 1->2
```
Example 2:
```C++
Input: 1->1->2->3->3
Output: 1->2->3
```

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode* deleteDuplicates(ListNode* head) {
    auto *out = head;
    while (head != nullptr && head->next != nullptr) {
      if (head->val == head->next->val) {
        head->next = head->next->next;
      } else {
        head = head->next;
      }
    }
    return out;
  }
};
```

# 86. Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
```C++
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
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
  ListNode* partition(ListNode* head, int x) {
    if (head == nullptr || head->next == nullptr) {
      return head;
    }
    
    ListNode before_head;
    ListNode* before = &before_head;
    ListNode after_head;
    ListNode* after = &after_head;
    
    while (head != nullptr) {
      if (head->val < x) {
        before->next = head;
        before = before->next;
      } else {
        after->next = head;
        after = after->next;
      }
      head = head->next;
    }
    
    after->next = nullptr;
    before->next = after_head.next;
    return before_head.next;
  }
};
```

# 92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
```C++
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
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
  ListNode* reverseBetween(ListNode* head, int m, int n) {
    if (m == n) {
      return head;
    }
    ListNode* curr = head;
    ListNode* first_tail = nullptr;
    ListNode* second_head = nullptr;
    ListNode* second_tail = nullptr;
    for (int i = 1; curr != nullptr; ++i) {
      if (i + 1 == m) {
        first_tail = curr;
      }
      if (i == m) {
        second_head = curr;
        second_tail = curr;
        curr = curr->next;
        second_tail->next = nullptr;
        continue;
      }
      if (i > m && i <= n) {
        ListNode* tmp = curr;
        curr = curr->next;
        tmp->next = second_head;
        second_head = tmp;
        continue;
      }
      if (i > n) {
        break;
      }
      curr = curr->next;
    }
    
    second_tail->next = curr;
    if (m == 1) {
      return second_head;
    }
    first_tail->next = second_head;
    return head;
  }
};
```

# 109. Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
![pic](https://assets.leetcode.com/uploads/2020/08/17/linked.jpg)
```C++
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
```
Example 2:
```C++
Input: head = []
Output: []
```
Example 3:
```C++
Input: head = [0]
Output: [0]
```
Example 4:
```C++
Input: head = [1,3]
Output: [3,1]
```
Constraints:

- The number of nodes in head is in the range [0, 2 * 104].
- -10^5 <= Node.val <= 10^5

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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
      if (head == nullptr) {
        return nullptr;
      }
      if (head->next == nullptr) {
        return new TreeNode(head->val);
      }
      if (head->next->next == nullptr) {
        TreeNode* root = new TreeNode(head->next->val);
        root->left = new TreeNode(head->val);
        return root;
      }
      
      ListNode dump(0);
      dump.next = head;
      
      ListNode* prev_slow = &dump;
      ListNode* slow = head;
      ListNode* fast = head;
      
      while (fast->next != nullptr && fast->next->next != nullptr) {
        prev_slow = prev_slow->next;
        slow = slow->next;
        fast = fast->next->next;
      }
      if (fast->next != nullptr) {
        fast = fast->next;
      }
      prev_slow->next = nullptr;
      
      TreeNode* root = new TreeNode(slow->val);
      root->left = sortedListToBST(head);
      root->right = sortedListToBST(slow->next);
      return root;
    }
};
```

# 138. Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

- val: an integer representing Node.val
- random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

Example 1:
![pic](https://assets.leetcode.com/uploads/2019/12/18/e1.png)
```C++
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```
Example 2:
![pic](https://assets.leetcode.com/uploads/2019/12/18/e2.png)
```C++
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```
Example 3:
![pic](https://assets.leetcode.com/uploads/2019/12/18/e3.png)
```C++
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```
Example 4:
```C++
Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
```
Constraints:

- -10000 <= Node.val <= 10000
- Node.random is null or pointing to a node in the linked list.
- Number of Nodes will not exceed 1000.

## Solution
```C++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
  Node* copyRandomList(Node* head) {
    if (head == nullptr) {
      return head;
    }
    
    Node* curr = head;
    while (curr != nullptr) {
      Node* next = curr->next;
      curr->next = new Node(curr->val);
      curr->next->next = next;
      curr = next;
    }
    curr = head;
    while (curr != nullptr) {
      Node* random = curr->random;
      if (random == nullptr) {
        curr = curr->next->next;
        continue;
      }
      curr->next->random = random->next;
      curr = curr->next->next;
    }
    curr = head;
    Node* new_head = curr->next;
    Node* new_curr = new_head;
    while (curr->next->next != nullptr) {
      curr->next = curr->next->next;
      curr = curr->next;
      new_curr->next = curr->next;
      new_curr = new_curr->next;
    }
    curr->next = nullptr;
    new_curr->next = nullptr;
    
    return new_head;
  }
};
```

# 141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

Constraints:

- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
      if (head == nullptr) {
        return false;
      }
      
      ListNode* slow = head;
      ListNode* fast = head;
      
      while (fast->next != nullptr && fast->next->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
          return true;
        }
      }
      
      return false;
    }
};
```

# 142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

Constraints:

- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
      if (head == nullptr) {
        return nullptr;
      }
      
      ListNode* slow = head;
      ListNode* fast = head;
      while (fast->next != nullptr && fast->next->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
          break;
        }
      }
      
      if (fast->next == nullptr || fast->next->next == nullptr) {
        return nullptr;
      }
      
      slow = head;
      while (slow != fast) {
        slow = slow->next;
        fast = fast->next;
      }
      return slow;
    }
};
```

# 143. Reorder List
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
Example 1:
```C++
Given 1->2->3->4, reorder it to 1->4->2->3.
```
Example 2:
```C++
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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
    void reorderList(ListNode* head) {
      if (head == nullptr || head->next == nullptr) {
        return;
      }
      
      ListNode* slow = head;
      ListNode* fast = head->next;
      while (fast->next != nullptr && fast->next->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
      }
      
      ListNode* second_head = nullptr;
      if (fast->next == nullptr) {
        second_head = slow->next;
        slow->next = nullptr;
      } else {
        second_head = slow->next->next;
        slow->next->next = nullptr;
      }
      
      ListNode* curr = second_head->next;
      second_head->next = nullptr;
      while (curr != nullptr) {
        ListNode* next = curr->next;
        curr->next = second_head;
        second_head = curr;
        curr = next;
      }
      
      curr = head;
      ListNode* sec_curr = second_head;
      while (curr != nullptr && sec_curr != nullptr) {
        ListNode* first_next = curr->next;
        ListNode* second_next = sec_curr->next;
        curr->next = sec_curr;
        sec_curr->next = first_next;
        curr = first_next;
        sec_curr = second_next;
      }
      
    }
};
```

# 147. Insertion Sort List
Sort a linked list using insertion sort.
Algorithm of Insertion Sort:

- Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
- At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
- It repeats until no input elements remain.

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
    ListNode* insertionSortList(ListNode* head) {
      if (head == nullptr || head->next == nullptr) {
        return head;
      }
      
      ListNode dump(-1);
      dump.next = head;
      ListNode* sorted_tail = head;
      ListNode* to_insert = head->next;
      head->next = nullptr;
      while (to_insert != nullptr) {
        ListNode* next_node = to_insert->next;
        to_insert->next = nullptr;
        
        ListNode* sorted_curr = &dump;
        while (sorted_curr != nullptr &&
               sorted_curr->next != nullptr &&
               sorted_curr->next->val < to_insert->val) {
          sorted_curr = sorted_curr->next;
        }
        ListNode* tmp = sorted_curr->next;
        sorted_curr->next = to_insert;
        to_insert->next = tmp;
        
        to_insert = next_node;
      }
      
      return dump.next;
    }
};
```

# 148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
```C++
Input: 4->2->1->3
Output: 1->2->3->4
```
Example 2:
```C++
Input: -1->5->3->4->0
Output: -1->0->3->4->5
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
  ListNode* MergeTwoSortedList(ListNode* head1, ListNode* head2) {
    if (head1 == nullptr) {
      return head2;
    }
    if (head2 == nullptr) {
      return head1;
    }
    
    ListNode* head = nullptr;
    if (head1->val < head2->val) {
      head = head1;
      head1 = head1->next;
    } else {
      head = head2;
      head2 = head2->next;
    }
    
    ListNode* curr = head;
    while (head1 != nullptr && head2 != nullptr) {
      if (head1->val < head2->val) {
        curr->next = head1;
        head1 = head1->next;
        curr = curr->next;
      } else {
        curr->next = head2;
        head2 = head2->next;
        curr = curr->next;
      }
    }
    
    if (head1 != nullptr) {
      curr->next =  head1;
    }
    if (head2 != nullptr) {
      curr->next = head2;
    }
    
    return head;
  }
  
  ListNode* sortList(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
      return head;
    }

    ListNode* slow = head;
    ListNode* fast = head->next;

    while (fast->next != nullptr && fast->next->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
    }
    ListNode* tmp = slow->next;
    slow->next = nullptr;
    ListNode* first_head = sortList(head);
    ListNode* second_head = sortList(tmp);
    return MergeTwoSortedList(first_head, second_head);
  }
};
```

# 160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
![pic](https://assets.leetcode.com/uploads/2018/12/13/160_statement.png)
begin to intersect at node c1.

Example 1:
![pic](https://assets.leetcode.com/uploads/2020/06/29/160_example_1_1.png)
```C++
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
```
Example 2:
![pic](https://assets.leetcode.com/uploads/2020/06/29/160_example_2.png)
```C++
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
``` 
Example 3:
![pic](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)
```C++
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
```

Notes:

- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Each value on each linked list is in the range [1, 10^9].
- Your code should preferably run in O(n) time and use only O(1) memory.

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    if (headA == nullptr || headB == nullptr) {
      return nullptr;
    }
    ListNode* curr_a = headA;
    int a_cnt = 0;
    while (curr_a != nullptr) {
      curr_a = curr_a->next;
      ++a_cnt;
    }
    
    ListNode* curr_b = headB;
    int b_cnt = 0;
    while (curr_b != nullptr) {
      curr_b = curr_b->next;
      ++b_cnt;
    }
    if (curr_a != curr_b) {
      return nullptr;
    }
    
    curr_a = headA;
    curr_b = headB;
    while (a_cnt != b_cnt) {
      if (a_cnt > b_cnt) {
        curr_a = curr_a->next;
        --a_cnt;
      } else {
        curr_b = curr_b->next;
        --b_cnt;
      }
    }
    while (curr_a != curr_b) {
      curr_a = curr_a->next;
      curr_b = curr_b->next;
    }
    return curr_a;
  }
};
```

# 203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example:
```C++
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode* removeElements(ListNode* head, int val) {
    if (head == nullptr) {
      return head;
    }
    
    if (head->val == val) {
      return removeElements(head->next, val);
    }
    
    if (head->next == nullptr) {
      return head;
    }
    
    if (head->next->val == val) {
      head->next = removeElements(head->next->next, val);
    } else {
      head->next = removeElements(head->next, val);
    }
    
    return head;
  }
};
```

# 206. Reverse Linked List

Reverse a singly linked list.

Example:
```C++
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  ListNode* reverseList(ListNode* head) {
    if (!head || !head->next) {
      return head;
    }

    ListNode *newHead = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return newHead;
  }
};
```

# 234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:
```C++
Input: 1->2
Output: false
```
Example 2:
```C++
Input: 1->2->2->1
Output: true
```
Follow up:
Could you do it in O(n) time and O(1) space?

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  bool isPalindrome(ListNode* head) {
    if (!head || !head->next) {
      return true;
    }
    
    auto *fast = head;
    auto *slow = head;
    while (fast && fast->next) {
      fast = fast->next->next;
      slow = slow->next;
    }
    
    if (fast) {
      slow = slow->next;
    }
    
    auto *head_curr = slow;
    auto *head_next = slow->next;
    head_curr->next = nullptr;
    
    while (head_next) {
      auto *tmp = head_curr;
      head_curr = head_next;
      head_next = head_next->next;
      head_curr->next = tmp;
    }
    
    while (head_curr) {
      if (head_curr->val != head->val) {
        return false;
      }
      head_curr = head_curr->next;
      head = head->next;
    }
    
    return true;
  }
};
```

# 237. Delete Node in a Linked List
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
![pic](https://assets.leetcode.com/uploads/2020/09/01/node1.jpg)
```C++
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```
Example 2:
![pic](https://assets.leetcode.com/uploads/2020/09/01/node2.jpg)
```C++
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```
Example 3:
```C++
Input: head = [1,2,3,4], node = 3
Output: [1,2,4]
```
Example 4:
```C++
Input: head = [0,1], node = 0
Output: [1]
```
Example 5:
```C++
Input: head = [-3,5,-99], node = -3
Output: [5,-99]
```
Constraints:

- The number of the nodes in the given list is in the range [2, 1000].
- -1000 <= Node.val <= 1000
- The value of each node in the list is unique.
- The node to be deleted is in the list and is not a tail node

## Solution
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  void deleteNode(ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;
  }   
};
```

# 328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
```C++
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```
Example 2:
```C++
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
```
Constraints:

- The relative order inside both the even and odd groups should remain as it was in the input.
- The first node is considered odd, the second node even and so on ...
- The length of the linked list is between [0, 10^4].

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
  ListNode* oddEvenList(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
      return head;
    }
    
    ListNode* odd_head = head;
    ListNode* odd_tail = head;
    ListNode* even_head = head->next;
    ListNode* even_tail = head->next;
    head = head->next->next;
    
    int flag = 0;
    while (head != nullptr) {
      if (flag == 0) {
        odd_tail->next = head;
        head = head->next;
        odd_tail = odd_tail->next;
      } else {
        even_tail->next = head;
        head = head->next;
        even_tail = even_tail->next;
      }
      flag = 1 - flag;
    }
    
    odd_tail->next = even_head;
    even_tail->next = nullptr;
    return odd_head;
  }
};
```

# 430. Flatten a Multilevel Doubly Linked List
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Example 1:
```C++
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:
```
![pic](https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlist.png)
```C++
After flattening the multilevel linked list it becomes:
```
![pic](https://assets.leetcode.com/uploads/2018/10/12/multilevellinkedlistflattened.png)

Example 2:
```C++
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
```
Example 3:
```C++
Input: head = []
Output: []
``` 
How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:
```C++
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
```
The serialization of each level is as follows:
```C++
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
```
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
```C++
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
```
Merging the serialization of each level and removing trailing nulls we obtain:
```C++
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
```
Constraints:

- Number of Nodes will not exceed 1000.
- 1 <= Node.val <= 10^5

## Solution
```C++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
  Node* GetTail(Node* head) {
    if (head == nullptr) {
      return head;
    }
    
    Node dump;
    dump.next = head;
    Node* curr = &dump;
    while (curr->next != nullptr) {
      if (curr->next->child != nullptr) {
        Node* child_head = curr->next->child;
        curr->next->child = nullptr;
        
        Node* child_tail = GetTail(child_head);
        
        Node* second_head = curr->next->next;
        
        curr->next->next = child_head;
        child_head->prev = curr->next;
        child_tail->next = second_head;
        if (second_head != nullptr) {
          second_head->prev = child_tail;
        }
        
        curr = child_tail;
        
      } else {
        curr = curr->next;
      }
    }
    
    return curr;
  }
  Node* flatten(Node* head) {
    GetTail(head);
    
    return head;
  }
};
```

# 445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
```C++
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
  int AddDigit(ListNode* l1, ListNode* l2) {
    if (l1->next == nullptr) {
      int sum = l1->val + l2->val;
      l1->val = sum % 10;
      return sum / 10;
    }
    
    int sum = l1->val + l2->val + AddDigit(l1->next, l2->next);
    l1->val = sum % 10;
    return sum / 10;
  }
  
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    if (l1->val == 0) {
      return l2;
    }
    if (l2->val == 0) {
      return l1;
    }
    
    ListNode* curr_l1 = l1;
    ListNode* curr_l2 = l2;
    while (curr_l1 != nullptr || curr_l2 != nullptr) {
      if (curr_l1 != nullptr && curr_l2 != nullptr) {
        curr_l1 = curr_l1->next;
        curr_l2 = curr_l2->next;
        continue;
      }
      
      if (curr_l1 != nullptr) {
        ListNode* tmp = l2;
        l2 = new ListNode(0);
        l2->next = tmp;
        curr_l1 = curr_l1->next;
      } else {
        ListNode* tmp = l1;
        l1 = new ListNode(0);
        l1->next = tmp;
        curr_l2 = curr_l2->next;
      }
    }
    
    if (AddDigit(l1, l2) > 0) {
      ListNode* head = new ListNode(1);
      head->next = l1;
      return head;
    }
    
    return l1;
  }
};
```

# 707. Design Linked List
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

- get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
- addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- addAtTail(val) : Append a node of value val to the last element of the linked list.
- addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
- deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:
```C++
Input: 
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output:  
[null,null,null,null,2,null,3]
Explanation:
MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
```
Constraints:
- 0 <= index,val <= 1000
- Please do not use the built-in LinkedList library.
- At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.

## Solution
```C++
class MyLinkedList {
 public:
  /** Initialize your data structure here. */
  MyLinkedList() : head_(nullptr), tail_(nullptr), size_(0) {

  }

  /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
  int get(int index) {
    if (index < 0 || index >= size_) {
      return -1;
    }
    
    if (index == 0) {
      return head_->val;
    }
    if (index == size_ - 1) {
      return tail_->val;
    }
    
    ListNode* target = head_;
    for (int i = 0; i < index; ++i) {
      target = target->next;
    }
    return target->val;
  }

  /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
  void addAtHead(int val) {
    if (head_ == nullptr && tail_ == nullptr) {
      head_ = new ListNode(val);
      tail_ = head_;
      size_ = 1;
      return;
    }
    
    ListNode* new_head = new ListNode(val);
    new_head->next = head_;
    head_->prev = new_head;
    head_ = new_head;
    //ListNode* old_head = head_;
    //head_ = new ListNode(val);
    //head_->next = old_head;
    //old_head->prev = head_;
    ++size_;
    return;
  }

  /** Append a node of value val to the last element of the linked list. */
  void addAtTail(int val) {
    if (head_ == nullptr && tail_ == nullptr) {
      head_ = new ListNode(val);
      tail_ = head_;
      size_ = 1;
      return;
    }
    
    ListNode* old_tail = tail_;
    tail_ = new ListNode(val);
    old_tail->next = tail_;
    tail_->prev = old_tail;
    ++size_;
    return;
  }

  /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
  void addAtIndex(int index, int val) {
    if (index < 0 || index > size_) {
      return;
    }
    
    if (index == 0) {
      addAtHead(val);
      return;
    }
    if (index == size_) {
      addAtTail(val);
      return;
    }
    ListNode* target_ahead = head_;
    for (int i = 0; i < index - 1; ++i) {
      target_ahead = target_ahead->next;
    }
    
    ListNode* next = target_ahead->next;
    ListNode* add_node = new ListNode(val);
    
    target_ahead->next = add_node;
    add_node->prev = target_ahead;
    add_node->next = next;
    next->prev = add_node;
    ++size_;
    return;
  }

  /** Delete the index-th node in the linked list, if the index is valid. */
  void deleteAtIndex(int index) {
    if (index < 0 || index >= size_) {
      return;
    }
    if (size_ == 0) {
      return;
    }
    
    if (index == 0) {
      if (size_ == 1) {
        head_ = nullptr;
        tail_ = nullptr;
        size_ = 0;
        return;
      }
      head_ = head_->next;
      head_->prev = nullptr;
      --size_;
      return;
    }
    if (index == size_ - 1) {
      if (size_ == 1) {
        head_ = nullptr;
        tail_ = nullptr;
        size_ = 0;
        return;
      }
      
      tail_ = tail_->prev;
      tail_->next = nullptr;
      --size_;
      return;
    }
    
    ListNode* target_ahead = head_;
    for (int i = 0; i < index - 1; ++i) {
      target_ahead = target_ahead->next;
    }
    
    target_ahead->next = target_ahead->next->next;
    target_ahead->next->prev = target_ahead;
    --size_;
    return;
  }
  
 private:
  struct ListNode {
    int val;
    ListNode* next;
    ListNode* prev;
    ListNode(int val = 0) : val(val), next(nullptr), prev(nullptr) {}
  };
  
  ListNode* head_;
  ListNode* tail_;
  int size_;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```

# 725. Split Linked List in Parts
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
```C++
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
```
Example 2:
```C++
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
```
Note:
- The length of root will be in the range [0, 1000].
- Each value of a node in the input will be an integer in the range [0, 999].
- k will be an integer in the range [1, 50].

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
  vector<ListNode*> splitListToParts(ListNode* root, int k) {
    if (k < 1) {
      return {};
    }
    if (k == 1) {
      return {root};
    }
    
    ListNode* curr = root;
    int list_cnt = 0;
    while (curr != nullptr) {
      ++list_cnt;
      curr = curr->next;
    }
    
    if (k >= list_cnt) {
      vector<ListNode*> result;
      ListNode* curr = root;
      for (int i = 0; i < k; ++i) {
        result.push_back(curr);
        if (curr == nullptr) {
          continue;
        }
        ListNode* tmp = curr->next;
        curr->next = nullptr;
        curr = tmp;
      }
      return result;
    }
    
    int part_cnt = list_cnt / k;
    int add_on = list_cnt % k;
    
    vector<ListNode*> result;
    ListNode* tail = root;
    for (int i = 0; i < k; ++i) {
      ListNode* head = tail;
      for (int j = 1; j < part_cnt; ++j) {
        tail = tail->next;
      }
      if (add_on > 0) {
        tail = tail->next;
        --add_on;
      }
      // split
      if (tail->next != nullptr) {
        ListNode* tmp = tail->next;
        tail->next = nullptr;
        tail = tmp;
      }
      // save
      result.push_back(head);
    }
    
    return result;
  }
};
```

# 817. Linked List Components
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:
```C++
Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
```
Example 2:
```C++
Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
```
Note:
- If N is the length of the linked list given by head, 1 <= N <= 10000.
- The value of each node in the linked list will be in the range [0, N - 1].
- 1 <= G.length <= 10000.
- G is a subset of all values in the linked list.

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
  int numComponents(ListNode* head, vector<int>& G) {
    if (head == nullptr || G.empty()) {
      return 0;
    }
    
    unordered_set<int> map(G.begin(), G.end());
    
    int cnt = 0;
    ListNode* curr = head;
    bool is_head_found = false;
    while (curr != nullptr) {
      if (map.find(curr->val) != map.end()) {
        is_head_found = true;
      } else {
        if (is_head_found) {
          ++cnt;
        }
        is_head_found = false;
      }
      curr = curr->next;
    }
    
    return is_head_found ? cnt + 1 : cnt;
  }
};
```

# 876. Middle of the Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
```C++
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
```
Example 2:
```C++
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
```
Note:

- The number of nodes in the given list will be between 1 and 100.

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
  ListNode* middleNode(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
      return head;
    }
    
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast->next != nullptr && fast->next->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
    }
    
    if (fast->next == nullptr) {
      return slow;
    }
    
    return slow->next;
  }
};
```

# 1019. Next Greater Node In Linked List
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

Example 1:
```C++
Input: [2,1,5]
Output: [5,5,0]
```
Example 2:
```C++
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
```
Example 3:
```C++
Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
```

Note:

- 1 <= node.val <= 10^9 for each node in the linked list.
- The given list has length in the range [0, 10000].

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
  vector<int> nextLargerNodes(ListNode* head) {
    if (head == nullptr) {
      return {};
    }
    
    ListNode* curr = head;
    vector<int> result;
    while (curr != nullptr) {
      ListNode* bigger = curr->next;
      while (bigger != nullptr && bigger->val <= curr->val) {
        bigger = bigger->next;
      }
      
      if (bigger == nullptr) {
        result.push_back(0);
      } else {
        result.push_back(bigger->val);
      }
      
      curr = curr->next;
    }
    
    return result;
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
  int getDecimalValue(ListNode* head) {
    ListNode* curr = head->next;
    head->next = nullptr;
    ListNode* tail = head;
    while (curr != nullptr) {
      ListNode* tmp = curr->next;
      curr->next = tail;
      tail = curr;
      curr = tmp;
    }
    
    int base = 1;
    int num = 0;
    while (tail != nullptr) {
      num += tail->val * base;
      base *= 2;
      tail = tail->next;
    }
    
    return num;
  }
};
```

# 1367. Linked List in Binary Tree
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1:
![pic](https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png)
```C++
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
```
Example 2:
![pic](https://assets.leetcode.com/uploads/2020/02/12/sample_2_1720.png)
```C++
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
```
Example 3:
```C++
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
```

Constraints:

- 1 <= node.val <= 100 for each node in the linked list and binary tree.
- The given linked list will contain between 1 and 100 nodes.
- The given binary tree will contain between 1 and 2500 nodes.

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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
  bool isSubPathCore(ListNode* head, TreeNode* root) {
    if (head == nullptr) {
      return true;
    }
    if (root == nullptr) {
      return false;
    }
    
    if (head->val == root->val) {
      return isSubPathCore(head->next, root->left) || isSubPathCore(head->next, root->right);
    }
    
    return false;
  }
  
  bool isSubPath(ListNode* head, TreeNode* root) {
    if (head == nullptr) {
      return true;
    }
    if (root == nullptr) {
      return false;
    }
    
    if (head->val == root->val) {
      if (isSubPathCore(head->next, root->left) || isSubPathCore(head->next, root->right)) {
        return true;
      } else {
        return isSubPath(head, root->left) || isSubPath(head, root->right);
      }
    }
    
    return isSubPath(head, root->left) || isSubPath(head, root->right);
  }
};
```
