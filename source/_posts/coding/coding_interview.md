---
title: Coding-Interview Problems
mathjax: true
comments: true
date: 2020-04-21 00:29:05
categories:
  - coding
---

# Assignment Operator
> The following is the declaration of type `MyString`, please add assignment operator function for it.
<!-- more -->
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

# Singleton

> Design a `Singleton`

## Solution
```c++
class Singleton {
 public:
  static Singleton *GetInstance() {
    static Singleton instance;
    return &instance;
  }
  ~Singleton() = default;
  Singleton(const Singleton &rhs) = delete;
  Singleton &operator=(const Singleton &rhs) = delete;

 private:
  Singleton() = default;
};
```

# Duplication Number
> Find the duplicated number in a list. You are given a list with or without duplicated numbers. All the numbers in the list are positive. If there are duplicated numbers in the list, please output them; if not, return -1;

For example, `{2, 3, 5, 4, 2, 0, 1}`, the duplicated number is `2`.
## Solution 1
```C++
void swap(int &a, int &b) {
  int tmp = a;
  a = b;
  b = tmp;
}

int GetDuplicateNum(std::vector<int> &arr) {
  if (arr.empty()) {
    return -1;
  }

  for (int i = 0; i < arr.size(); ++i) {
    while (arr[i] != i) {
      if (arr[arr[i]] == arr[i]) {
        return arr[i];
      }
      swap(arr[arr[i]], arr[i]);
    }
  }

  return -1;
}
```
Every number needs only twice exchange at most to find its location, so the time complexity is $O(n)$. All the operations are on the input array, so the space complexity is $O(1)$.

## Solution 2
The above solution changes the input array, to protect the input array:
```C++
int NumCnt(const std::vector<int> &arr, const int start, const int end) {
  int cnt(0);
  for (auto num : arr) {
    if (num >= start && num <=end) {
      cnt++;
    }
  }
  return cnt;
}
  
int GetRangeDuplication(const std::vector<int> &arr, const int start,
                        const int end) {
  if (start == end) {
    return -1;
  }

  if (end - start == 1) {
    const int cnt_start = NumCnt(arr, start, start);
    return cnt_start > 1 ? start : end;
  }

  const int mid = (start + end) / 2;
  return NumCnt(arr, start, mid) > mid - start + 1 ? 
      GetRangeDuplication(arr, start, mid) : GetRangeDuplication(arr, mid, end);
}

int GetDuplicatedNum(const std::vector<int> &arr) {
  if (arr.empty()) {
    return -1;
  }

  return GetRangeDuplication(arr, 0, arr.size() - 1);
}

```
The function will be called $log(n)$ times, and every time costs $O(n)$, so the time complexity is $O(nlog(n))$. There is no other space needed, so the space complexity is $O(1)$

# Lookup in 2D Vector
> In a 2D vector, all the rows and colums are sorted. Please write a function to check if a number is in the vector.

For example, the following vector contains the number `7`, then the function returns true; as for `5`, the functions returns false;
## Solution
```C++
bool IsVectorContainNum(
    const std::vector<std::vector<int>> &arr, const int num) {
  if (arr.empty()) {
    return false;
  }

  int row = 0;
  int col = arr.front().size() - 1;

  while (row < arr.size() && col >=0) {
    if (arr[row][col] == num) {
      return true;
    } else if (arr[row][col] > num) {
      col--;
    } else {
      row++;
    }
  }

  return false;
}
```

# Replace Spaces

> Design a function to replace all the spaces in a string with "%20".

For instance, input: "We are happy.", output: "We%20are%20happy.".
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

# Print the Reverse of a Linked List

> Please print the reverse of a linked list, for example, the linked list is `3->5->7->9`, then the output should be `9<-7<-5<-3`.
## Solution
```C++
void reverse_print(Node *node) {
  if (node == nullptr) {
    return;
  }

  if (node->next == nullptr) {
    std::cout << node->value << "<-";
    return;;
  }

  reverse_print(node->next);
  std::cout << node->value << "<-";
```
}

# Rebuild Binary Tree

> Please rebuild the binary tree with the preorder and inorder vectors of this binary tree. Assuming preorder and inorder vectors have no repeat numbers. For example, with the preorder vector `{1, 2, 4, 7, 3, 5, 6, 8}` and inorder vector `{4, 7, 2, 1, 5, 3, 8, 6}`, the binary tree is:

 ```C++
       1
      / \
     2   3
    /   / \
   4   5   6
    \     /
     7   8
```
## Solution
```C++
struct BinaryTree {
  BinaryTree(int value = 0) : value(value), left(nullptr), right(nullptr) {}
  int value;
  BinaryTree *left;
  BinaryTree *right;
};

BinaryTree *construct_bin_tree(
    const std::vector<int> &preorder, const int start_index_preorder,
    const int end_index_preorder, const std::vector<int> &inorder,
    const int start_index_inorder, const int end_index_inorder) {

  if (end_index_preorder == start_index_preorder) {
    return new BinaryTree(preorder[start_index_preorder]);
  }

  int inorder_head_index = -1;
  for (int i = start_index_inorder; i <= end_index_inorder; ++i) {
    if (inorder[i] == preorder[start_index_preorder]) {
      inorder_head_index = i;
      break;
    }
  }
  if (inorder_head_index < 0) {
    return nullptr;
    std::cout << "error occurs" << std::endl;
  }

  auto *new_head = new BinaryTree(preorder[start_index_preorder]);
  const int gap = inorder_head_index - start_index_inorder;
  if (gap != 0) {
    new_head->left = construct_bin_tree(
        preorder, start_index_preorder + 1, start_index_preorder + gap,
        inorder, start_index_inorder, inorder_head_index - 1);
  }

  if (gap != end_index_inorder - start_index_inorder) {
    new_head->right = construct_bin_tree(
        preorder, start_index_preorder + gap + 1, end_index_preorder,
        inorder, inorder_head_index + 1, end_index_inorder);
  }

  return new_head;
}

BinaryTree *rebuild_binary_tree(
    const std::vector<int> &preorder, const std::vector<int> &inorder) {
  if (preorder.empty() || inorder.empty() ||
      preorder.size() != inorder.size()) {
    return nullptr;
  }

  return construct_bin_tree(
      preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
}
```

# Next Node of Binary Tree in Inorder

> Given a binary tree and a node, please find the next node in inorder. The binary tree node has a pointer to its parent.
## Solution
```C++
struct BinaryTree {
  BinaryTree(int value = 0) 
      : value(value), parent(nullptr), left(nullptr), right(nullptr) {}
  int value;
  BinaryTree *parent;
  BinaryTree *left;
  BinaryTree *right;
};

BinaryTree *GetNextInorder(BinaryTree *node) {
  if (node == nullptr || node->parent == nullptr) {
    return nullptr;
  }

  if (node->right != nullptr) {
    BinaryTree *tmp = node->right;
    while (tmp->left != nullptr) {
      tmp = tmp->left;
    }
    return tmp;
  } else if (node == node->parent->left) {
    return node->parent;
  } else {
    BinaryTree *tmp = node;
    while (tmp->parent != nullptr && tmp != tmp->parent->left) {
      tmp = tmp->parent;
    }
    return tmp->parent == nullptr ? nullptr : tmp->parent;
  }
}
```

# Implement a Queue Using two Stacks

