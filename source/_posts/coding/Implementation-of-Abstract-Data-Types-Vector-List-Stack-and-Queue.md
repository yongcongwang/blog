---
title: 'Implementation of Abstract Data Types: Vector, List, Stack and Queue'
mathjax: true
categories:
  - coding
date: 2020-10-09 23:56:21
---

An `abstract data type`(ADT) is a set of objects together with a set of operations. Objects such as lists, sets, and graphs along with their operations can be viewed as ADTs, just as integers, reals, and boolens are data types.

The C++ language includes an implementation of common data structures in its library, which is popularly known as the `Standard Template Library`(STL).

<!-- more -->
# Vector

```C++
#include <iostream>
#include <algorithm>

template <typename Object>
class Vector {
 public:
  explicit Vector(int size = 0)
      : size_(0), capacity_(size_ + 10), objects_(new Object[capacity_]) {}

  Vector(const Vector& rhs)
      : size_(rhs.size_), capacity_(rhs.capacity_),
        objects_(new Object[capacity_]) {
    for (std::size_t i = 0; i < size_; ++i) {
      objects_[i] = rhs.objects_[i];
    }
  }

  Vector& operator=(const Vector& rhs) {
    Vector copied(rhs);
    std::swap(*this, copied);
    return *this;
  }

  ~Vector() { 
    delete[] objects_;
  }

  Vector(Vector&& rhs)
      : size_(rhs.size_), capacity_(rhs.capacity_), objects_(rhs.objects_) {
    rhs.size_ = 0;
    rhs.capacity_ = 0;
    rhs.objects_ = nullptr;
  }

  Vector& operator=(Vector&& rhs) {
    std::swap(size_, rhs.size_);
    std::swap(capacity_, rhs.capacity_);
    std::swap(objects_, rhs.objects_);
    return *this;
  }

 public:
  void resize(int new_size) {
    if (new_size > capacity_) {
      reserve(new_size * 2);
    }

    size_ = new_size;
  }

  void reserve(int new_capacity) {
    if (new_capacity < size_) {
      return;
    }

    Object *new_array = new Object[new_capacity];
    for (int i = 0; i < size_; ++i) {
      new_array[i] = objects_[i];
    }

    capacity_ = new_capacity;
    std::swap(objects, new_array);
    delete[] new_array;
  }

  Object& operator[](int index) {
    return objects_[index];  // TODO: input check
  }

  const Object& operator[](int index) const {
    return objects_[index];  // TODO: input check
  }

  bool empty() const {
    return size_ == 0;
  }

  int size() const {
    return size_;
  }

  int capacity() const {
    return capacity_;
  }

  void push_back(const Object& x) {
    if (size_ == capacity_) {
      reserve(2 * capacity_ + 1);
    }

    objects_[size_] = x;
    ++size_;
  }

  void push_back(const Object&& x) {
    if (size_ == capacity_) {
      reserve(2 * capacity_ + 1);
    }

    objects_[size_] = std::move(x);
    ++size_;
  }

  void pop_back() {
    --size_;
  }

  const Object& back() const {
    return objects_[size_ - 1];  // TODO: empty check
  }

  const Object& front() const {
    return objects_[0];  // TODO: empty check
  }

 public:
  typedef Object* iterator;
  typedef const Object* const_iterator;

  iterator begin() {
    return &object[0];
  }

  const_iterator begin() const {
    return &object[0];
  }

  iterator end() {
    return &object[size_];
  }
  const_iterator end() const {
    return &object[size_];
  }

 private:
  int size_;
  int capacity_;
  Object* objects_;
};
```
