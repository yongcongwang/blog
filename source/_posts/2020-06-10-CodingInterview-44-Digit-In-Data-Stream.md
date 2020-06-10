---
title: CodingInterview | 44 Digit In Data Stream
mathjax: true
comments: true
date: 2020-06-10 22:15:18
categories: coding
---

> There is a number stream: "0123456789101112131415...", in this stream, the 5th digit is `5`, 13th digit is `1`, 19th digit is `4`.
> Please output the number of any digit.

<!-- more -->

## Solution
```
int GetDigitsSum(const int digits) {
  if (digits == 1) {
    return 10;
  }

  return 9 * std::pow(10, digits - 1);
}

int GetDigitsStart(const int digits) {
  if (digits == 1) {
    return 0;
  }

  return std::pow(10, digits - 1);
}

int GetNumDigits(int num, int digits) {
  int target_num = GetDigitsStart(digits) + num / digits;
  int digit_right = digits - num % digits;

  while (digit_right > 1) {
    target_num /= 10;
  }
  return target_num % 10;
}

int GetDigitInStream(int num) {
  if (num < 0) {
    return -1;
  }

  int digits = 1;
  while (true) {
    int digits_sum = GetDigitsSum(digits);
    if (num < digits_sum) {
      return GetNumDigits(num, digits);
    }
    digits ++;
    num -= digits_sum;
  }
}
```
