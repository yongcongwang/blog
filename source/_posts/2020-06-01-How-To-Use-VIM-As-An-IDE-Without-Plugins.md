---
title: How To Use VIM As An IDE Without Plugins
mathjax: true
comments: true
date: 2020-06-01 14:24:14
categories: software
---
## Environment
### Update Vim
The default version of vim in `ubuntu 18.04 LTS` is 8.0, and the newest version of vim is 8.2.
```bash
git clone git@github.com:vim/vim.git
cd vim
make
sudo make install
```
### Config
```bash
bash <(curl -s https://raw.githubusercontent.com/yongcongwang/dotfiles/master/deploy.sh) vim
```
## General Usage
### New To Vim
#### Start Vim
To start vim, type the command `vim file.txt` at any command prompt. Because this is a new file, you get a blank window:
```
        +---------------------------------------+
        |#                                      |
        |~                                      |
        |~                                      |
        |~                                      |
        |~                                      |
        |"file.txt" [New file]                  |
        +---------------------------------------+
```
- `#` is the cursor position;
- `~` indicates lines not in the file;
- at the bottom of vim is a message line that indicates the file is named file.txt and shows you are creating a new file.

#### Insert Text
The vim editor is a modal editor, which means that the editor behaves differently depending on which mode you are in.
The two basic modes are:
- Normal mode, the charactors you type are treated as commands;
- Insert mode, the charactors you type are treated as text.
To get in insert mode you should type `i`(for Insert), and to get in normal mode you should type `<ESC>`.

#### Moving Around
In `Normal`mode, to move the cursor, press the `h, j, k, l` keys as indicated.
```
             ^
             k              Hint:  The h key is at the left and moves left.
       < h       l >               The l key is at the right and moves right.
             j                     The j key looks like a down arrow.
             v
```

#### Delete Charactors
In `Normal` mode, you can delete charactors with following commands:
- `x`: delete a charactor. Move the cursor over a charactor and type `x` to delete it. (This is a throwback to the old days of the typewriter, when you deleted things by typing xxxx over them.)
- `dd`: delete a line.
- `J`: delete a line break.

#### Undo And Redo
If you delete too much, you can type `u` to undo the last edit.
And if you **undo** too much, you can press `CTRL-R` to **redo** them.

#### Other Editing Commands
- `a`: since `i` **inserts** a charactor before the cursor, you can use `a` to **append** a charactor after the cursor.
- `o`: creates a new and empty line below the cursor and puts vim in `Insert` mode.
- `O`: creates a new and empty line above the cursor and puts vim in `Insert` mode.
- `[cnt]-command`: you can add a number `cnt` before command to repeat the command `cnt` times. For example, you want to move up 9 lines, you can either type `kkkkkkkkk` or you can type `9k`.

#### Getting Out
After modifying the file, you can use:
- `w`: to **write** the file;
- `q`: to **quite** the vim;
- `wq`: to **write** the file and then **quit**  the vim;
- `q!`: to ignore the changes and **force** **quit** vim.

#### Find Help
Everything you always wanted to know can be found in the vim help files. To get help on **something**, use the command:
- `:help {something}`

### Moving Faster
#### Charactor Based Movement
One of the most useful movement commands is the single-charactor search command `fx`(Find x) which search forward in the line for the charactor `x`. 
For example, you are at the beginning of the following line. Suppose you want to go to the h of human, just execute the command `fh` and the cursor will be positioned over the h:
```
To err is human.  To really foul up you need a computer. 
---------->--------------->
    fh           fy
```
And you can specify a count:
```
To err is human.  To really foul up you need a computer. 
          --------------------->
                   3fl
```
Other similar commands:
- `F`, to find backward:

```
To err is human.  To really foul up you need a computer. 
          <---------------------
                    Fh
```
- `t` and `T`, works like the `f`, but it stops one charactor before the searched charactor:

```
To err is human.  To really foul up you need a computer. 
           <------------  ------------->
                Th              tn
```

#### Word Based Movement
You can also move the cursor based on words:
- `w`, to move forward a **word**;
```
        This is a line with example text 
          --->-->->----------------->
           w  w  w    3w
```
- `b`, to move **backward** a word;
```
        This is a line with example text 
        <----<--<-<---------<---
           b   b b    2b      b
```
- `e`, to the **end** of a word;
- `ge`, to the end of a previous word.
```
        This is a line with example text 
           <-   <--- ----->   ---->
           ge    ge     e       e
```

#### Line Based Movement
- `0`, to move to the start of a line;
- `^`, to move to the first charactor of the line;
- `$`, to move to the end of the line;
- `gg`, to move to the first line of the file;
- `G`, to move to the last line of the file;
- `:[num]`, to move to [num] line.

#### Parenthesis Based Movement
When writing a program you often use pairs like `()`, `[]` and `{}`, you can use `%` to jump between them.
If the cursor is on a `(` it will movet to the matching `)`. If it's on a `)` it will move to the matching `(`.
```
                            %
                         <----->
                if (a == (b * c) / d) 
                   <---------------->
                            %
```

#### Scrolling Around
- `CTRL-U`, to scroll **up** half a screen of text;
- `CTRL-D`, to scroll **down** half a screen of text;
- `CTRL-F`, to scroll **forward** a screen of text;
- `CTRL-B`, to scroll **backward** a screen of text;
- `zz`, to move the cursor line to the center of the screen.
```
                                       +----------------+
                                       | some text      |
                                       | some text      |
                                       | some text      |
        +---------------+              | some text      |
        | some text     |  CTRL-U  --> |                |
        |               |              | 123456         |
        | 123456        |              +----------------+
        | 7890          |
        |               |              +----------------+
        | example       |  CTRL-D -->  | 7890           |
        +---------------+              |                |
                                       | example        |
                                       | example        |
                                       | example        |
                                       | example        |
                                       +----------------+


        +------------------+             +------------------+
        | earlier text     |             | earlier text     |
        | earlier text     |             | earlier text     |
        | earlier text     |             | earlier text     |
        | earlier text     |   zz  -->   | line with cursor |
        | earlier text     |             | later text       |
        | earlier text     |             | later text       |
        | line with cursor |             | later text       |
        +------------------+             +------------------+                                       
```

#### Search
- `/{string}`, to search forward `string` in the whole file;
- `*`, pressing `*` at the word you want to search works just like `/{string}`;
- `?{string}`, to search word `string` in the whole file;
- `#`, pressing `#` at the word you want to search works just like `/{string}`;

## Advanced Features

### Communicate With Terminal

## Compile(C++)

### g++

### cmake

## Debug

### Gdb

### Gdb And Apollo

## Use Vim Mode In Other apps

### bash

### Chrome

### Visual Studio Code

