---
title: CodingInterview | 30 A Min Stack
mathjax: true
comments: true
date: 2020-05-21 23:47:46
categories: coding
---

> Define a stack that can output its min value.
> The time complexity of `min`, `push`, `pop` methods of the stack must be $O(1)$.

<!-- more -->

## Solution
```C++
#include <limits>

template <typename T>
class MyStack {
 public:
  MyStack() : head_(nullptr) {}
  ~MyStack() {
    while (head_ != nullptr) {
      Node* tmp = head_;
      head_ = head_->next;
      delete tmp;
    }
  };

 public:
  void push(T val) {
    Node* new_node = new Node(val);
    new_node->next = head_;
    head_ = new_node;
  }

  T pop() {
    if (head_ == nullptr) {
      return std::numeric_limits<T>::max();
    }

    T value = head_->value;
    Node* tmp = head_;
    head_ = head_->next;

    delete tmp;
    return value;
  }

  T top() {
    if (head_ == nullptr) {
      return std::numeric_limits<T>::max();
    }

    return head_->value;
  }

  bool empty() {
    return head_ == nullptr;
  }

 private:
  struct Node {
    Node(T val = 0) : value(val), next(nullptr) {}

    T value;
    Node* next;
  };

  Node* head_;
};

template <typename T>
class MinStack {
 public:
  MinStack() = default;
  ~MinStack() = default;
 
 public:
  void push(T value) {
    data_.push(value);
    assist_.push(value < assist_.top() ? value : assist_.top());
  }

  T pop() {
    if (data_.empty()) {
      return std::numeric_limits<T>::max();
    }

    assist_.pop();
    data_.pop();
  }

  T top() {
    if (data_.empty()) {
      return std::numeric_limits<T>::max();
    }

    return data_.top();
  }

  T min() {
    if (assist_.empty()) {
      return std::numeric_limits<T>::max();
    }
    return assist_.top();
  }

 private:
  MyStack<T> data_;
  MyStack<T> assist_;
};
```
