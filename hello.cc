#include <iostream>
#include <vector>

struct Node {
  explicit Node(int val = 0) : val(val), next(nullptr) {}

  int val;
  Node* next;
};

int main() {
  std::cout << "hello, world" << std::endl;

  auto* tmp = new Node();
  std::cout << tmp->val << std::endl;

  //std::cout << tmp->next->val << std::endl;
  delete tmp;

  return 1.0 / 0.0;
}
