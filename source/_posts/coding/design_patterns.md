---
title: Design Patterns
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

### Structure
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
Facade provides a simplified interface to a library, a framework, or any other complex set of classes.

### Problem
Image that you must make your code with a broad set of objects that belong to a sophisticated library of framework. Ordinarily, you'd need to initialize all of those objects, keep track of dependencies, execute methods in the correct order, and so on.

As a result, the business logic of your classes would become tightly coupled to the implementation details of 3rd-party classes, making it hard to comprehend and maintain.

### Structure
![facade](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/facade.png?raw=true)

### Advantage
- You can isolate your code from the complexity of a subsystem.

### Disadvantage
- A facade can become a god object coupled to all classes of an app.

## Flyweight
Flyweight lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each objects.

### Problem
Say you decide to create a simple video game: players would be moving around a map and shooting each other. You choose to implement a realistic particle system, and make it a distinctive feature of the game.
After its completion, you discovered the game uses too much RAM. The problem was related to your particle system. Each particle, such as a bullet, a missile or a piece of sharapnel was represented by a separate object containing plenty of data. At some point, when the carnage on a player's screen reached its climax, newly created particles no longer fit into the remaining RAM, so the program crashed.

### Structure
![flyweight](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/flyweight.png?raw=true)

### Advantage
- You can save lots of RAM, assuming your program has tons of similar objects.

### Disadvantage
- You might be trading RAM over CPU cycles when some of the context data needs to be recalculated each time somebody calls a flyweight method.
- The code becomes more complicated. New team members will always be wondering why the state of an entity was separated in such a way.

## Proxy
Proxy lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

### Problem
Why would you want to control access to an object? Here is an example: you have a massive object that consumes a vast amount of system resources. You need it from time to time, but not always.

You would implement lazy initialization: create this object only when it's actually needed. All of the object's clients would need to execute some deferred initialization code. Unfortunately, this would probably cause a lot of code duplication.

In an ideal world, we'd want to put this code directly into our object's class, but that isn't always possible. For instance, the class may be part of a closed 3rd-party library.

### Structure
![proxy](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/proxy.png?raw=true)

### Advantage
- You can control the service object without clients knowing about it.
- You can manage the lifecycle of the service object when clients don't care about it.
- The proxy works even if the service object isn't ready or is not available.
- `Open/Close Principle`.

### Disadvantage
- The code may become more complicated since you need to introduce a lot of new classes.
- The response from the service might get delayed.

# Behavioral Pattern

## Chain of Responsibility
Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

### Structure
![chain](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/chain.png?raw=true)

### Advantage
- You can control the order of request handling.
- `Single Responsibility Principle`.
- `Open/Close Principle`.

### Disadvantage
- Some requets may end up unhandled.

## Command
Command turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests. This transformation lets you parameterize methods with different requests, delay or queue a request's execution, and support undoable operation.

### Problem
Imagine you're working on a new text-editor app. Your current task is to create a toolbar with a bunch of buttons for various operations of the editor. You created a very neat `Button` class that can be used for buttons on the toolbar, as well as for generic buttons in varous dialogs.

While all of these buttons look similar, they're all supposed to do different things. Where would you put the code for the various click handlers of these buttons? The simplest solution is to create tons of subclasses for each place where the button is used. These subclasses would contain the code that would have to be executed on a button click.

Before long, you realize that this approach is deeply flawed:
- You have an enormous number of subclasses, and that would be okey if you weren't risking breaking the code in these subclasses each time you modify the base `Button` class.
- And here's the ugliest part. Some operations, such as copying/pasting test, would need to be invoked from multiple places.
- Initially, when your app only had toolbar, it was okay to place the implementation of various operations into the button subclasses. But when you implementation context menus, shortcuts, and other stuff, you have to either duplicate the operation's code in many classes or make menus dependent on buttons, which is an even worse option.

### Structure
![command](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/command.png?raw=true)

### Advantage
- `Single Responsibility Principle`.
- `Open/Close Principle`.
- You can implement undo/redo.
- You can implement deferred execution of operation.
- You can assemble a set of simple commands into a complex one.