> Using two stacks to implement a queue and realize the queue's two functions: `AppendTail` and `DeleteHead`.
## Solution
```C++
template <typename T> class MyQueue {
 public:
  void AppendTail(const T &node) {
    stack1.push(node);
  }
  T DeleteHead() {
    if (stack2.empty()) {
      while (!stack1.empty()) {
        T &tmp = stack1.top();
        stack1.pop();
        stack2.push(tmp);
      }
    }

    if (stack2.empty()) {
      std::cout << "No element in queue" << std::endl;
      // TODO: the exception
    }

    T head = stack2.top();
    stack2.pop();
    return head;
  }

 private:
  std::stack<T> stack1;
  std::stack<T> stack2;
};
```

# Fibonacci Sequence

> Write a function to get the nth number of Fibonacci sequence. The Fibonacci sequence is defined as following:
$$
f(n) = 
\begin{cases}
0, & if & n = 0 \\\\
1, & if & n = 1 \\\\
f(n - 1) + f(n - 2), & if & n > 1
\end{cases}
$$
## Solution 1
```C++
int FibonacciRecursion(const int n) {
  if (n <= 0) {
    return 0;
  }

  if (n == 1) {
    return 1;
  }

  return FibonacciRecursion(n - 1) + FibonacciRecursion(n - 2);
}
```

This solution is simple, but its time complexity is $O(2^n)$, which is usually unacceptable.

## Solution 2
```C++
int FibonacciLoop(const int n) {
  if (n <= 0) {
    return 0;
  }

  if (n == 1) {
    return 1;
  }

  int result = 0;
  int fibo_minus_two = 0;
  int fibo_minus_one = 1;
  for (int i = 2; i <= n; ++i) {
    result = fibo_minus_two + fibo_minus_one;
    fibo_minus_two = fibo_minus_one;
    fibo_minus_one = result;
  }

  return result;
}
```

This solution use loop to calculate the result, and its time complexity is $O(n)$

# Minimum of Rotated Sorted Array

> The rotation is that putting a few elements ahead of the array to the end. With a rotated sorted array, please output the minimum of the array.
> For example, `{3, 4, 5, 1, 2}` is a rotation of `{1, 2, 3, 4, 5}` and its min value is `1`.
## Solution 1
Loop to find the minimum, and the time complexity is $O(n)$
```C++
int GetMinimumTravesal(const std::vector<int> &arr) {
  if (arr.empty()) {
    return 0;
  }

  int min = arr[0];
  for (auto &num : arr) {
    if (num < min) {
      min = num;
    }
  }

  return min;
}
```

## Solution 2
As we know the array is sorted, we can use the binary search to find the minimum, and the time complexity is $O(log(n))$
```C++
int GetMinimumBin(const std::vector<int> &arr, const int start_index, const int end_index) {
  if (start_index == end_index) {
    return arr[start_index];
  }

  if (end_index - start_index == 1) {
    return arr[start_index] < arr[end_index] ? arr[start_index] : arr[end_index];
  }

  int mid_index = (start_index + end_index) / 2;


  if (arr[start_index] == arr[mid_index] && arr[mid_index] == arr[end_index]) {
    return GetMinimumTravesal(arr);
  }

  if (arr[mid_index] >= arr[start_index]) {
    return GetMinimumBin(arr, mid_index, end_index);
  } else {
    return GetMinimumBin(arr, start_index, mid_index);
  }
}

int GetMinimumBinary(const std::vector<int> &arr) {
  if (arr.empty()) {
    return 0;
  }

  return GetMinimumBin(arr, 0, arr.size() - 1);
}
```

# Path in 2D Matrix

> Please design a function to check if a path exists in a 2D matrix. Path can start from any position, and it can expend to up/down/left/right cell. If the path passes by a cell, it can not do that again.
> For example, following 2d matrix contains the path `bfce`, but the path `abfb` is not in it.
```
a b t g
c f c s
j d e h
```
## Solution
```C++
bool IsPathInMatrixCore(
    const std::vector<std::vector<char>> &matrix,
    const int row, const int col, std::vector<std::vector<bool>> &map,
    const std::vector<char> &path, const int index) {
  if (index == path.size()) {
    return true;
  }

  bool result = false;
  // up
  int row_up = row - 1;
  if (row_up >=0 && map[row_up][col] && matrix[row_up][col] == path[index]) {
    auto temp = map;
    temp[row_up][col] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row_up, col, temp, path, index + 1);
  }
  // down
  int row_down = row + 1;
  if (row_down <= matrix.size() - 1 && map[row_down][col] &&
      matrix[row_down][col] == path[index]) {
    auto temp = map;
    temp[row_down][col] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row_down, col, temp, path, index + 1);
  }
  // left
  int col_left = col - 1;
  if (col_left >=0 && map[row][col_left] &&
      matrix[row][col_left] == path[index]) {
    auto temp = map;
    temp[row][col_left] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row, col_left, temp, path, index + 1);
  }

  // right
  int col_right = col + 1;
  if (col_right <= matrix.front().size() - 1 && map[row][col_right] &&
      matrix[row][col_right] == path[index]) {
    auto temp = map;
    temp[row][col_right] = false;
    result = result ||
             IsPathInMatrixCore(matrix, row, col_right, temp, path, index + 1);
  }

  return result;
}

bool IsPathInMatrix(const std::vector<std::vector<char>> &matrix,
                    const std::vector<char> &path) {
  if (matrix.empty() || path.empty()) {
    return false;
  }

  std::vector<std::vector<bool>> map(
      matrix.size(), std::vector<bool>(matrix.front().size(), true));

  std::vector<char> path_to_find(path);

  for (int row = 0; row < matrix.size(); ++row) {
    for (int col = 0; col < matrix.front().size(); ++col) {
      if (matrix[row][col] == path.front()) {
        auto temp = map;
        temp[row][col] = false;
        return IsPathInMatrixCore(matrix, row, col, temp, path_to_find, 1);
      }
    }
  }

  return false;
}
```

# Moving Count

> There is a $m * n$ matrix. A robot moves from $(0, 0)$ and it can move to left/right/up/down cell, but not the cell whose digital sum of row index and column index is bigger than k.
> For example, $k = 18$, robot can move to $(35, 37)$, because $3 + 5 + 3 + 7 = 18$. But it cannot move to $(35, 38)$, because $3 + 5 + 3 + 8 = 19 > 18$.
> How many cells the robot can reach?
## Solution
```C++
int GetDigitalSum(const int num) {
  int tmp = num;
  int sum = 0;
  while (tmp != 0) {
    sum += tmp % 10;
    tmp = tmp / 10;
  }
  return sum;
}

bool IsReachable(
    const int threshold, const int rows, const int cols, const int row,
    const int col, const std::vector<std::vector<bool>> &visited) {
  if (row >= 0 && row <= rows && col >= 0 && col <= cols &&
      GetDigitalSum(row) + GetDigitalSum(col) <= threshold &&
      !visited[row][col]) {
    return true;
  }
  return false;
}

int GetMovingCountCore(
    const int threshold, const int rows, const int cols, const int row,
    const int col, std::vector<std::vector<bool>> &visited) {
  int count = 0;
  if (IsReachable(threshold, rows, cols, row, col, visited)) {
    visited[row][col] = true;
    count = 1 + 
            GetMovingCountCore(threshold, rows, cols, row - 1, col, visited) +
            GetMovingCountCore(threshold, rows, cols, row + 1, col, visited) +
            GetMovingCountCore(threshold, rows, cols, row, col - 1, visited) +
            GetMovingCountCore(threshold, rows, cols, row, col + 1, visited);
  }
  return count;
}

int GetMovingCount(const int threshold, const int rows, const int cols) {
  if (threshold < 0 || rows < 0 || cols < 0) {
    return 0;
  }

  std::vector<std::vector<bool>> visited(
      rows + 1, std::vector<bool>(cols + 1, false));
  return GetMovingCountCore(threshold, rows, cols, 0, 0, visited);
}
```

