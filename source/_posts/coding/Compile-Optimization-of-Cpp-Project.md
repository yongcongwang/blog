---
title: Compile Optimization of Cpp Project
mathjax: true
date: 2021-01-28 13:42:57
---

<!-- more -->

# Compilation Process

In general, the compilation of a C++ program involves these four steps:
1. Preprocessing
2. Compiling
3. Assembling
4. Linking

![factory](/images/2021/compile_optimization/compile_process.png)

## Preprocessing
Preprocessor directives are one of the unique feature of C++. Before a C++ program gets compiled by the compiler, the source code gets preprocessed by the preprocessor. 
> All preprocessor directives in C++ begin with `#`, and they do not need to end with a semicolon(`;`) because this is not a statement in C++.

There are different preprocessor directives that perform different tasks.
- Inclusion Directives:
  - `#include`: specifies the files to be included, especially header-file
- Macro Definition Directive:
 - `#define`: define a macro substitution
 - `#undef`: undefine a macro
- Conditional Compilation Directive:
 - `#if`: test a condition
 - `#elif`: else if condition
 - `#endif`: end of `#if`
 - `#ifdef`: used to test for macro definition
 - `#ifndef`: used to test for whether a macro is not defined
 - `#else`: it provides an alternative option when `#if` fails
- Other directives:
 - `#error`
 - `#line`: Supplies a line number for compiler message
 - `#pragma`: Supplies implementation-defined instructions to the compiler

Some macros C++ predefined are:
- `__LINE__`: this contians the current line number of the program when it is being compiled
- `__FILE__`: this contians the current file name of the program when it is being compiled
- `__DATE__`: this contians the string of the form `month/day/year` that is the date of the translation of the source code into object code
- `__TIME__`: this contians the string of the form `hour:minute:second` that is the time at which the program was compiled

The processor obeys directives defined in file to:
- replacing macros
- expanding include files
- expanding conditinal code
- removing comments

You can use `g++ -E` to get preprocessed file with the extension `.i` or `.ii`.

## Compiling
Compiling is the second step. It takes the output of the preprocessor and generates assembly language, an intermediate human readable language, specific to the target processor. The compiler parses the pure C++ source code (now without any preprocessor directives) and converts it into assembly code.
Compilers usually let you stop compilation at this point. This is very useful because with it you can compile each source code file separately. The advantage this provides is that you don’t need to recompile everything if you only change a single file.
It's at this stage that "regular" compiler errors, like syntax errors or failed overload resolution errors are reported.

You can use `g++ -S` to get compiled file with the extension `.s`.

## Assembling
After compiling, we get the assembly code. Then the assembler will translate the assembly code into machine code producing actual binary file in some format(ELF, COFF, a.out, etc.). This object file contains the compiled code(in binary form) of the symbols defined in the input. Symbols in the object files are referred to by name.

Object files can refer to symbols that are not defined. This is the case when you use a declaration, and don't provide a definition for it. The compiler doesn't mind this and will happily produce the object file as long as the source code is well-formed.

You can use `g++ -c` to get assembled file with the extension `.o`.

## Linking
The linker is what produces the final compilation output from the `object file` that compiler generated. The output of linker can be:
- shared library: it doesn't add the library code to the output, so it has the smallest file size;
- static library: it add all the library code to the output, which makes its larger size;
- executable file: it combine all the binary file to an executable, and has the largest file size.

While linking, the linker links all the boject files by replacing the references to undefined symbols with the correct addresses. Each of these symbols can be defined in other object files or in libraries. If they are defined in libraries other than the standard library, you need to tell the linker the path of them.

At this stage the most common erros are:
- missing definitions, which means that either the definitions don't exist or the object files or libraries they reside were not given to the linker
- duplicate definitions, which means that the same symbol was defined in two different object files or libraries

# Optimization Methods and Results

| compile step | preprocessing | compiling | assembling | linking | total |
|---|---|---|---|---|---|
| time(s) | 0.337 | 54.403 | 3.741 | 8.272 | 66.416 |

## Compile what we used
In prediction module, we have three parts of code:
- onboard: which runs on our computing platform and supports for auto-driving system;
- offboard: which contains tools and deep-learning model trainers and runs on our develop PC;
- unittest: which is the unit-test case of above parts.

In our previous work we compile all of three parts with a bash script.
The file tree is like this:
```
.
├── build
├── cmake
├── CMakeLists.txt
├── docs
├── offboard
├── onboard
└── unit_test
```
And we use the script to build them all:
```bash
#!/bin/bash
cmake -DCMAKE_INSTALL_PREFIX=$INSTALL_DIR -DCMAKE_BUILD_TYPE=Debug \
      -Bbuild -H.
make -C build -j12 install
```

But when we develop new features or fix bugs, what we want is to varify our code quickly, it's no need to build offboard or unit_test code.

