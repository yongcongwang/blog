---
title: Class Diagram
categories: software
tags:
  - diagram
mathjax: true
comments: true
date: 2020-07-08 10:32:18
---

In software engineering, a diagram in the UML(Unified Modeling Language) is a type of static structure diagram that describes the structure of a system by showing the system's classes, their attributes, operations(or methods), and the relationship among objects.
![diagram](https://github.com/yongcongwang/images/blob/master/blog/2020/diagram.png?raw=true)

<!-- more -->

# Visibility
To specify the visibility of a class member(i.e. attribute or method), these notations must be placed before the member's name:
- `+`: Public
- `-`: Private
- `#`: Protected
- `~`: Package

# Relationships
A relationship is a general term covering the specific types of logical connections found on class and object diagrams.
![diagram_relationship](https://github.com/yongcongwang/images/blob/master/blog/2020/diagram_relationship.png?raw=true)


## Instance-level Relationships

### Dependency
`Dependency` is the relationship of `... uses a ...` that indicates that one class depends on another because it uses it at some point in time. One class depends on another if the independent class is a
- parameter
- local variable

of a method of the dependent class.

### Association

### Aggregation
### Composition

## Class-level Relationships

### Generalization
### Realization