# Cut Line
> If there is a line with the length of $n$, please cut the line into $m$ sections($m$ and $n$ are int, and $n > 1$, $m > 1$) and the product of all sections is maximum.
> For example, the line is $18$ long, and we cut it into 3 sections: $2, 3, 3$, the product is maximum: $18$.
## Solution 1
```C++
int GetMaxCuttingDP(const int length) {
  if (length < 2) {
    return 0;
  }

  if (length == 2) {
    return 1;
  }

  if (length == 3) {
    return 2;
  }

  std::vector<int> product;
  product.push_back(0);
  product.push_back(1);
  product.push_back(2);
  product.push_back(3);

  for (int i = 4; i <= length; ++i) {
    int max(0);
    for (int j = 1; j <= i / 2; ++j) {
      int curr_product = product[j] * product[i - j];
      max = max > curr_product ? max : curr_product;
    }
    product.push_back(max);
  }

  return product.back();
}
```
There are two loops in the code, and the time complexity is $O(n^2)$.

## Solution 2
```c++

int GetMaxCuttingGreed(const int length) {
  if (length < 2) {
    return 0;
  }

  if (length == 2) {
    return 1;
  }

  if (length == 3) {
    return 2;
  }

  int ThreeCnt = length / 3;
  if (length % 3 == 1) {
    ThreeCnt--;
  }

  const int TwoCnt = (length - ThreeCnt * 3) / 2;
  return std::pow(3, ThreeCnt) * std::pow(2, TwoCnt);
}
```
This is the solution with the time complexity of $O(n)$.

# The Count of 1 in Binary Number

> Input a integar and output the count of 1 in its binary.
> For example, $9$ in binary is $1001$, so the count of 1 is $2$.
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

# Power of An Integar

> Realize a function to get the integar exponent of a number without the usage of library. You don't need to consider about the big number.
## Solution
```C++
double pos_power(const double base, const int exponent) {
  double result = 1;
  for (int i = 0; i < exponent; ++i) {
    result *= base;
  }
  return result;
}

double power(const double base, const int exponent) {
  if (base == 0) {
    return 0;
  }
  if (exponent == 0) {
    return 1;
  }
  if (exponent == 1) {
    return base;
  }

  const int exp = exponent > 0 ? exponent : -exponent;
  double result = pos_power(base, exp >> 1);
  result *= result;
  result *= exp & 0x01 ? base : 1;
  return exponent > 0 ? result : 1.0 / result;
}
```

# Print The Number From One to Maximum Nth Digits

> Input the number $n$, please print 1 to maximum nth digits in order. For example, input 3, output: 1, 2, 3, ..., 998, 999.
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

# Delete A Node In A List With The Time Complexity Of O(1)

> With a head node pointer and a node pointer of a singly linked node, delete the node in $O(1)$ time.
## Solution
```C++
struct ListNode {
  ListNode(int value = 0) : value(value) {}

  int value;
  ListNode *next;
};

void DeleteLastNode(ListNode* header) {
  ListNode* curr_node = header;
  while (curr_node != nullptr) {
    if (curr_node->next->next == nullptr) {
      curr_node->next = nullptr;
      return;
    }
    curr_node = curr_node->next;
  }
}

void DeleteNode(ListNode* header, ListNode* del_node) {
  if (header == nullptr) {
    return;
  }
  if (header->next == nullptr) {
    header = nullptr;
    return;
  }

  if (del_node->next == nullptr) {
    DeleteLastNode(header);
    return;
  }

  ListNode* curr_node = header;
  while (curr_node != nullptr) {
    if (curr_node->next == del_node) {
      curr_node->next = del_node->next;
      return;
    }
    curr_node = curr_node->next;
  }
}
```

# Regular Expression Pattern Match

> Please relize a function to match the regular expression with "." and "\*".
> The "." represents for any char, and "\*" represents that the char before it can appears any times(0 or more).
> For example, "aaa" matches with the pattern of "a.a" and "ab\*ac\*a" but dismatches with the pattern of "aa.a" and "ab\*a".
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

# Check If The String Can Represent For A Number

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

# Reorder The Array

> Input an array of integar, please reorder the array so that all the odd numbers are in the first half part, and all the even numbers are in the latter half part.
> For example, after reordering, {1, 2, 3, 4, 5} may change to {1, 3, 5, 2, 4}.
## Solution
```C++
#include <algorithm>
#include <vector>

bool IsOdd(const int& num) {
  return num & 0x01;
}

void ReorderOddEven(std::vector<int>& arr, bool (*func)(const int& num)) {
  if (arr.empty()) {
    return;
  }

  int left(0);
  int right(arr.size() - 1);

  while (left < right) {
    while (left < arr.size() && func(arr[left])) {
      left++;
    }
    while (right >= 0 && !func(arr[right])) {
      right--;
    }
    if (left < right) {
      std::swap(arr[left], arr[right]);
    }
  }
}

int main() {
  std::vector arr1{1, 2, 3, 4, 5};
  std::vector arr2{2, 3, 4, 5, 6};

  ReorderOddEven(arr1, IsOdd);
  ReorderOddEven(arr2, IsOdd);
}
```

# Delete Last Kth Node In A List

> Delete the last kth node of a list.
## Solution
```C++
#include <iostream>

struct Node {
  Node(int val = 0) : value(val), next(nullptr) {}
  int value;
  Node* next;

  Node* set_next(int val) {
    next = new Node(val);
    return next;
  }

  void output() {
    std::cout << value;
    if (next != nullptr) {
      std::cout << "->";
      next->output();
    } else {
      std::cout << std::endl;
    }
  }
};

Node* DeleteLastNthNode(Node* head, const int k) {
  if (head == nullptr || k < 1) {
    return nullptr;
  }

  int cnt(1);
  Node* kth_head = head;
  while (cnt++ < k) {
    if (kth_head->next != nullptr) {
      kth_head = kth_head->next;
    } else {
      return nullptr;
    }
  }

  Node* last_kth(head);
  Node* last_kth_front(nullptr);
  while (kth_head->next != nullptr) {
    kth_head = kth_head->next;
    last_kth_front = last_kth;
    last_kth = last_kth->next;
  }

  last_kth_front->next = last_kth->next;
  last_kth->next = nullptr;

  return last_kth;
}

int main() {
  Node* head1 = new Node(1);
  head1->set_next(2)->set_next(3)->set_next(4)->set_next(5);
  head1->output();
  DeleteLastNthNode(head1, 2)->output();
  head1->output();
}
```

# Find The Entrance Of A Loop In A Node List

> If a node list contains a loop, how to find the entrance? 
> For example, the following node list has the loop entrnace of node 3.
> `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3`
## Solution
```C++
struct Node {
  Node(int val = 0) : value(val), next(nullptr) {}
  int value;
  Node* next;

  Node* set_next(int val) {
    next = new Node(val);
    return next;
  }
};

Node* GetOneLoopNode(Node* head) {
  if (head == nullptr) {
    return nullptr;
  }

  Node* slow = head;
  Node* fast = head;

  while (fast->next && fast->next->next) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) {
      return slow;
    }
  }

  return nullptr;
}

int GetLoopCnt(Node* node) {
  if (node == nullptr) {
    return 0;
  }
  int cnt(1);
  Node* head = node;
  while (head->next != nullptr) {
    if (head->next == node) {
      return cnt;
    } else {
      cnt++;
      head = head->next;
    }
  }
  return 0;
}

Node* GetLoopEntrance(Node* head) {
  if (head == nullptr) {
    return nullptr;
  }

  Node* node_in_loop = GetOneLoopNode(head);
  if (node_in_loop == nullptr) {
    return nullptr;
  }

  const int loop_cnt = GetLoopCnt(node_in_loop);

  Node* fast = head;
  Node* slow = head;
  for (auto i = 0; i < loop_cnt; ++i) {
    fast = fast->next;
  }

  while (fast != slow) {
    fast = fast->next;
    slow = slow->next;
  }

  return fast;
}
```