Now we split the code into three parts and just compile the part we interested. The file tree is like this:
```
.
├── build
├── build.sh
├── cmake
├── CMakeLists.txt
├── docs
├── Doxyfile
├── offboard
│   ├── CMakeLists.txt
│   └── model_training
├── onboard
│   ├── CMakeLists.txt
│   └── proto
└── unit_test
    ├── CMakeLists.txt
    └── onboard
```
At the top level of repo, we use three flags to define which part of code we want to compile in `CMakeLists.txt`:
```cmake
# Build options
set(BUILD_ONBOARD OFF CACHE BOOL "build_onboard")
set(BUILD_OFFBOARD OFF CACHE BOOL "build_offboard")
set(BUILD_UNIT_TEST OFF CACHE BOOL "build_unit_test")

if(${BUILD_ONBOARD})
  add_subdirectory(onboard)
endif(${BUILD_ONBOARD})

if(${BUILD_OFFBOARD})
  add_subdirectory(offboard)
endif(${BUILD_OFFBOARD})

if(${BUILD_UNIT_TEST})
  add_subdirectory(unit_test)
endif(${BUILD_UNIT_TEST})
```
In bash script file, we choose what we want to build:
```bash
function build_onboard(){
  set +e
  mkdir build
  set -e
  cmake -DCMAKE_INSTALL_PREFIX=$INSTALL_DIR -DCMAKE_BUILD_TYPE=Debug \
        -DBUILD_ONBOARD=ON -DBUILD_OFFBOARD=OFF -DBUILD_UNIT_TEST=OFF \
        -Bbuild -H.
  make -C build -j12 install  || {
    echo "$R -> Build failed! $E"
    exit 1
  }
  echo -e "$G -> Build onboard successfully! $TAIL $E"
  return $?
}
```

### Result
| | Before optimization | After optimization |
|---|---|---|
| time(s) | 81 | 66 |

## Compiler options
A compiler is a special program that processes statements written in a particular programming language and turns them into machine language or "code" that a computer's processor uses.
In linux platform, we use GCC to compile our code. When you invoke GCC, it normally does preprocessing, compilation, assembly and linking.

### Parallel compilation
In Linux platform we use `GNU/Make` tool to compile code. When we execute make command, we should use the `-j` option to define parallel jobs. In the bash script we use `$(nporc)` to get the number of cpu core as the `-j` parameter and increase the compilation performance.
```bash
make -C build -j$(nproc) install
```

#### Result
| | Before optimization(`j8`) | After optimization(`j12`) |
|---|---|---|
| time(s) | 70 | 66 |

### Optimize options
These options control various sorts of optimizations.
Without any optimization option, the compiler’s goal is to reduce the cost of compilation and to make debugging produce the expected results.
Turning on optimization flags makes the compiler attempt to improve the performance and/or code size at the expense of compilation time and possibly the ability to debug the program.

Here are some option levels:
- `-O/-O1`: Optimizing compilation takes somewhat more time, and a lot more memory for a large function.With `-O`, the compiler tries to reduce code size and execution time, without performing any optimizations that take a great deal of compilation time.
- `-O2`: Optimize even more. GCC performs nearly all supported optimizations that do not involve a space-speed tradeoff. As compared to -O, this option increases both compilation time and the performance of the generated code.

- `-O3`: Optimize yet more.
- `-O0`: Reduce compilation time and make debugging produce the expected results. This is the default.
- `-Os`: Optimize for size. -Os enables all -O2 optimizations except those that often increase code size
- `-Ofast`: Disregard strict standards compliance. -Ofast enables all -O3 optimizations. It also enables optimizations that are not valid for all standard-compliant programs.
- `-Og`: Optimize debugging experience.

#### Results
| Compilation option | Assume time(`s`) | Shared library size(`M`) |
|---|---|---|
| `-O0` | 49 | 29 |
| `-O1` | 43 | 3.5 |
| `-O2` | 48 | 3.4 |
| `-O3` | 49 | 3.4 |
| `-Os` | 46 | 3.5 |
| `-Ofast` | 49 | 3.4 |

### Debugging options
To tell GCC to emit extra information for use by a debugger, in almost all cases you need only to add `-g` to your other options.

GCC allows you to use `-g` with `-O`. But this combination taken by optimized code may occasionally be surprising:
- some variables you declared may not exist at all;
- flow of control may briefly move where you did not expect it;
- some statements may not be executed because they compute constant results or their values are already at hand;
- some statements may execute in different places because they have moved out of loops.

This makes it reasonable to use the optimizer for programs that might have bugs.

If you are not using some other optimization option, consider `-Og -g` option. With no `-O` option at all, some compiler passes that collect information useful for debugging do not run at all, so that `-Og` may result in a better debugging experience.

Here are some options for debugging:
- `-g`: Produce debugging information in the operating system’s native format (stabs, COFF, XCOFF, or DWARF). GDB can work with this debugging information.
- `-g[level]`: Request debugging information ans also use `level` to specify how much information. The default level is 2.
 - Level 0: produces no debug information at all
 - Level 1: produces minimal information, enough for making backtraces in parts of the program that you don’t plan to debug. This includes descriptions of functions and external variables, and line number tables, but no information about local variables.
 - Level 2: produces normal debug information as default.
 - Level 3: includes extra information, such as all the macro definitions present in the program. Some debuggers support macro expansion when you use -g3.

What we should know is that producing debug symbols will increase both executable file size and compilation time, so the conclusion is:
- if you don't need to debug with gdb, do not add `-g` option to g++ flags;
- if you need to debug with gdb, use `-Og -g` option to get better debugging experience.

#### Results
| Compilation option | Assume time(`s`) | Shared library size(`M`) |
|---|---|---|
| `-O0 -g` | 66 | 151 |
| `-Og -g` | 67 | 135 |
| `-O` | 45 | 3.5 |
| `NONE` | 63 | 130 |


## Include denpencies optimization

### compiler static analyzer

### Doxygen

### include-what-you-need

## Code optimization

### Predeclaration

### Replace boost library

# Reference
- [C++ Preprocessor](https://www.w3schools.in/cplusplus-tutorial/preprocessor/)
- [The Compilation Process](https://medium.com/coding-den/the-compilation-process-a1307824d40e)
- [GCC Command Options](https://gcc.gnu.org/onlinedocs/gcc/Invoking-GCC.html#Invoking-GCC)
- [C++服务编译耗时优化原理及实践](https://tech.meituan.com/2020/12/10/apache-kylin-practice-in-meituan.html)
