---
title: CodingInterview | 15 The Count of 1 in Binary Number
mathjax: true
comments: true
date: 2020-05-03 23:41:09
categories: coding
---

> Input a integar and output the count of 1 in its binary.
> For example, $9$ in binary is $1001$, so the count of 1 is $2$.
<!-- more -->
## Solution 1
```C++
int NumOfOneMethod1(int n) {
  int cnt(0);
  unsigned int flag(1);

  while (flag) {
    cnt += n & flag ? 1 : 0;
    flag = flag << 1;
  }
  return cnt;
}
```
## Solution 2
```C++
int NumOfOneMethod2(int n) {
  int cnt(0);

  while (n) {
    cnt++;
    n = (n - 1) & n;
  }

  return cnt;
}
```