# Reverse Node List

> Realize a function to reverse a node list. Input a head pointer of a node list, please output a pointer of the reversed node list head.
## Solution
```C++
struct Node {
  Node(int val = 0) : value(val) {}

  int value;
  Node* next;
};


Node* ReverseNodeList(Node* head) {
  if (head == nullptr || head->next == nullptr) {
    return head;
  }

  Node* prev_node = head;
  Node* curr_node = head->next;

  Node* next_node(nullptr);
  prev_node->next = nullptr;
  while (curr_node != nullptr) {
    next_node = curr_node->next;
    curr_node->next = prev_node;

    prev_node = curr_node;
    curr_node = next_node;
  }

  return prev_node;
}
```

# Merge Two Sorted Lists

> Please merege two sorted lists, the new list should also be sorted.
> For example, input node1: `1->3->5->7` and `2->4->6->8`, the new list should be `1->2->3->4->5->6->7->8`.


## Solution
```C++
Node* MergeTwoSortedLists(Node* head1, Node* head2) {
  if (head1 == nullptr) {
    return head2;
  }
  if (head2 == nullptr) {
    return head1;
  }

  Node* head;
  Node* curr_list1 = head1;
  Node* curr_list2 = head2;
  if (curr_list1->value < curr_list2->value) {
    head = curr_list1;
    curr_list1 = curr_list1->next;
  } else {
    head = curr_list2;
    curr_list2 = curr_list2->next;
  }

  Node* result = head;

  while (curr_list1 != nullptr && curr_list2 != nullptr) {
    if (curr_list1->value < curr_list2->value) {
      head->next = curr_list1;
      head = head->next;
      curr_list1 = curr_list1->next;
    } else {
      head->next = curr_list2;
      head = head->next;
      curr_list2 = curr_list2->next;
    }
  }

  if (curr_list1 != nullptr) {
    head->next = curr_list1;
  }
  if (curr_list2 != nullptr) {
    head->next = curr_list2;
  }

  return result;
}
```

# Subtree Of A Tree

> Input two binary trees A and B, please check if B is a subtree of A


## Solution
```C++
struct Tree {
  Tree(int value = 0) : value(value), left(nullptr), right(nullptr) {}

  int value;
  Tree* left;
  Tree* right;
};

bool IsSubTreeMatched(Tree* root, Tree* sub) {
  if (sub == nullptr) {
    return true;
  }

  if (root == nullptr) {
    return false;
  }

  return root->value == sub->value &&
         IsSubTreeMatched(root->left, sub->left) &&
         IsSubTreeMatched(root->right, sub->right);
}

bool IsSubTree(Tree* origin, Tree* sub) {
  if (origin == nullptr || sub == nullptr) {
    return false;
  }

  bool result = false;
  if (origin->value == sub->value) {
    result = IsSubTreeMatched(origin, sub);
  }

  return result || IsSubTree(origin->left, sub) ||
         IsSubTree(origin->right, sub);
}
```

# The Mirror Of A BinaryTree

> Please realize a function to output the mirror of a binary tree.
> For example, input tree is left one, and output tree is right one.

```C++
    8          8    
   / \        / \   
  6  10      10  6  
 / \ / \    / \ / \ 
5  7 9 11  11 9 7  5
```


## Solution
```C++
void MirrorBinaryTree(BinaryTreeNode* root) {
  if (root == nullptr) {
    return;
  }

  BinaryTreeNode* tmp = root->left;
  root->left = root->right;
  root->right = tmp;

  MirrorBinaryTree(root->left);
  MirrorBinaryTree(root->right);
}
```

# The Symmetry Of A Binary Tree

> Check a symmetric binary tree. For example, the left is symmetric and the right is not.
```
    8          8    
   / \        / \   
  6   6      6   9
 / \ / \    / \ / \ 
5  7 7  5   5 7 7 5
```


## Solution
```C++
struct BinTreeNode {
 BinTreeNode(int val = 0) : value(val), left(nullptr), right(nullptr) {}

 int value;
 BinTreeNode* left;
 BinTreeNode* right;
};

bool IsSymmetryTwo(BinTreeNode* root1, BinTreeNode* root2) {
  if (root1 == nullptr && root2 == nullptr) {
    return true;
  }

  if (root1 == nullptr || root2 == nullptr) {
    return false;
  }

  if (root1->value != root2->value) {
    return false;
  }

  return IsSymmetryTwo(root1->left, root2->right) &&
         IsSymmetryTwo(root1->right, root2->left);
}

bool IsSymmetry(BinTreeNode* root) {
  return IsSymmetryTwo(root, root);
}
```

# Print Matrix Clockwise

> Please print a matrix in clockwise. For example, the matrix is:
```C++
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
```
> print the number: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

## Solution
```C++
void PrintMatrixCircle(
    const std::vector<std::vector<int>>& matrix, const int start) {
  if (matrix.empty() || start < 0) {
    return;
  }

  const int row_max = matrix.size() - start - 1;
  const int col_max = matrix.front().size() - start - 1;


  // first step
  for (int i = start; i <= col_max; ++i) {
    std::cout << matrix[start][i] << " ";
  }

  // second step
  if (start < row_max) {
    for (int i = start + 1; i <= row_max; ++i) {
      std::cout << matrix[i][col_max] << " ";
    }
  }

  // third step
  if (start < row_max && start < col_max) {
    for (int i = col_max - 1; i >= start; --i) {
      std::cout << matrix[row_max][i] << " ";
    }
  }

  // forth step
  if (start < row_max - 1 && start < col_max) {
    for (int i = row_max - 1; i >= start + 1; --i) {
      std::cout << matrix[i][start] << " ";
    }
  }
}

void PrintMatrixReverse(const std::vector<std::vector<int>>& matrix) {
  if (matrix.empty()) {
    return;
  }

  int start(0);
  while (start * 2 < matrix.front().size() && start * 2 < matrix.size()) {
    PrintMatrixCircle(matrix, start);
    start++;
  }
}
```

# A Min Stack

> Define a stack that can output its min value.
> The time complexity of `min`, `push`, `pop` methods of the stack must be $O(1)$.

## Solution
```C++
#include <limits>

template <typename T>
class MyStack {
 public:
  MyStack() : head_(nullptr) {}
  ~MyStack() {
    while (head_ != nullptr) {
      Node* tmp = head_;
      head_ = head_->next;
      delete tmp;
    }
  };

 public:
  void push(T val) {
    Node* new_node = new Node(val);
    new_node->next = head_;
    head_ = new_node;
  }

  T pop() {
    if (head_ == nullptr) {
      return std::numeric_limits<T>::max();
    }

    T value = head_->value;
    Node* tmp = head_;
    head_ = head_->next;

    delete tmp;
    return value;
  }

  T top() {
    if (head_ == nullptr) {
      return std::numeric_limits<T>::max();
    }

    return head_->value;
  }

  bool empty() {
    return head_ == nullptr;
  }

 private:
  struct Node {
    Node(T val = 0) : value(val), next(nullptr) {}

    T value;
    Node* next;
  };

  Node* head_;
};

template <typename T>
class MinStack {
 public:
  MinStack() = default;
  ~MinStack() = default;
 
 public:
  void push(T value) {
    data_.push(value);
    assist_.push(value < assist_.top() ? value : assist_.top());
  }

  T pop() {
    if (data_.empty()) {
      return std::numeric_limits<T>::max();
    }

    assist_.pop();
    data_.pop();
  }

  T top() {
    if (data_.empty()) {
      return std::numeric_limits<T>::max();
    }

    return data_.top();
  }

  T min() {
    if (assist_.empty()) {
      return std::numeric_limits<T>::max();
    }
    return assist_.top();
  }

 private:
  MyStack<T> data_;
  MyStack<T> assist_;
};
```

