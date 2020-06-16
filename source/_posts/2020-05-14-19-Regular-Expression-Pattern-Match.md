---
title: CodingInterview | 19 Regular Expression Pattern Match
mathjax: true
comments: true
date: 2020-05-14 00:27:27
categories: coding
tags:
 - coding
 - coding_interview
---

> Please relize a function to match the regular expression with "." and "\*".
> The "." represents for any char, and "\*" represents that the char before it can appears any times(0 or more).
> For example, "aaa" matches with the pattern of "a.a" and "ab\*ac\*a" but dismatches with the pattern of "aa.a" and "ab\*a".
<!-- more -->
## Solution
```C++
bool IsMatchRecursive(char* str, char* pattern) {
  if (*str == '\0' && *pattern == '\0') {
    return true;
  }

  if (*str != '\0' && *pattern == '\0') {
    return false;
  }

  if (*(pattern + 1) == '*') {
    if (*str == *pattern || *pattern == '.' && *str != '\0') {
      return IsMatchRecursive(str, pattern + 2) ||
             IsMatchRecursive(str + 1, pattern + 2) ||
             IsMatchRecursive(str + 1, pattern);
    } else {
      return IsMatchRecursive(str, pattern + 2);
    }
  }

  if (*str == *pattern || *pattern == '.' && *str != '\0') {
    return IsMatchRecursive(str + 1, pattern + 1);
  }

  return false;
}

bool IsMatch(char* str, char* pattern) {
  if (str == nullptr || pattern == nullptr) {
    return false;
  }

  return IsMatchRecursive(str, pattern);
}
```
