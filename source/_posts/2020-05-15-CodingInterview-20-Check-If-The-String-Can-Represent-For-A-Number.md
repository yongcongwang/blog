---
title: CodingInterview | 20 Check If The String Can Represent For A Number
mathjax: true
comments: true
date: 2020-05-15 00:34:50
categories: coding
---

> Please check if a string can represent for a number. For example, "+100", "5e2", "-123", "3.1415" can represent for a number; "12e", "1a3.22", "1.2.3", "+-5" and "1e+5.2" not.

## Solution
```C++
bool ScanUnsignedIntegar(std::string& str) {
  if (str.empty()) {
    return false;
  }

  bool is_num_found(false);
  while (!str.empty() && str.front() >= '0' && str.front() <= '9') {
    str.erase(str.begin());
    is_num_found = true;
  }

  return is_num_found;
}

bool ScanIntegar(std::string& str) {
  if (str.empty()) {
    return false;
  }

  if (str.front() == '+' || str.front() == '-') {
    str.erase(str.begin());
  }

  return ScanUnsignedIntegar(str);
}

bool IsStrNumber(std::string& str) {
  if (str.empty()) {
    return false;
  }

  bool is_num = ScanIntegar(str);

  if (!str.empty() && str.front() == '.') {
    str.erase(str.begin());
    is_num = ScanUnsignedIntegar(str) || is_num;
  }

  if (!str.empty() && (str.front() == 'e' || str.front() == 'E')) {
    str.erase(str.begin());
    is_num = ScanIntegar(str) && is_num;
  }

  return is_num && str.empty();
}
```