# The Push And Pop Sequences Of Stack

> Input two integar sequences, the first is the push order of a stack, please check if the second is one of the pop order of the stack. Assume that all the numbers in the stack are different.
> For exmaple, `{1, 2, 3, 4, 5}` is a push order of a stack, `{4, 5, 3, 2, 1}` can be its pop order, but `{4, 3, 5, 1, 2}` can not be.

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

# Print A Binary Tree From Top To Bottom

## Print Binary Tree Without Line Split
> Print all nodes of a binary tree whithout line split, for the nodes in the same level, print them from left to right.
> For example, a binary tree:
```C++
       8
      / \
     6  10 
    / \ / \
   5  7 9 11
```
> should be printed as `8, 6, 10, 5, 7, 9, 11`.

### Solution
```C++
struct BinNode {
  BinNode(int val = 0) : value(val), left(nullptr), right(nullptr) {}

  int value;
  BinNode* left;
  BinNode* right;
};

void PrintBinTree(const BinNode* root) {
  if (root == nullptr) {
    return;
  }

  std::deque<const BinNode*> out;
  out.push_back(root);
  while (!out.empty()) {
    const BinNode* parrent = out.front();
    out.pop_front();
    std::cout << parrent->value << " ";

    if (parrent->left != nullptr) {
      out.push_back(parrent->left);
    }
    if (parrent->right != nullptr) {
      out.push_back(parrent->right);
    }
  }

  std::cout << std::endl;
}
```

## Print Binary Tree With Line Split
> Please print the binary tree with line split, the output of the tree is:
```C++
8
6 10
5 7 9 11
```

### Solution
```C++
void PrintBinTreeLineSplit(const BinNode* root) {
  if (root == nullptr) {
    return;
  }

  std::deque<const BinNode*> out;
  out.push_back(root);
  std::size_t curr_level_cnt = 1;
  std::size_t next_level_cnt = 0;
  while (!out.empty()) {
    const BinNode* parrent = out.front();
    out.pop_front();
    std::cout << parrent->value << " ";
    curr_level_cnt--;

    if (parrent->left != nullptr) {
      out.push_back(parrent->left);
      next_level_cnt++;
    }
    if (parrent->right != nullptr) {
      out.push_back(parrent->right);
      next_level_cnt++;
    }

    if (curr_level_cnt == 0) {
      std::cout << std::endl;
      curr_level_cnt = next_level_cnt;
      next_level_cnt = 0;
    }
  }

  std::cout << std::endl;
}
```

## Print Binary Tree in z order
> Please print the binary tree with line split in z order, the output of the tree is:
```C++
8
6 10
5 7 9 11
```

### Solution
```C++
void PrintBinTreeLineZ(const BinNode* root) {
  if (root == nullptr) {
    return;
  }

  std::array<std::stack<const BinNode*>, 2> out;
  std::size_t curr_index = 0;
  std::size_t next_index = 1;
  out[curr_index].push(root);
  while (!out[0].empty() || !out[1].empty()) {
    const BinNode* parrent = out[curr_index].top();
    out[curr_index].pop();
    std::cout << parrent->value << " ";

    if (curr_index == 0) {
      if (parrent->left != nullptr) {
        out[next_index].push(parrent->left);
      }
      if (parrent->right != nullptr) {
        out[next_index].push(parrent->right);
      }
    } else {
      if (parrent->right != nullptr) {
        out[next_index].push(parrent->right);
      }
      if (parrent->left != nullptr) {
        out[next_index].push(parrent->left);
      }
    }

    if (out[curr_index].empty()) {
      std::cout << std::endl;
      curr_index = 1 - curr_index;
      next_index = 1 - next_index;
    }
  }

  std::cout << std::endl;
}
```

# Check Binary Search Tree Post Order

> Please check if the list is a post order travesal result of a binary search tree.
> Assume that there are no repeated numbers in the list.
> For example, `{5, 7, 6, 9, 11, 10, 8}` is a post order travesal result of the binary search tree:
```C++
       8
      / \
     6  10 
    / \ / \
   5  7 9 11
```
> and, `{7, 4, 6, 5}` is not a post order travesal result of any binary search tree.

## Solution
```C++
bool IsBinSearchTreePostOrder(
    std::vector<int>::iterator it_begin, std::vector<int>::iterator it_end) {
  if (it_begin == it_end) {
    return true;
  }

  auto left_child = it_begin;
  while (left_child != it_end) {
    if (*left_child > *it_end) {
      break;
    }
    left_child++;
  }

  auto right_child = left_child;
  while (right_child != it_end) {
    if (*right_child < *it_end) {
      return false;
    }
    right_child++;
  }

  return IsBinSearchTreePostOrder(it_begin, left_child - 1) &&
         IsBinSearchTreePostOrder(left_child, it_end - 1);
}
```

# Print The Path Whose Sum Is A Given Value Of A Binary Tree

> Input a binary tree and an integar, please print all the paths whose sum is the integar.
> For example, with the binary tree:
```C++
     10
    / \
   5  12
  / \ 
 4  7 
```
> and the sum integar 12, the path is `10 12` and `10 5 7`.

## Solution
```C++
struct BinNode {
  BinNode(int val = 0) : value(val), left(nullptr), right(nullptr) {}

  int value;
  BinNode* left;
  BinNode* right;
};

int SumStack(const std::vector<int>& path) {
  return std::accumulate(path.begin(), path.end(), 0);
}

void PrintStack(const std::vector<int>& path) {
  std::for_each(path.begin(), path.end(), 
                [](int ele) { std::cout << ele << " "; });
  std::cout << std::endl;
}

void PrintBinTreePathSum(
    const BinNode* root, const int sum, std::vector<int>& path) {
  path.push_back(root->value);
  if (root->left == nullptr && root->right == nullptr && SumStack(path) == sum) {
    PrintStack(path);
  }

  if (root->left != nullptr) {
    PrintBinTreePathSum(root->left, sum, path);
  }

  if (root->right != nullptr) {
    PrintBinTreePathSum(root->right, sum, path);
  }
  path.pop_back();
}

void PrintBinTreeSum(const BinNode* root, const int sum) {
  if (root == nullptr) {
    return;
  }

  std::vector<int> path;
  PrintBinTreePathSum(root, sum, path);
}
```

# Copy Of Complex List Node

> Please realize a function to copy a complex list node. The defination of complex list node is as below:
```C++
struct Node {
  Node(int val = 0) : value(val), sibling(nullptr), next(nullptr) {}

  int value;
  Node* sibling;
  Node* next;
};
```

> And the picture is like this:
```C++
      +---------+
      |         |
+-+  +v+  +-+  +++  +-+
|A+-->B+-->C+-->D+-->E|
+++  +++  +^+  +-+  +^+
 |    |    |         |
 +---------+         |
      +--------------+
```

