---
title: Effective Cpp
mathjax: true
date: 2021-02-15 22:39:15
---

This is a summary of the book "Effective C++" which gives 55 specific ways to imporve your programs and designs by Scott Meyers.

<!-- more -->

# View C++ as a federation of languages.
- Rules for effective C++ programming vary, depending on the part of C++ you are using.

# Prefer consts, enums, and inlines to #defines.
- For simple constants, prefer const objects or enums to `#define`s.
- For function-like macros, prefer inline functions to `#define`s.

# Use `const` whenever possible. 
- Declaring something const help compilers detect usage errors. const can be applied to objects at any scope, to function parameters and return types, and to member functions as a whole.
- Compilers enforce bitwise constness, but you should program using logical constness.
- When const and non-const member functions have essentially identical implementations, code duplication can be avoided by having the non-const version call the const version.

# Make sure that the objects are initialized before they're used.
- Manually initialize objects of built-in type, because C++ only sometimes initializes them itself.
- In a constructor, prefer use of the member initialization list to assignment inside the body of the constructor. List data members in the initialization list in the same order they're declared in the class.
- Avoid initialization order problems across translation units by replacing non-local static objects with local static objects.
