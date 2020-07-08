---
title: CodingInterview | 58 Reverse Words
categories: coding
tags:
  - coding interview
mathjax: true
comments: true
date: 2020-07-07 23:59:11
---

> Input a sentence, please reverse all the words of it. For example, input "I am a student", the output would be "student a am I".

<!-- more -->
## Solution
```C++
void ReverseString(std::string::iterator start, std::string::iterator end) {
  while (start < end) {
    auto tmp = *start;
    *start =  *end;
    *end = tmp;
    start++;
    end--;
  }
}

std::string ReverseSentence(std::string sentence) {
  if (sentence.empty()) {
    return "";
  }

  ReverseString(sentence.begin(), sentence.end() - 1);
  std::cout << "reverse: " << sentence << std::endl;

  auto start = sentence.begin();
  auto end = sentence.begin();
  while (end != sentence.end()) {
    if (*end == ' ') {
      ReverseString(start, end - 1);
      start = end + 1;
      end = start;
    } else {
      end++;
    }
  }

  return sentence;
}
```

> The operator `left turn` of a string is to move the charactors in front of the string to the end. For example, input the string "abcdefg" and the number $2$, the output should be "cdefgab".

## Solution
```C++
std::string LeftTurnString(std::string str, const int num) {
  if (str.empty() || num >= str.size()) {
    return "";
  }
  if (num < 1) {
    return str;
  }

  ReverseString(str.begin(), str.end() - 1);
  ReverseString(str.end() - num, str.end() - 1);
  ReverseString(str.begin(), str.end() - num - 1);

  return str;
}
```