## Solution
```C++
void CopyEachNode(Node* origin) {
  Node* head = origin;
  while (head != nullptr) {
    Node* tmp = head->next;
    head->next = new Node(head->value);
    head->next->next = tmp;
    head = tmp;
  }
}

void CopySibingInfo(Node* origin) {
  Node* head = origin;
  while (head != nullptr) {
    Node* tmp = head->sibling;
    if (tmp != nullptr) {
      head->next->sibling = tmp->next;
    }
    head = head->next->next;
  }
}

Node* SplitTwoList(Node* origin) {
  Node* even_head = origin->next;
  Node* curr_odd = origin;
  Node* curr_even = even_head;
  Node* curr_node = even_head->next;
  int curr_node_cnt(1);
  while (curr_node != nullptr) {
    if (curr_node_cnt & 1) {
      curr_odd->next = curr_node;
      curr_odd = curr_odd->next;
    } else {
      curr_even->next = curr_node;
      curr_even = curr_even->next;
    }
    curr_node = curr_node->next;
    curr_node_cnt++;
  }

  return even_head;
}

Node* CopyNodeList(Node* origin) {
  if (origin == nullptr) {
    return nullptr;
  }

  CopyEachNode(origin);
  CopySibingInfo(origin);
  return SplitTwoList(origin);
}
```

# Convert A Binary Search Tree To A Doubly Linked List

> Please convert a binary search tree to a doubly linked list. Creating new space is not allowed, and the doubly linked list should be sorted.
> For example, the binary search tree:
```C++
    10
   / \
  6   14
 / \ / \
4  8 12 16
```
> should be converted to:
```C++
  ->   ->   ->    ->    ->    -> 
4    6    8    10    12    14
  <-   <-   <-    <-    <-    <-
```

## Solution
```C++
struct Node {
  Node(int value = 0) : value(value), left(nullptr), right(nullptr) {}

  int value;
  Node* left;
  Node* right;
};

void Convert(Node* root, Node*& list_last) {
  if (root->left != nullptr) {
    Convert(root->left, list_last);
  }

  if (list_last == nullptr) {
    list_last = root;
    return;
  }

  list_last->right = root;
  root->left = list_last;
  list_last = root;

  if (root->right != nullptr) {
    Convert(root->right, list_last);
  }
}

Node* ConvertBinTreeToNodeList(Node* root) {
  if (root == nullptr) {
    return nullptr;
  }

  Node* list_last = nullptr;
  Convert(root, list_last);

  Node* result = root;
  while (result->left != nullptr) {
    result = result->left;
  }
  return result;
}
```


# Serialize And Deserialize A Binary Tree

> Please realize two functions to serialize and deserialize a binary tree.

## Solution
```C++
constexpr int INVALID_INT = -255;

struct Node {
  Node(int value = 0) : value(value), left(nullptr), right(nullptr) {}

  int value;
  Node* left;
  Node* right;
};

void Serialize(Node* root, std::queue<int>& ser) {
  if (root == nullptr) {
    ser.push(INVALID_INT);
    return;
  }

  ser.push(root->value);
  Serialize(root->left, ser);
  Serialize(root->right, ser);
}

void Deserialize(Node*& root, std::queue<int>& ser) {

  if (!ser.empty() && ser.front() != INVALID_INT) {
    root = new Node(ser.front());
    ser.pop();

    Deserialize(root->left, ser);
    Deserialize(root->right, ser);
  } else {
    ser.pop();
  }
}
```

# The Permutations Of String

> Please print all the permutations of a string. For example, "abc" can be:
> abc, acb, bac, bca, cab and cba.

## Solution
```C++
void PrintPermutations(std::string& str, const int curr_index) {
  if (curr_index == str.size() - 1) {
    std::cout << str << std::endl;
  } else {
    for (int i = curr_index; i < str.size(); ++i) {
      std::swap(str[curr_index], str[i]);
      PrintPermutations(str, curr_index + 1);
      std::swap(str[curr_index], str[i]);
    }
  }
}

void PrintAllPermutations(const std::string& str) {
  if (str.empty()) {
    return;
  }

  std::string tmp(str);
  PrintPermutations(tmp, 0);
}
```

# The Number Appears More Than Half Of The Length Times Of Array 

> A number appears more than half of the length of the list times, please find it out. 
> For example, in the list `{1, 2, 3, 2, 2, 2, 5, 4, 2}`, the `2` is the number.

## Solution
```C++
int NumAppearMoreThanHalf(const std::vector<int>& arr) {
  if (arr.empty()) {
    return -1;
  }

  int base = arr.front();
  int base_cnt = 0;

  for (const auto &ele : arr) {
    if (ele == base) {
      base_cnt++;
    } else if (base_cnt > 0) {
      base_cnt--;
    } else {
      base = ele;
      base_cnt = 1;
    }
  }

  return base;
}
```

# The Smallest K Numbers Of The List

> Input a list of n numbers, please find the smallest k numbers.
> For example, the smallest `4` numbers of the list `4, 5, 1, 6, 2, 7, 3, 8` is:
> `1, 2, 3, 4`.

## Solution
```C++
bool GetMinKNumbers(
    const std::vector<int>& arr, const int k,
    std::multiset<int, std::greater<int>>* const result) {
  if (k > arr.size() || k <= 0) {
    return false;
  }

  std::multiset<int, std::greater<int>> tmp(arr.begin(), arr.begin() + k);
  result->swap(tmp);

  auto it = arr.begin() + k;
  while (it != arr.end()) {
    if (*it < *result->begin()) {
      result->erase(result->begin());
      result->insert(*it);
    }

    it++;
  }

  return true;
}
```

# The Median In A Stream

> Get the median of a data stream.

## Solution
```
class StreamMedian {
 public:
  StreamMedian() = default;
  ~StreamMedian() = default;

  void Insert(const int value) {
    if (min_heap_.size() == max_heap_.size()) {
      min_heap_.push(value);
      max_heap_.push(min_heap_.top());
      min_heap_.pop();

    } else {
      max_heap_.push(value);
      min_heap_.push(max_heap_.top());
      max_heap_.pop();
    }
  }

  int Median() const {
    const int num_cnt = min_heap_.size() + max_heap_.size();
    if (num_cnt == 0) {
      return -1;
    }

    if (num_cnt & 1) {
      return max_heap_.top();
    }

    return (max_heap_.top() + min_heap_.top()) / 2;
  }

 private:
  std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap_;
  std::priority_queue<int, std::vector<int>, std::less<int>> max_heap_;
};
```

# Greatest Sum Of Subarray

> Input a integar array, elements of the array can be positive or negtive, please output the maximum sum of its subarray. 

## Solution
```
int MaxSubarray(const std::vector<int>& arr) {
  if (arr.empty()) {
    return -1;
  }

  int max= std::numeric_limits<int>::min();
  int sum = 0;
  for (const auto& ele : arr) {
    sum += ele;
    max = std::max(sum, max);
    sum = sum < 0 ? 0 : sum;
  }

  return max;
}
```

# Find The Occurences Of 1 In Range 1-n

> Find the occurences of 1 in range `1-n`.

## Solution
```
int GetNumLength(int num) {
  int cnt(0);
  while (num != 0) {
    num /= 10;
    cnt ++;
  }

  return cnt;
}

int OneAppearance(const int num) {
  if (num <= 0) {
    return 0;
  }

  const int length = GetNumLength(num);
  if (length == 1) {
    return 1;
  }

  const int tmp = std::pow(10, length - 1);
  const int first = num / tmp;
  const int top_one_cnt = first == 1 ? num % tmp + 1 : std::pow(10, length - 1);
  const int top_other_cnt = first * (length - 1) * std::pow(10, length - 2);
  const int sub_cnt = OneAppearance(num % 10);

  return top_one_cnt + top_other_cnt + sub_cnt;
}
```

