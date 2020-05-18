---
title: CodingInterview | 17 Print The Number From One to Maximum Nth Digits
mathjax: true
comments: true
date: 2020-05-12 00:21:58
categories: coding
---

> Input the number $n$, please print 1 to maximum nth digits in order. For example, input 3, output: 1, 2, 3, ..., 998, 999.
<!-- more -->
## Solution
```C++
void PrintNoneZeroNumber(const std::vector<char> &digits) {
  auto it = digits.begin();
  while (*it == '0') {
    it++;
  }

  while (it != digits.end()) {
    std::cout << *it;
    it++;
  }
  std::cout << std::endl;
}

void PrintOneToNthDigits(std::vector<char> &digits, const std::size_t index) {
  if (index == digits.size() - 1) {
    PrintNoneZeroNumber(digits);
    return;
  }

  for (std::size_t i = 0; i < 10; ++i) {
    digits[index + 1] = i + '0';
    PrintOneToNthDigits(digits, index + 1);
  }
}

void PrintOneToNDigits(const std::size_t n) {
  if (n == 0) {
    return;
  }

  std::vector<char> digits(n, '0');
  for (std::size_t i = 0; i < 10; ++i) {
    digits[0] = i + '0';
    PrintOneToNthDigits(digits, 0);
  }
}
```
