---
title: Design Patterns software
mathjax: true
comments: true
categories:
  - coding
date: 2020-07-14 20:45:12
---

Design patterns are typical solutions to commonly occurring problems in software design. The are likely pre-made blueprints that you can customize to solve a recurring design problem in your code.

You can't just find a pattern and copy it into your problem, the way you can with off-the-shelf functions or libraries. The pattern is not a specific piece of code, but a general concept for solving a particular problem. You can follow the pattern details and implement a solution that suits the realities of your own problem.

<!-- more -->

# Benefits
Why should we spend time learning design patterns?
- Design patterns are a toolkit of `tried and tested solutions` to common problems in software design. Even if you never encounter those problems, knowing patterns is still useful because it teaches you how to solve all sorts of problems using principles of object-oriented design.
- Design patterns define a common language that you and your teammates can use to communicate more efficiently. You can say "just use a Singleton for that", and everyone will understand the idea behind your suggestion. No need to explain what a singleton is if you know the pattern and its name.

# Classification of Patterns
Design patterns differ by their complexity, level of detail and scale of applicability to the entire system being designed. 

The most basic and low-level patterns are often called `idioms`. They usually apply only to a single programming language.

The most universal and high-level patterns are architectural patterns. Developers can implement these patterns in virtually any language. Unlike other patterns, they can be used to design the architecture of an entire application.

In addition, all patterns can be categorized by their `intent`, we cover three main groups of patterns:
- `Creational patterns`, provide object creation mechanisms that increase flexibility and reuse of existing code.
- `Structural patterns`, explain how to assemble objects and classes into large structures, while keeping the structures flexible and efficient.
- `Behavioral patterns`, take care of effective communication and the assignment of responsibilities between objects.

# Creatinal Pattern
Creational patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

## Factory Method
`Factory Method` is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclass to alter the type of objects that will be created.

### Problem
Imagine you're creating a logistic management application. The first version of your app can only handle transportation by trucks, so the bulk of your code lives inside the `Truck` class. And you may have the process:
```
Receive Order -> Arrange Time -> Transportation
```

After a while, your app becomes pretty popular. Now you can also receive requests from sea transportation, you have to add the `Ship` class to your app. 

But at present most of your code is coupled to the `Truck` class. Adding `Ship` into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

### Structure
![factory](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/factory.png?raw=true)

### Advantage
- You avoid tight coupling between the creator and the concrete products.
- `Single Responsiblity Principle`. You can move the product creation code into one place in the program, making the code easier to support.
- `Open/Close Principle`. You can introduce new types of products into the program without breaking existing client code.

### Disadvantage
- The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you're introducing the pattern into an existing hierarchy of creator classes.

## Abstract Factory
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

### Problem
Imagine you're creating a furniture shop. Your code consists of classes that represents:
1. A family of related products: `Chair` + `Sofa` + `CoffeeTable`.
2. Several variants of this family. For example, products `Chair` + `Sofa` + `CoffeeTable` are available in these variant: `Modern` + `Victorian` + `ArtDeco`.

You need a way to create individual furniture objects so that they match other objects of the same family.
Also, you don't want to change existing code when adding new products or families of products to the program. Furniture vendors update their catalogs often, and you wouldn't want to change the core code each time it happens.

### Architecture
![abstract_factory](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/abstract_factory.png?raw=true)

### Advantage
- You can be sure that the products you're getting from a factory are compatible with each other.
- You avoid tight coupling between the creator and the concrete products.
- `Single Responsiblity Principle`. You can move the product creation code into one place in the program, making the code easier to support.
- `Open/Close Principle`. You can introduce new types of products into the program without breaking existing client code.

### Disadvantage
- The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you're introducing the pattern into an existing hierarchy of creator classes.

## Builder
Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction.

### Problem
Imagine a complex object that requires laborous, step-by-step initialization of many fields and nested objects. Such initialization code is usually buried inside a monstrous constructor with lots of parameters. Or even worse: scattered all over the client code.

For example, you have a class `House`. To build a simple house you need to construct four walls and a floor, install a door, fit a pair of windows and build a proof. But what if you want a bigger, brighter house with a backyard and other goodies?

The simplest way is to extend the base class `House` and create a set of subclasses to cover all combinations of the parameters. But enventually you'll end up with a considerable number of subclasses.

Another approach that doesn't involve breeding subclasses. You can create a giant constructor right in the base `House` with all possible parameters that control the house object. The problem of this approach is that in most cases most of the parameters will be unused, making the constructor calls pretty ugly.

### Structure
![builder](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/builder.png?raw=true)

### Advantage
- You can construct objects step-by-step, defer construction steps or run steps recursively.
- You can reuse the same construction code when building various representations of products.
- `Single Responsibility Principle`. You can isolate complex construction code from the business logic of the product.

### Disadvantage
- The overall complexity of the code increases since the pattern requires creating multiple new classes.

## Prototype
Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

### Problem
Say you have an object, and you want to create an exact copy of it. How would you do it? First, you have to create a new object of the same class. Then you have to go through all the fields of the original object and copy their values over to the new object.
But problem occurs:
- Not all objects can be copied that way because some of the object's fields may be private and not visible from outside of the objects itself.
- You have to know the object's class to create a duplicate, your code becomes dependent on that class.

### Structure
![prototype](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/prototype.png?raw=true)