# Digit In Data Stream

> There is a number stream: "0123456789101112131415...", in this stream, the 5th digit is `5`, 13th digit is `1`, 19th digit is `4`.
> Please output the number of any digit.

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

# Rerange The List To Min Number

> Rerange all the numbers in a list, please print the minimum number of reranged list. For example, input the list `{3, 32, 321}`, you should print `321323`.

## Solution
```C++
void PrintMinArray(std::vector<int>& arr) {
  if (arr.empty()) {
    return;
  }
  std::sort(arr.begin(), arr.end(),
            [](int a, int b) {
              return std::stoi(std::to_string(a) + std::to_string(b)) < 
                     std::stoi(std::to_string(b) + std::to_string(a));
            });

  for (auto ele : arr) {
    std::cout << ele;
  }
  std::cout << std::endl;
}
```

# Translate Integar to String

> With an integar given, we translate the number digits to string with the rule: 0 to "a", 1 to "b", ..., 11 to "l", ..., 25 to "z". An integar may have more than one translation, for example, 12248 has 5 different translations: "bccfi", "bwfi", "bczi", "mcfi" and "mzi". Please find the number of translation methods of an integar.

```C++
std::size_t TransNumberToString(const std::size_t num) {
  const std::string num_str = std::to_string(num);
  const std::size_t length(num_str.size());
  if (length < 2) {
    return 1;
  }

  std::vector<int> sum(length + 1, 0);
  sum[length - 1] = 1;
  sum[length] = 1;
  for (int i = length - 2; i >= 0; --i) {
    sum[i] = sum[i + 1];
    const int tmp = std::stoi(std::string(1, num_str[i]) +
                              std::string(1, num_str[i + 1]));
    if (tmp < 26) {
      sum[i] += sum[i + 2];
    }
  }

  return sum.front();
}
```

# Maximum Gift Value

> Every grid of a 2d vector has a gift, and every gift has a value(bigger than 0). You start from the top left of vector exit from right bottom. So what's the maximum gift value you can get?
> For example, a 2d vector like:
```C++
1 10 3 8
12 2 9 6
5 7 4 11
3 7 16 5
```
> you can get the maximum git value if you go through: `1 -> 12 -> 5 -> 7 -> 7 -> 16 -> 5`.

## Solution
```C++
int MaxGiftValue(const std::vector<std::vector<int>>& map) {
  if (map.empty()) {
    return 0;
  }

  const int row_cnt = map.size();
  const int col_cnt = map.front().size();
  std::vector<std::vector<int>> gift_values(
      row_cnt, std::vector<int>(col_cnt, 0));

  for (int i = 0; i < row_cnt; ++i) {
    for (int j = 0; j < col_cnt; ++j) {
      const int left = j - 1 >= 0 ? gift_values[i][j - 1] : 0;
      const int up = i - 1 >= 0 ? gift_values[i - 1][j] : 0;

      gift_values[i][j] = std::max(left, up) + map[i][j];
    }
  }

  return gift_values.back().back();
}
```

# Length of the longest substring without repeated charactors

> Please find the longest substring without repeated charactors of a string and output its length.
> Forexample, in string "arabcacfr" the longest substring without repeated charactors is "acfr", and its length is 4.

## Solution
```
int MaximumSubstringWithoutRepeat(const std::string& str) {
  if (str.empty()) {
    return 0;
  }

  std::unordered_map<char, int> substring_idxs;
  int max_length(0);
  int start_idx(0);

  for (int i = 0; i < str.size(); ++i) {
    auto it = substring_idxs.find(str[i]);
    if (it != substring_idxs.end()){
      const int new_start = it->second + 1;
      for (auto j = start_idx; j < new_start; ++j) {
        substring_idxs.erase(str[j]);
      }
      start_idx = new_start;
    }
    substring_idxs[str[i]] = i;
    max_length = std::max(max_length, i - start_idx + 1);
  }

  return max_length;
}
```

# Kth ugly number

> The number that contains only 2, 3, 5 is called ugly number. In general, 1 is the first ugly number. For example, 6, 8 are ugly numbers but 17 not.
> Please output kth ugly number.

## Solution
```C++
int KthUglyNumber(const int k) {
  if (k < 1) {
    return -1;
  }

  int ugly_base_2 = 0;
  int ugly_base_3 = 0;
  int ugly_base_5 = 0;
  std::vector<int> ugly_list;
  ugly_list.push_back(1);
  int curr_ugly_cnt = 1;
  while (curr_ugly_cnt < k) {
    ugly_list.push_back(
        std::min(std::min(ugly_list[ugly_base_2] * 2,
                          ugly_list[ugly_base_3] * 3),
                 ugly_list[ugly_base_5] * 5));
    while (ugly_list[ugly_base_2] * 2 <= ugly_list.back()) {
      ugly_base_2++;
    }
    while (ugly_list[ugly_base_3] * 3 <= ugly_list.back()) {
      ugly_base_3++;
    }
    while (ugly_list[ugly_base_5] * 5 <= ugly_list.back()) {
      ugly_base_5++;
    }

    curr_ugly_cnt++;
  }

  return ugly_list.back();
}
```

# First Charactor that Occurs Only Once

> Find the charactor that only occurs once in a string. For example, in "abaccdeff", 'b' occurs only once.

## Solution
```C++
char FirstNoRepeatChar(const std::string& str) {
  if (str.empty()) {
    return ' ';
  }

  std::unordered_map<char, int> map_char_cnt;
  for (const auto& c : str) {
    if (map_char_cnt.find(c) == map_char_cnt.end()) {
      map_char_cnt[c] = 1;
    } else {
      map_char_cnt[c] += 1;
    }
  }

  for (const auto& c : str) {
    if (map_char_cnt[c] == 1) {
      return c;
    }
  }

  return ' ';
}
```

# Inverse Pairs in Array

> If there are two numbers in array, the number in front is bigger than the number in back, they form an inverse pair. For example, in the list `{7, 5, 6, 4}`, there are 5 inverse pairs: `(7, 6), (7, 5), (7, 4), (6, 4), (5, 4)`. Inpu an array, please output the number of inverse pairs.

## Solution
```C+++
int GetInversePairs(std::vector<int>& arr, int start, int end) {
  if (start == end) {
    return 0;
  }

  int mid = (end + start) / 2;
  int left_cnt = GetInversePairs(arr, start, mid);
  int right_cnt = GetInversePairs(arr, mid + 1, end);

  int merge_cnt = 0;
  int left_end = mid;
  int right_end = end;
  std::vector<int> tmp;
  while (left_end >= start && right_end >= mid + 1) {
    if (arr[left_end] > arr[right_end]) {
      merge_cnt += right_end - mid;
      tmp.push_back(arr[left_end]);
      left_end--;
    } else {
      tmp.push_back(arr[right_end]);
      right_end--;
    }
  }
  while (left_end >= start) {
    tmp.push_back(arr[left_end]);
    left_end--;
  }
  while (right_end >= mid + 1) {
    tmp.push_back(arr[right_end]);
    right_end--;
  }
  for (int i = end; i >= start; --i) {
    arr[i] = tmp[end - i];
  }

  return left_cnt + right_cnt + merge_cnt;
}

int InversePairsCount(std::vector<int>& arr) {
  if (arr.empty()) {
    return 0;
  }

  return GetInversePairs(arr, 0, arr.size() - 1);
}
```

# First Public Node

> Input two node list, please find their first public node.

