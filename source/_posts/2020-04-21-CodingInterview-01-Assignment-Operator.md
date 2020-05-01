---
title: CodingInterview | 01 Assignment Operator
mathjax: true
comments: true
date: 2020-04-21 00:29:05
categories: coding
---
> The following is the declaration of type `MyString`, please add assignment operator function for it.

```c++
class MyString {
 public:
  MyString(char *data = nullptr);
  Mystring(const MyString &rhs);

  ~MyString() = default;

 private:
  char *my_string;
};
```

## Solution

```c++
class MyString {
 public:
  MyString(char *data = nullptr);
  Mystring(const MyString &rhs);
  MyString &operator=(const MyString &rhs) {
    if (this != &rhs) {
      MyString tmp_string(rhs);
      char *tmp = tmp_string.my_string;
      tmp_string.my_string = my_string;
      my_string = tmp;
    }

    return *this;
  }

  ~MyString() = default;

 private:
  char *my_string;
};
```
