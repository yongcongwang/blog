---
title: CodingInterview | 05 Replace Spaces
mathjax: true
comments: true
date: 2020-04-25 01:55:01
categories: coding
---

> Design a function to replace all the spaces in a string with "%20".

For instance, input: "We are happy.", output: "We%20are%20happy.".
<!-- more -->
## Solution
```C++
void ReplaceSpace(char *const arr, const int length) {
  if (arr == nullptr || length <= 0) {
    return;
  }

  int space_cnt = 0;
  int char_cnt = 0;
  int i = 0;
  while (arr[i] != '\0') {
    if (arr[i++] == ' ') {
      space_cnt++;
    }
    char_cnt++;
  }
  char_cnt++;

  if (char_cnt + space_cnt * 2 > length) {
    return;
  }

  int end_of_origin = char_cnt - 1;
  int start_of_new = space_cnt * 2 + char_cnt - 1;

  while (end_of_origin >= 0) {
    if (arr[end_of_origin] == ' ') {
      arr[start_of_new--] = '0';
      arr[start_of_new--] = '2';
      arr[start_of_new--] = '%';
      end_of_origin--;
    } else {
      arr[start_of_new--] = arr[end_of_origin--];
    }
  }
}
```
