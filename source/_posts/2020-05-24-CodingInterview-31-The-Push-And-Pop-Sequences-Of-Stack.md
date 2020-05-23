---
title: CodingInterview | 31 The Push And Pop Sequences Of Stack
mathjax: true
comments: true
date: 2020-05-24 00:20:12
categories: coding
---

> Input two integar sequences, the first is the push order of a stack, please check if the second is one of the pop order of the stack. Assume that all the numbers in the stack are different.
> For exmaple, `{1, 2, 3, 4, 5}` is a push order of a stack, `{4, 5, 3, 2, 1}` can be its pop order, but `{4, 3, 5, 1, 2}` can not be.

<!-- more -->

## Solution
```C++
bool IsStackInOutOrder(
    const std::vector<int>& in, const std::vector<int>& out) {
  if (in.empty() && out.empty()) {
    return true;
  }

  if (in.size() != out.size()) {
    return false;
  }

  auto it_in = in.begin();
  auto it_out = out.begin();
  std::stack<int> arr;
  while (it_in != in.end()) {
    if (arr.empty()) {
      arr.push(*it_in);
      it_in++;
      continue;
    }
    if (arr.top() == *it_out) {
      arr.pop();
      it_out++;
    } else {
      arr.push(*it_in);
      it_in++;
    }
  }

  while (!arr.empty()) {
    if (arr.top() != *it_out) {
      return false;
    }
    arr.pop();
    it_out++;
  }

  return true;
}
```
