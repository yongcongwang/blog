---
title: Design Patterns
categories: software
tags:
  - coding
  - design pattern
mathjax: true
comments: true
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

## Creatinal Pattern
Creational patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

### Factory Method
`Factory Method` is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclass to alter the type of objects that will be created.

#### Problem
Imagine you're creating a logistic management application. The first version of your app can only handle transportation by trucks, so the bulk of your code lives inside the `Truck` class. And you may have the process:
```
Receive Order -> Arrange Time -> Transportation
```

After a while, your app becomes pretty popular. Now you can also receive requests from sea transportation, you have to add the `Ship` class to your app. 

But at present most of your code is coupled to the `Truck` class. Adding `Ship` into the app would require making changes to the entire codebase. Moreover, if later you decide to add another type of transportation to the app, you will probably need to make all of these changes again.

#### Structure
![factory](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/factory.png?raw=true)

#### Advantage
- You avoid tight coupling between the creator and the concrete products.
- `Single Responsiblity Principle`. You can move the product creation code into one place in the program, making the code easier to support.
- `Open/Close Principle`. You can introduce new types of products into the program without breaking existing client code.

#### Disadvantage
- The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you're introducing the pattern into an existing hierarchy of creator classes.

### Abstract Factory
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

#### Problem
Imagine you're creating a furniture shop. Your code consists of classes that represents:
1. A family of related products: `Chair` + `Sofa` + `CoffeeTable`.
2. Several variants of this family. For example, products `Chair` + `Sofa` + `CoffeeTable` are available in these variant: `Modern` + `Victorian` + `ArtDeco`.

You need a way to create individual furniture objects so that they match other objects of the same family.
Also, you don't want to change existing code when adding new products or families of products to the program. Furniture vendors update their catalogs often, and you wouldn't want to change the core code each time it happens.

#### Architecture
![abstract_factory](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/abstract_factory.png?raw=true)

#### Advantage
- You can be sure that the products you're getting from a factory are compatible with each other.
- You avoid tight coupling between the creator and the concrete products.
- `Single Responsiblity Principle`. You can move the product creation code into one place in the program, making the code easier to support.
- `Open/Close Principle`. You can introduce new types of products into the program without breaking existing client code.

#### Disadvantage
- The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you're introducing the pattern into an existing hierarchy of creator classes.

### Builder

### Prototype

### Singleton

## Structural Pattern

### Adapter

### Bridge

### Composite

### Decrator

### Facade

### Flyweight

### Proxy

## Behavioral Pattern

### Chain of Responsibility

### Command

### Iterator

### Mediator

### Memento

### Observer

### State

### Strategy

### Template Method

### Visitor