### Advantage
- You can clone objects without coupling to their concrete classes.
- You can get rid of repeated initialization code in favor of cloning pre-built prototypes.
- You can produce complex objects more conveniently.
- You get an alternative to inheritance when dealing with configuration presets for complex objects.

### Disadvantage
- Cloning complex objects that have circular references might be very tricky.

## Singleton
Signleton is a creational design pattern that lets you ensure a class has only one instance, while providing a global access point to this instance.

### Problem
The Singleton pattern solves two problems at the same time, violating the `Single Responsibility Principle`:
- Ensure that a class has just a single instance.
- Provide a global access point to that instance.

### Structure
![singleton](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/singleton.png?raw=true)

### Advantage
- You can be sure that a class has only a single instance.
- You gain a global access point to that instance.
- The singleton object is initialized only when it's requested for the first time.

### Disadvantage
- Violates the `Single Responsibility Principle`. The pattern solves two problems at the time.
- The Singleton pattern can mask bad design, for instance, when components of the program know too much about each other.
- The pattern requires special treatment in a multithreaded environment so that multiple threads won't create a singleton object several times.
- It may be difficult to unit test the client code of the Singleton because many test frameworks rely on inheritance when producing mock objects. Since the constructor of the singleton class is private and override static methods is impossible in most languages, you will need to think of a creative way to mock the singleton. Or just don't write the tests. Or don't use the Singleton pattern.

# Structural Pattern
Structural patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

## Adapter
Adapter allows objects with incompatible interfaces to collaborate.

### Problem
Imagine you're creating a stock market monitoring app. The app downloads the stock data from multiple sources in `xml` format and then displays nice-looking charts and diagrams for the user.
At some point, you decide to improve the app by integrating a smart 3rd-party analytics library. But there's a catch: the analytics library only works with data in `json` format.
You could change the library to work with `xml`. However, this might break some existing code that relies on the library. And worse, you might not have access to the library's source code in the first place, making this approach impossible.

### Strucure
![adapter](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/adapter.png?raw=true)

### Advantage
- `Single Responsibility Principle`.
- `Open/Close Principle`.

### Disadvantage
- The overall complexity of the code increases becuase you need to introduce a set of new interfaces and classes. Sometimes it's simpler just to change the service class so that it matches the rest of your code.

## Bridge
Bridge lets you split a large class or a set of closely related classes into two separate hierarchies: abstraction and implementation, which can be developed independently of each other.

### Problem
Say you have a geometric `Shape` class with a pair of subclasses: 
- `Circle`;
- `Square`.
You want to extend this class hierarchy to incorporate colors, so you plan to create `Red` and `Blue` shape subclasses. However, since you already have two subclasses, you'll need to create four classes combinations such as `BlueCircle` and `RedSquare`.
![shape](https://refactoring.guru/images/patterns/diagrams/bridge/problem-en.png)
Adding new shape types and colors to the hierarchy will grow it exponentially.

### Structure
![bridge](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/bridge.png?raw=true)

### Advantage
- You can create platform-independent classes and apps.
- The client code works with high-level abstractions. It isn't exposed to the platform details.
- `Open/Close Principle`.
- `Single Responsibility Principle`.

### Disadvantage
- You might make the code more complicated by applying the pattern to a highly cohesive class.

## Composite
Composite lets you compose objects into tree structures and then work with these structures as if they were individual objects.

### Problem
Using the Composite pattern makes sense only when the core model of your app can be represented as a tree.
For example, imagine that you have two types of objects: `Products` and `Boxes`. A `Box` can contain several `Products` as well as a number of smaller `Boxes`. The little `Boxes` can also hold some `Products` or even smaller `Boxes`, and so on.

Say you want to travel all over the `Products`, you could try direct approach: unwrap all the boxes and then calculate the total, but it's not a simple problem.
![boxes](https://refactoring.guru/images/patterns/diagrams/composite/problem-en.png)

### Structure
![composite](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/composite.png?raw=true)

### Advantage
- You can work with complex tree structures more conveniently: use polymorphism and recursion to your advantage.
- `Open/Close Principle`.

### Disadvantage
- It might be difficult to provide a common interface for classes whose functionality differs too much. In certain scenarios, you'd need to overgeneralize the component interface, making it harder to comprehend.

## Decrator(Wrapper)
Decorator lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behavior.

### Problem
Imagine you have a class `Notifier` and it can send message via emails. But latter another client class which uses this class is supposed to send messages in other ways, for example, sms message or slack message.
You can extend the `Notifier` and add `sms` and `slack` methods, but what if we just want `email` and `slack`? What if we want some more methods?
You have to find some other way to structure notifications classes so that their number won't accidentally break some Guinness record.

### Structure
![decorator](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/decorator.png?raw=true)

### Advantage
- You can extand an object's behavior without making a new subclass.
- You can add or remove resonsibilities from an object at runtime.
- You can combine several behaviors by wrapping an object into multiple decorates.
- `Single Responsibility Principle`.

### Disadvantage
- It's hard to remove a specific wrapper from the wrapper stack.
- It's hard to implement a decorator in such a way that its behavior doesn't depend on the order in the decorators stack.
- The initial configuration code of layers might look pretty ugly.

## Facade

## Flyweight

## Proxy

# Behavioral Pattern

## Chain of Responsibility

## Command

## Iterator

## Mediator

## Memento

## Observer

## State

## Strategy

## Template Method

## Visitor

# Reference
- [Design Patterns](https://refactoring.guru/design-patterns)