### Disadvantage
- The code may become more complicated since you're introducing a whole new layer between senders and receivers.

## Iterator
Iterator lets you traverse elements of a collection without exposing its underlying representation(list, stack, tree, etc.).

### Problem
Collections are one of most used data types in programming. Nonetheless, a collection is just a container for a group of objects.
Most collections store their elements in simple lists. However, some of them are based on stacks, trees, graphs and other complex data structures.
But no matter how a collection is structued, it must provide some way of accessing its elements so that other code can use these elements. There should be a way to go through each elements.
It may be easy to traverse on a list. But when you have to traverse elements of a complex data structure(like a tree), things get tricky.

### Structure
![iterator](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/iterator.png?raw=true)

### Advantage
- `Single Responsibility Principle`.
- `Open/Close Principle`.
- You can iterate over the same collection in parallel because each iterator object contains its own iteration state.
- For the same reason, you can delay an iteration and continue it when needed.

### Disadvantage
- Applying the pattern can be overkill if your app only works with simple collections.
- Using an iterator may be less efficient than going through elements of some specialized collections directly.

## Mediator
Mediator lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

### Problem
Say you have a dialog for creating and editing customer profiles. It consists of various form controls such as text fields, checkboxes, buttons, etc.

Some of the form elements may interact with others. For instance, selecting "I have a dog" checkbox may reveal a hidden text field for entering the dog's name. Another example is the submit button that has to validate values of all fields before saving the data.

By having this logic implemented directly inside the code of the form elements you make these elements' classes much harder to reuse in other forms of the app. For example, you won't be able to use that checkbox class inside another form, because it's coupled to the dog's text field. You can use either all the classes involved in rendering the profile form, or none at all.

### Structure
![mediator](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/mediator.png?raw=true)

### Advantage
- `Single Responsibility Principle`.
- `Open/Close Principle`.
- You can reduce coupling between various components of a program.
- You can reuse individual components more easily.

### Disadvantage
- Over time a mediator can evolve into a `God Object`.

## Memento
Memento lets you save and restore the previous state of an object without revealing the detail of its implementation.

### Problem
Imagine you're creating a text editor app. In addition to simple text editing, your editor can format text, insert inline images, etc.

At some point you decide to let users undo any operations carried out on the text. This feature has become so common over the years that nowadays people expect app to have it. For the implementation, you chose to take the direct approach, before performing any operation, the app records the state of all objects and save it in some storage.
But the tricky case appears:
- You need to go over all the fields in an objetct and copy their values into storage. However, this would only work if the object had quite relaxed access restrictions to its contents. You can not access the private params.
- If you want to refactor some of the editor classes, the copying class should also change.
- You store the params in a list of a class, then you should make its fields public. Other classes would become dependent on every little change to the snapshot class.

### Structure
![memento](https://github.com/yongcongwang/images/blob/master/blog/2020/design_pattern/memento.png?raw=true)

### Advantage
- You can reduce snapshots of the object's state without violating its encapsulation.
- You can simplify the originator's code by letting the caretaker maintain the history of the originator's state.

### Disadvantage
- The app might consume lots of RAM if clients create mementos too often.
- Catetaker's should track the originator's lifecycle to be able to destroy obsolete mementos.
- Most dynamic programming languages, such as PHP, Python, and JavaScript, can't guarantee that the state within the memento stays untouched.

## Observer
Observer lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing. 

### Problems
Imagine you have two types of objects: a `Customer` and a `Store`. The customer is very interested in a particular brand of product which should become available in the store very soon.

The customer could visit the store every day and check product availability. But while the product is still en route, most of these trips would be pointless.

On the other hand, the store could send tons of emails to all customers each time a new product becomes available. This would save some customers from endless trips to the store. At the same time, it'd upset other customers who aren't interested in new products.

### Structure
![observer](https://github.com/yongcongwang/images/blob/master/blog/2020/design_patter/observer.png?raw=true)

### Advantage
- `Open/Close Principle`.
- You can establish relations between objects at run time.

### Disadvantage
- Subscribers are notified in random order.

## State

## Strategy

## Template Method

## Visitor

# Reference
- [Design Patterns](https://refactoring.guru/design-patterns)
