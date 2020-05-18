---
title: CodingInterview | 02 Singleton
mathjax: true
comments: true
date: 2020-04-22 22:29:24
categories: coding
---

> Design a `Singleton`
<!-- more -->
## Solution
```c++
class Singleton {
 public:
  static Singleton *GetInstance() {
    static Singleton instance;
    return &instance;
  }
  ~Singleton() = default;
  Singleton(const Singleton &rhs) = delete;
  Singleton &operator=(const Singleton &rhs) = delete;

 private:
  Singleton() = default;
};
```
