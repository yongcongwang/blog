---
title: Design Patterns in C++
date: 2019-06-05 20:44:42
categories: coding
tags:
 - data structure
---

# Strategy Pattern
## Intent
- Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from the clients that use it.
- Capture the abstraction in an interface, bury implementation details in derived classes.
<!-- more -->
![strategy](https://raw.githubusercontent.com/yongcongwang/images/d61aba476dd49b0750f290467cfa5fc2e5da917b/blog/2019/strategy.svg)

```C++
// By yongcong.wang @ 09/06/2019
#include <iostream>

class Strategy {
 public:
  explicit Strategy() {}
  virtual ~Strategy() {}

  virtual void exec() = 0;

 private:
  Strategy(const Strategy &rhs);
  Strategy &operator=(const Strategy &rhs);
};

class ConcreteStrategyA : public Strategy {
 public:
  explicit ConcreteStrategyA () : Strategy() {}
  ~ConcreteStrategyA() {}

  void exec() {
    std::cout << "StrategyA: exec()" << std::endl;
  }

 private:
  ConcreteStrategyA(const ConcreteStrategyA &rhs);
  ConcreteStrategyA &operator=(const ConcreteStrategyA &rhs);
};

class ConcreteStrategyB : public Strategy {
 public:
  explicit ConcreteStrategyB () : Strategy() {}
  ~ConcreteStrategyB() {}

  void exec() {
    std::cout << "StrategyB: exec()" << std::endl;
  }

 private:
  ConcreteStrategyB(const ConcreteStrategyB &rhs);
  ConcreteStrategyB &operator=(const ConcreteStrategyB &rhs);
};

class Context {
 public:
  explicit Context(Strategy *strategy) : strategy_(strategy) {}
  ~Context() {}

  void setStrategy(Strategy *strategy) {
    strategy_ = strategy;
  }

  void exec() {
    strategy_->exec();
  }

 private:
  Context(const Context &rhs);
  Context &operator=(const Context &rhs);

  Strategy *strategy_;
};

int main() {
  ConcreteStrategyA str_a;
  ConcreteStrategyB str_b;

  std::cout << "set a strategy" << std::endl;
  Context cont(&str_a);
  cont.exec();
  std::cout << "set b strategy" << std::endl;
  cont.setStrategy(&str_b);
  cont.exec();

  return 0;
}

```
output: 

```shell
set a strategy
StrategyA: exec()
set b strategy
StrategyB: exec()
```

# Observer Pattern
Observer pattern is used when there is one-to-many relationship between objects such as if one object is modified, its dependent objects are to be notified automatically.

![observer](https://github.com/yongcongwang/images/blob/master/blog/2019/test.png?raw=true)
```C++
// By yongcong.wang @ 09/06/2019
#include <iostream>
#include <vector>

class Observer {
 public:
  explicit Observer() {}
  virtual ~Observer() {}

  virtual void update() = 0;

 private:
  Observer(const Observer &rhs);
  Observer &operator=(const Observer &rhs);
};

class ConcreteObserverA : public Observer {
 public:
  explicit ConcreteObserverA() : Observer() {}
  virtual ~ConcreteObserverA() {}

  void update() {
    std::cout << "observer A heard" << std::endl;
  }

 private:
  ConcreteObserverA(const ConcreteObserverA &rhs);
  ConcreteObserverA &operator=(const ConcreteObserverA &rhs);
};

class ConcreteObserverB : public Observer {
 public:
  explicit ConcreteObserverB() : Observer() {}
  virtual ~ConcreteObserverB() {}

  void update() {
    std::cout << "observer B heard" << std::endl;
  }

 private:
  ConcreteObserverB(const ConcreteObserverB &rhs);
  ConcreteObserverB &operator=(const ConcreteObserverB &rhs);
};

class Subject {
 public:
  explicit Subject() {}
  virtual ~Subject() {}

  virtual void registerObserver(Observer *observer) = 0;
  virtual void removeObserver(Observer *observer) = 0;
  virtual void notifyObserver() = 0;

 private:
  Subject(const Subject &rhs);
  Subject &operator=(const Subject &rhs);
};

class ConcreteSubjectA : public Subject {
 public:
  explicit ConcreteSubjectA() : Subject() {}
  virtual ~ConcreteSubjectA() {}

  void registerObserver(Observer *observer) {
    observer_list_.push_back(observer);
  }

  void removeObserver(Observer *observer) {
    for (auto it = observer_list_.begin(); it != observer_list_.end(); ++it) {
      if (*it == observer) {
        observer_list_.erase(it);
        return;
      }
    }
  }

  void notifyObserver() {
    for (auto it = observer_list_.begin(); it != observer_list_.end(); ++it) {
      (*it)->update();
    }
  }

 private:
  ConcreteSubjectA(const ConcreteSubjectA &rhs);
  ConcreteSubjectA &operator=(const ConcreteSubjectA &rhs);

  std::vector<Observer *> observer_list_;
};

int main() {
  ConcreteObserverA obsr_a;
  ConcreteObserverB obsr_b;
  ConcreteSubjectA subj;
  std::cout << "add two observer and update" << std::endl;
  subj.registerObserver(&obsr_a);
  subj.registerObserver(&obsr_b);
  subj.notifyObserver();
  std::cout << "remove ovserver A and update" << std::endl;
  subj.removeObserver(&obsr_a);
  subj.notifyObserver();

  return 0;
}

```

output:

```shell
add two observer and update
observer A heard
observer B heard
remove ovserver A and update
observer B heard
```

# Decorator Pattern
Decorator pattern allows a user to add new functionality to an existing object without altering its structure. This type of design pattern comes under structural pattern as this pattern acts as a wrapper to existing class.
This pattern creates a decorator class which wraps the original class and provides additional functionality keeping class methods signature inact;

![decorator](https://github.com/yongcongwang/images/blob/master/blog/2019/decorator.png?raw=true)
```C++
// By yongcong.wang @ 28/07/2019
#include <iostream>
#include <string>
#include <memory>

class Component {
 public:
  explicit Component() {};
  virtual ~Component() {};
  Component(const Component &rhs) = delete;
  Component &operator=(const Component &rhs) = delete;

  virtual std::string methodA() = 0;
  virtual std::string methodB() = 0;

 private:
};

class ConcreteComponentA : public Component {
 public:
  ConcreteComponentA() : Component() {};
  ~ConcreteComponentA() {};
  ConcreteComponentA(const ConcreteComponentA &rhs) = delete;
  ConcreteComponentA &operator=(const ConcreteComponentA &rhs) = delete;

  std::string methodA() {
    return "ConcreteComponentA methodA ";
  };

  std::string methodB() {
    return "ConcreteComponentA methodB ";
  };

 private:
};

class Decorator : public Component {
 public:
  Decorator(std::shared_ptr<Component> component) : component_(component) {};
  ~Decorator() {};
  Decorator(const Decorator &rhs) = delete;
  Decorator &operator=(const Decorator &rhs) = delete;

  std::string methodA() {
    return component_->methodA();
  };

  std::string methodB() {
    return component_->methodB();
  };

 protected:
  std::shared_ptr<Component> component_;
};

class ConcreteDecoratorA : public Decorator {
 public:
  ConcreteDecoratorA(std::shared_ptr<Component> component) : Decorator(component) {};
  ~ConcreteDecoratorA() {};
  ConcreteDecoratorA(const ConcreteDecoratorA &rhs) = delete;
  ConcreteDecoratorA &operator=(const ConcreteDecoratorA &rhs) = delete;

  std::string methodA() {
    return component_->methodA() + "ConcreteDecoratorA methodA ";
  }
  std::string methodB() {
    return component_->methodB() + "ConcreteDecoratorB methodB ";
  }

 private:
};

class ConcreteDecoratorB : public Decorator {
 public:
  ConcreteDecoratorB(std::shared_ptr<Component> component) : Decorator(component) {};
  ~ConcreteDecoratorB() {};
  ConcreteDecoratorB(const ConcreteDecoratorB &rhs) = delete;
  ConcreteDecoratorB &operator=(const ConcreteDecoratorB &rhs) = delete;

  std::string methodA() {
    return component_->methodA() + "ConcreteDecoratorB methodA ";
  }
  std::string methodB() {
    return component_->methodB() + "ConcreteDecoratorB methodB ";
  }

 private:
};

int main() {
  std::shared_ptr<ConcreteComponentA> ptr_component_a = std::make_shared<ConcreteComponentA>();
  std::cout << ptr_component_a->methodA() << ", " << ptr_component_a->methodB() << std::endl;
  
  std::shared_ptr<ConcreteDecoratorA> ptr_decorator_a = std::make_shared<ConcreteDecoratorA>(
      ptr_component_a);
  std::cout << ptr_decorator_a->methodA() << ", " << ptr_decorator_a->methodB() << std::endl;

  std::shared_ptr<ConcreteDecoratorB> ptr_decorator_b = std::make_shared<ConcreteDecoratorB>(
      ptr_component_a);
  std::cout << ptr_decorator_b->methodA() << ", " << ptr_decorator_b->methodB() << std::endl;

  std::shared_ptr<ConcreteDecoratorB> ptr_decorator_a_b = std::make_shared<ConcreteDecoratorB>(
      ptr_decorator_a);
  std::cout << ptr_decorator_a_b->methodA() << ", " << ptr_decorator_a_b->methodB() << std::endl;

  return 0;
}
```

output:
```Shell
ConcreteComponentA methodA , ConcreteComponentA methodB 
ConcreteComponentA methodA ConcreteDecoratorA methodA , ConcreteComponentA methodB ConcreteDecoratorB methodB 
ConcreteComponentA methodA ConcreteDecoratorB methodA , ConcreteComponentA methodB ConcreteDecoratorB methodB 
ConcreteComponentA methodA ConcreteDecoratorA methodA ConcreteDecoratorB methodA , ConcreteComponentA methodB ConcreteDecoratorB methodB ConcreteDecoratorB methodB 
```

# Factory Pattern
The factory pattern is a creational pattern that uses factory methods to deal with the problem of creating objects without having to specify the exact calss of the object that will be created. This is done by creating objects by calling a factory method, either specified in an interface and implemented by child classes, or implemented in a base class and optionally overridden by derived classes rather than by calling a constructor.
According to the type of problems, there are three kinds of `Factory Pattern`:
- Simple Factory
- Normal Factory
- Abstract Factory

## Simple Factory
Simple Factory defines a method to create an object. It voilates the `Open/close Principle(OCP)`

![simple factory](https://github.com/yongcongwang/images/blob/master/blog/2019/simple_factory.png?raw=true)
```C++
// By yongcong.wang @ 30/07/2019
#include <iostream>
#include <string>
#include <memory>

class Product {
 public:
  explicit Product() {}
  virtual ~Product() {}
  Product(const Product &rhs) = delete;
  Product &operator=(const Product &rhs) = delete;

  virtual void operation() = 0;
};

class ConcreteProductA : public Product {
 public:
  explicit ConcreteProductA() : Product() {}
  ~ConcreteProductA() {}
  ConcreteProductA(const ConcreteProductA &rhs) = delete;
  ConcreteProductA &operator=(const ConcreteProductA &rhs) = delete;

  void operation() {
    std::cout << "ConcreteProductA called!" << std::endl;
  }
};

class ConcreteProductB : public Product {
 public:
  explicit ConcreteProductB() : Product() {}
  ~ConcreteProductB() {}
  ConcreteProductB(const ConcreteProductB &rhs) = delete;
  ConcreteProductB &operator=(const ConcreteProductB &rhs) = delete;

  void operation() {
    std::cout << "ConcreteProductB called!" << std::endl;
  }
};

class Factory {
 public:
  explicit Factory() {}
  ~Factory() {}
  Factory(const Factory &rhs) = delete;
  Factory &operator=(const Factory &rhs) = delete;

  std::shared_ptr<Product> createProduct(const std::string &product) {
    if (product == "ProductA") {
      return std::make_shared<ConcreteProductA>();
    }
    if (product == "ProductB") {
      return std::make_shared<ConcreteProductB>();
    }
  }

};

int main() {
  Factory factory;

  std::shared_ptr<Product> product_a = factory.createProduct("ProductA");
  std::shared_ptr<Product> product_b = factory.createProduct("ProductB");

  product_a->operation();
  product_b->operation();

  return 0;
}
```

output:
```Shell
ConcreteProductA called!
ConcreteProductB called!
```

## Normal Factory
Normal Factory not only encapsulates the creation of object but also put the creation of object into derived class. It only provides the method of creating objects, and the realization is in `ConcreteFactory`.
Disadvantage: the addition of factory object will cause the increasing of classes.
![normal facory](https://github.com/yongcongwang/images/blob/master/blog/2019/normal_factory.png?raw=true)

```C++
// By yongcong.wang @ 30/07/2019
#include <iostream>
#include <string>
#include <memory>

class Product {
 public:
  explicit Product() {}
  virtual ~Product() {}
  Product(const Product &rhs) = delete;
  Product &operator=(const Product &rhs) = delete;

  virtual void operation() = 0;
};

class ConcreteProductA : public Product {
 public:
  explicit ConcreteProductA() : Product() {}
  ~ConcreteProductA() {}
  ConcreteProductA(const ConcreteProductA &rhs) = delete;
  ConcreteProductA &operator=(const ConcreteProductA &rhs) = delete;

  void operation() {
    std::cout << "ConcreteProductA called!" << std::endl;
  }
};

class ConcreteProductB : public Product {
 public:
  explicit ConcreteProductB() : Product() {}
  ~ConcreteProductB() {}
  ConcreteProductB(const ConcreteProductB &rhs) = delete;
  ConcreteProductB &operator=(const ConcreteProductB &rhs) = delete;

  void operation() {
    std::cout << "ConcreteProductB called!" << std::endl;
  }
};

class Factory {
 public:
  explicit Factory() {}
  virtual ~Factory() {}
  Factory(const Factory &rhs) = delete;
  Factory &operator=(const Factory &rhs) = delete;

  virtual std::shared_ptr<Product> createProduct() = 0;
};

class ConcreteFactoryA : public Factory {
 public:
  explicit ConcreteFactoryA() : Factory() {}
  ~ConcreteFactoryA() {}
  ConcreteFactoryA(const ConcreteFactoryA &rhs) = delete;
  ConcreteFactoryA &operator=(const ConcreteFactoryA &rhs) = delete;

  std::shared_ptr<Product> createProduct() {
    return std::make_shared<ConcreteProductA>();
  }
};

class ConcreteFactoryB : public Factory {
 public:
  explicit ConcreteFactoryB() : Factory() {}
  ~ConcreteFactoryB() {}
  ConcreteFactoryB(const ConcreteFactoryB &rhs) = delete;
  ConcreteFactoryB &operator=(const ConcreteFactoryB &rhs) = delete;

  std::shared_ptr<Product> createProduct() {
    return std::make_shared<ConcreteProductB>();
  }
};

int main() {

  auto factory_a = std::make_shared<ConcreteFactoryA>();
  auto factory_b = std::make_shared<ConcreteFactoryB>();

  auto product_a = factory_a->createProduct();
  auto product_b = factory_b->createProduct();

  product_a->operation();
  product_b->operation();

  return 0;
}
```

output:
```Shell
ConcreteProductA called!
ConcreteProductB called!
```


## Abstract Factory
`Abstract Factory` improves the ablility of production of factory child, it provides methods for client. You can create multiple production objects via those methods.
![abstract factory](https://github.com/yongcongwang/images/blob/master/blog/2019/abstract_factory.png?raw=true)

# Singleton Pattern
