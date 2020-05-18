---
title: Build Calculator Using Stack
categories: coding
mathjax: true
date: 2019-08-15 09:55:30
---

Write a function that takes a string of arithmetic equation and return a scalar as the evaluation of the equation arithmetic supports 4 operators: `+`, `*`, `&`, `|`, where + and * are defined as usual, & and | are defined as pairwise max, min, respectively A & B = fmax(A, B), A | B = fmin(A, B)

Priority: &, | higher than * higher than +

Your algorithm should handle space, decimal and negative numbers. For any invalid input, output should be zero.
<!-- more -->
```C++
// By yongcong.wang @ 15/08/2019
#include <iostream>
#include <stack>
#include <string>

class Calculator {
 public:
  Calculator() {}
  ~Calculator() {}

  double calculate(std::string input) {
    input = removeSpace(input);
    std::stack<char> operators;
    std::stack<int> numbers;

    std::cout << "after remove space: " << input << std::endl;
    if (input.empty() || isOperator(input[0])) {
      return 0;
    }
    std::cout << "valid input" << std::endl;

    while (!input.empty()) {
      int neg_fac = 1;
      if (isNegtive(input[0])) {
        std::cout << "is negtive: " << input[0] << std::endl;
        neg_fac = -1;
        cutNegtive(&input);
      }

      if (isNumber(input[0])) {
        std::cout << "is number: " << input[0] << std::endl;
        numbers.push(neg_fac * cutNumber(&input));
        neg_fac = 1;
      }

      if (isOperator(input[0])) {
        std::cout << "is operator: " << input[0] << std::endl;
        if (neg_fac != 1) {
          return 0;
        }

        if (operators.empty()) {
          operators.push(cutOperator(&input));
          continue;
        } else {
          if (getOperatorPrioty(input[0]) > getOperatorPrioty(operators.top())) {
            operators.push(cutOperator(&input));
          } else {
            int b = numbers.top();
            numbers.pop();
            int a = numbers.top();
            numbers.pop();
            char op = operators.top();
            operators.pop();
            numbers.push(operateNumbers(op, a, b));
          }
        }
      }
      std::cout << "operators size is: " << operators.size() << " numbers.size() is " 
                << numbers.size() << std::endl;
    }

    while (!operators.empty()) {
      int b = numbers.top();
      numbers.pop();
      int a = numbers.top();
      numbers.pop();
      char op = operators.top();
      operators.pop();
      numbers.push(operateNumbers(op, a, b));
    }

    return numbers.top();
  }

 private:
  std::string removeSpace(std::string input) {
    std::string output;
    for (int i = 0; i < input.size(); ++i) {
      if (input[i] != ' ') {
        output += input[i];
      }
    }
    return output;
  }

  bool isOperator(char c) {
    if (c == '+' || c == '*' || c == '&' || c == '|') {
      return true;
    } else {
      return false;
    }
  }

  int getOperatorPrioty(char c) {
    switch (c) {
      case '+' : {
        return 0;
      }
      case '*' : {
        return 1;
      }
      case '&' : {
        return 2;
      }
      case '|' : {
        return 2;
      }
      default : {
        return -1;
      }
    }
  }

  int operateNumbers(char c, int a, int b) {
    switch (c) {
      case '+' : {
        return a + b;
      }
      case '*' : {
        return a * b;
      }
      case '&' : {
        return a > b ? a : b;
      }
      case '|' : {
        return a < b ? a : b;
      }
      default : {
        return 0;
      }
    }
  }

  char cutOperator(std::string *input) {
    auto &s = *input;
    if (isOperator(s[0])) {
      char out = s[0];
      s = s.erase(0, 1);
      return out;
    }
  }

  bool isNegtive(char c) {
    if (c == '-') {
      return true;
    } else {
      return false;
    }
  }

  char cutNegtive(std::string *input) {
    auto &s = *input;
    if (isNegtive(s[0])) {
      char out = s[0];
      s = s.erase(0, 1);
      return out;
    }
  }

  bool isNumber(char c) {
    if (c >= '0' && c <= '9') {
      return true;
    } else {
      return false;
    }
  }

  int cutNumber(std::string *input) {
    auto &s = *input;
    int out = 0;
    int num_cnt = 0;
    for (auto c : s) {
      if (isNumber(c)) {
        out = out * 10 + (c - '0');
        num_cnt++;
      } else {
        break;
      }
    }
    s = s.erase(0, num_cnt);
    return out;
  }

};

int main() {
  std::string input("-2 + 3 * 5 & 2 | 1");
  Calculator calc;
  std::cout << "calc " << input << std::endl;
  std::cout << "result is " << calc.calculate(input) << std::endl;
}
```
