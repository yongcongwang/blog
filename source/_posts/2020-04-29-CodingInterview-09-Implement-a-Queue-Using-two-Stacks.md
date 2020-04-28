---
title: CodingInterview | 09 Implement a Queue Using two Stacks
mathjax: true
comments: true
date: 2020-04-29 01:34:42
categories: coding
---

> Using two stacks to implement a queue and realize the queue's two functions: `AppendTail` and `DeleteHead`.

## Solution
```C++
template <typename T> class MyQueue {
 public:
  void AppendTail(const T &node) {
    stack1.push(node);
  }
  T DeleteHead() {
    if (stack2.empty()) {
      while (!stack1.empty()) {
        T &tmp = stack1.top();
        stack1.pop();
        stack2.push(tmp);
      }
    }

    if (stack2.empty()) {
      std::cout << "No element in queue" << std::endl;
      // TODO: the exception
    }

    T head = stack2.top();
    stack2.pop();
    return head;
  }

 private:
  std::stack<T> stack1;
  std::stack<T> stack2;
};
```
