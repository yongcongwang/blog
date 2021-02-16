---
title: Effective Modern Cpp
mathjax: true
date: 2021-02-16 20:16:10
---
This is a summary of the book "Effective Modern C++" which gives 42 specific ways to imporve your programs and designs by Scott Meyers.

<!-- more -->

# 1. Understand template type deduction.
- During template type deduction, arguments that are references are treated as non-reference, i.e., their reference-ness is ignored.
- When deducing types for universal reference parameters, lvalue arguments get special treatment.
- when deducing types for by-value parameters, `const` and/or `volatile` arguments are treated as non-const and non-volatile.
- During template type deduction, arguments that are array or function names decay to pointers, unless they're used to initialize references.

# 2. Understand auto type deduction.
- `auto` type deduction is usually the same as template type deduction, buy `auto` type deduction assumes that a braced initializer represents a `std::initializer_list`, and template type deduction doesn't.
- `auto` in a function return type or a lambda parameter implies template type deduction, not auto type deduction.

# 3. Understand `decltype`.
- `decltype` almost always yields the type of a variable or expression without any modifications.
- For lvalue expressions of type T other than names, decltype always reports a type of `T&`.
- C++14 supports `decltype(auto)`, which, like auto, deduces a type from its initializer, but it performs the type deduction using the `decltype` rules.

# 4. Know how to view deduced types.
- Deduced types can often be seen using:
 - IDE editors,
 - compiler error messages,
 - Boost TypeIndex library.
- The results of some tools may be neither helpful nor accurate, so an understanding of C++'s type deduction rules remains essential.

# 5. Prefer `auto` to explicit type declarations.
- The advances are:
 - `auto` variables must be initialized,
 - immune to type mismatches that can lead to portability or efficiency problems,
 - can ease the process of refactoring,
 - require less typing than variables with explicitly specified types.
- `auto`-typed variables are subject to the pitfalls described in iterm 2 and 6.

# 6. Use the explicitly typed initializer idiom when auto deduces undesired types.
- "Invisible" proxy types can cause auto to deduce the "wrong" type for an initializing expression.
- The explicitly typed initializer idiom forces auto to deduce the type you want it to have.

# 7. Distinguish between `()` and `{}` when creating objects.
- Braced initialization is the most widely usable initialization syntax, it prevents narrowing conversions, and it's immune to C++'s most vexing parse.
- During constructor overload resolution, braced initializers are matched to `std::initializer_list` parameters if at all possible, even if other constructors offer seemingly better matches.
- An example of where the choice between parentheses and braces can make a significant difference is creating a `std::vector<numeric type>` with two arguments.
- Choosing between parentheses and braces for object creation inside templates can be challenging.

# 8. Prefer `nullptr` to `0` and `NULL`.
- Avoid overloading on integral and pointer types.

# 9. Prefer alias declarations to typedefs.
- `typedef`s don't support templatization, but alias declarations do.
- Alias templates avoid the `::type` suffix and, in templatess, the "typename" prefix often required to refer to  typedefs.
- C++14 offers alias templates for all the C++11 type traits transformations.

# 10. Prefer `scoped enums` to `unscoped enums`.
- C++98-style `enum`s are now known as unscoped enums.
- Enumerators of scoped enums are visible only within the enum. They convert to other types only with a cast.
- Both scoped and unscoped enums support specification of the underlying type. The default underlying type for scoped enums is int. Unscoped enums have no default underlying type.
- Scoped enums may always be forward-declared. Unscoped enums may be forward-declared only if their declaraation specifies an underlying type.

# 11. Prefer deleted functions to private underfined ones.
- Any function may be deleted, including non-member functions and template instantiations.

# 12. Declare overriding functions `override`.
- Declare overriding functions `override`.
- Member function reference qualifiers make it possible to treat lvalue and rvalue objects(`*this`) diffrently.

# 13. Prefer `const_iterator`s to `iterator`s.
- In maximally generic code, prefer non-member versions of begin, end, rbegin, etc, over their member function counterparts.

# 14. Declare functions `noexcept` if they won't emit exceptions.
- `noexcept` is part of a function's interface, and that means that callers may depend on it.
- `noexcept` functions are more optimizable than non-noexcept functions.
- `noexcept` is particularly valuable for the move operations, swap, memory deallocation functions and destructions.
- Most functions are exception-neutral rather than `noexcept`.

# 15. Use `constexpr` whenever possible.
- `constexpr` objects are `const` and are initialized with valuess known during compilation.
- `constexpr` functions can produce compile-time results when called with arguments whose values are known during compilation.
- `constexpr` objects and functions may be used in a wider range of contexts than non-constexpr objects and functions.
- `constexpr` is part of an object's or function's interface.

# 16. Make `const` member functions thread safe.
- Make `const` member functionsthreadsafe unless you're certain they'll never be used in a concurrent context.
- Use of `std::atomic` variables may offer better performance than a mutex, but they're suited for manipulation of only a single variable or memory location.

# 17. Understand special member function generation.
- The special member functions are those compilers may generate on their own:
 - default constructor,
 - destructor,
 - copy constructor,
 - copy operator,
 - move constructor,
 - move operator
- Move operations are generated only for classes lacking explicitly declared move operations, copy operations and a destructor.
- The copy operations are generated only for classes lacking an explicitly declared copy operations, and it's deleted if a move operation is declared.
- Member function templates never suppress generation of special member functions.

# 18. Use `std::unique_ptr` for exclusive-ownership resource management.
- `std::unique_ptr` is a small, fast, move-only smart pointer for managing resources with exclusive-ownership semantics.
- By default, resource destruction takes place via `delete`, but custom deleters can be specified. Stateful deleters and function pointers as deleters increase the size of `std::unique_ptr` objects.
- Converting a `std::unique_ptr` to a `std::shared_ptr` is easy.

# 19. use `std::shared_ptr` for shared-ownership resource management.
- `std::shared_ptr`s offer convenience approaching that of garbage collection for the shared lifetime management of arbitrary resources.
- Compared to `std::unique_ptr`, `std::shared_ptr` objects are typically twice as big, incur overhead for control blocks, and require atomic reference count manipulations.
- Default resource destruction is via `delete`, but custom deleters are supported. The type of the deleter has no effect on the type of the `std::shared_ptr`.
- Avoid creating `std::shared_ptr`s from viariable of raw pointer type.

# 20. Use `std::weak_ptr` for `std::shared_ptr`-like pointers that can dangle.
- Use `std::weak_ptr` for `std::shared_ptr`-like pointers that can dangle.
- Potential use cases for `std::weak_ptr` includes caching, observer lists, and the prevention of `std::shared_ptr` cycles.

# Prefer `std::make_unique` and `std::make_shared` to direct use of `new`.