## Solution
```C++
struct Node {
  Node(int val = 0) : value(val), next(nullptr) {}
  int value;
  Node* next;
};

Node* FirstPublicNode(Node* first, Node* second) {
  if (first == nullptr || second == nullptr) {
    return nullptr;
  }

  int first_length(0);
  Node* tmp = first;
  while (tmp != nullptr) {
    first_length++;
    tmp = tmp->next;
  }

  int second_length(0);
  tmp = second;
  while (tmp != nullptr) {
    second_length++;
    tmp = tmp->next;
  }

  Node* head_first = first;
  Node* head_second = second;
  if (first_length > second_length) {
    int skip_cnt = first_length - second_length;
    while (skip_cnt > 0) {
      head_first = head_first->next;
      skip_cnt--;
    }
  } else {
    int skip_cnt = second_length - first_length ;
    while (skip_cnt > 0) {
      head_second = head_second->next;
      skip_cnt--;
    }
  }

  while (head_first != nullptr && head_second != nullptr) {
    if (head_first->value == head_second->value) {
      return head_first;
    }
    head_first = head_first->next;
    head_second = head_second->next;
  }
  return nullptr;
}
```

# Kth Node in Binary Search Tree

> Please find the kth node of the binary search tree. For example, in the below tree:
```C++
    5
   / \
  3   7
 / \ / \
2  4 6  8
```
> the 3th node is 4

## Solution
```C++
struct Node {
  int value;
  Node* left;
  Node* right;

  Node(int val = 0) : value(val), left(nullptr), right(nullptr) {}
};

const Node* KthNodeRecurse(const Node* root, int& k) {
  if (root == nullptr) {
    return nullptr;
  }

  const Node* target = KthNodeRecurse(root->left, k);

  if (k == 1) {
    if (target != nullptr) {
      return target;
    }

    return root;
  }

  k--;
  target = KthNodeRecurse(root->right, k);

  return k == 1 && target != nullptr ? target : nullptr;
}

const Node* KthNode(const Node* root, int num) {
  if (root == nullptr || num < 1) {
    return nullptr;
  }

  return KthNodeRecurse(root, num);
}
```

# Look up Number in Array 

> Input an array and a number, please output how many times the number occurs in the array.
> For example, in the array `{1, 2, 3, 3, 3, 3, 4, 5}` the number `3` occurs 4 times.

## Solution
```C++
int GetLeftIndex(
    const std::vector<int>& arr, const int num, int start, int end) {
  if (start < 0 || end < start) {
    return -1;
  }

  int mid = (end + start) / 2;

  if (arr[mid] == num) {
    if (mid == 0 || arr[mid - 1] < num) {
      return mid;
    }

    return GetLeftIndex(arr, num, start, mid - 1);
  }

  if (arr[mid] > num) {
    return GetLeftIndex(arr, num, start, mid - 1);
  }

  return GetLeftIndex(arr, num, mid + 1, end);
}

int GetRightIndex(
    const std::vector<int>& arr, const int num, int start, int end) {
  if (start < 0 || end < start) {
    return -1;
  }

  int mid = (end + start) / 2;

  if (arr[mid] == num) {
    if (mid == arr.size() - 1 || arr[mid + 1] > num) {
      return mid;
    }

    return GetRightIndex(arr, num, mid + 1, end);
  }

  if (arr[mid] > num) {
    return GetRightIndex(arr, num, start, mid - 1);
  }

  return GetRightIndex(arr, num, mid + 1, end);
}

int TimesInArray(const std::vector<int>& arr, const int num) {
  if (arr.empty()) {
    return -1;
  }

  int left = GetLeftIndex(arr, num, 0, arr.size() - 1);
  int right = GetRightIndex(arr, num, left, arr.size() - 1);

  if (left >= 0 && right >= 0) {
    return right - left + 1;
  }

  return -1;
}
```

# Depth of Binary Search Tree

> Please ouput the maximum depth of a BST.

## Solution
```C++
struct Node {
  int value;
  Node* left;
  Node* right;

  Node(int val = 0) : value(val), left(nullptr), right(nullptr) {}
};

int DepthBinarySearchTree(Node* root) {
  if (root == nullptr) {
    return 0;
  }

  int left = DepthBinarySearchTree(root->left);
  int right = DepthBinarySearchTree(root->right);

  return left > right ? left + 1 : right + 1;
}
```

# Two Numbers That occurs Only Once in List 

> In an integar array, all numbers appears twice except two, please output them.
> You should realize the function within time complexity of $O(n)$ and space complexity of $O(1)$.

## Solution
```C++
int FirstOneDigit(int num) {
  int result(0);
  while((num & 1) == 0 && result < 8 * sizeof(int)) {
    num = num >> 1;
    result++;
  }

  return result;
}

bool IsDigitKOne(int num, int k) {
  num = num >> k;
  return num & 1;
}

std::pair<int, int> TwoTimesNumber(const std::vector<int>& arr) {
  if (arr.empty()) {
    return {-1, -1};
  }

  int result_or(0);
  for (auto num : arr) {
    result_or ^= num;
  }

  int digit_one = FirstOneDigit(result_or);

  int result1(0);
  int result2(0);

  for (auto num : arr) {
    if (IsDigitKOne(num, digit_one)) {
      result1 ^= num;
    } else {
      result2 ^= num;
    }
  }

  return {result1, result2};
}
```

# Sum of The Numbers

> With a sorted array and a number `s`, please output two numbers in the array whose sum is `s`.

## solution
```C++
std::pair<int, int> SumNumbers(const std::vector<int>& arr, const int num) {
  if (arr.empty()) {
    return {0, 0};
  }

  int start = 0;
  int end = arr.size() - 1;
  while (end > start) {
    if (arr[start] + arr[end] > num) {
      end--;
    } else if (arr[start] + arr[end] < num) {
      start++;
    } else {
      return {arr[start], arr[end]};
    }
  }

  return {0, 0};
}
```

# Reverse Words

> With a positive integar `s`, please output all the positive continuous integar sequences whose sum is `s`. For example, with the input of `15`, the output would be `1, 2, 3, 4, 5`, `4, 5, 6` and `7, 8`.

## Solution
```C++
void PrintVec(int start, int end) {
  while (start < end) {
    std::cout << start << " ";
    start++;
  }
  std::cout << end << std::endl;
}

void SumSequence(const int num) {
  if (num < 2) {
    return;
  }

  int start = 1;
  int end = 2;
  int sum = 3;

  while (end < num) {
    if (sum > num) {
      sum -= start;
      start++;
    } else if (sum < num) {
      end++;
      sum += end;
    } else {
      PrintVec(start, end);
      end++;
      sum += end;
    }
  }
}
```

# Maximum of the List
> Given a vector and a sliding window, please find all the maximum number in the sliding window. For example, input vector {2, 3, 4, 2, 6, 2, 5, 1} and sliding window 3, then there are 6 sliding windows, all the maximum numbers are {4, 4, 6, 6, 6, 5}.

## Solution
```C++
std::vector<int> MaxNum(const std::vector<int>& arr, const int window) {
  if (arr.empty() || window < 1) {
    return {};
  }

  std::deque<int> indices;
  indices.push_back(0);
  std::vector<int> max;
  for (std::size_t i = 1; i < arr.size(); ++i) {
    if (i - indices.front() >= window) {
      indices.pop_front();
    }
    if (arr[i] > arr[indices.front()]) {
      indices.clear();
      indices.push_back(i);
    } else {
      if (indices.size() == 1) {
        indices.push_back(i);
      } else {
        if (arr[indices.back()] < arr[i]) {
          indices.pop_back();
          indices.push_back(i);
        }
      }
    }

    if (i >= window - 1) {
      max.push_back(arr[indices.front()]);
    }
  }

  return max;
}
```

