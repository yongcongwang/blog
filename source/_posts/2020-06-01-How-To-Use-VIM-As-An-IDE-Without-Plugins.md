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
- Normal mode, the characters you type are treated as commands;
- Insert mode, the characters you type are treated as text.
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
In `Normal` mode, you can delete characters with following commands:
- `x`: delete a character. Move the cursor over a character and type `x` to delete it. (This is a throwback to the old days of the typewriter, when you deleted things by typing xxxx over them.)
- `dd`: delete a line.
- `J`: delete a line break.

#### Undo And Redo
If you delete too much, you can type `u` to undo the last edit.
And if you **undo** too much, you can press `CTRL-R` to **redo** them.

#### Other Editing Commands
- `a`: since `i` **inserts** a character before the cursor, you can use `a` to **append** a character after the cursor.
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

### Move Faster
#### Charactor Based Movement
One of the most useful movement commands is the single-character search command `fx`(Find x) which search forward in the line for the character `x`. 
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
- `t` and `T`, works like the `f`, but it stops one character before the searched character:

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
- `^`, to move to the first character of the line;
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

Once you searched something, you can use `n` to jump to **next** item, and `N` to jump to previous item.

#### Marks
Vim enables you to place your own marks in the text:
- `mx`, to mark a the place under the cursor as `x`, x can be `a to z`;
- `\`x`, to go to the marked place;
- `marks`, to place all the marks you can go to.

### Change Smarter
#### Operators With Range
You can use the pattern `[operator][count][range]` to change more characters. For example, `d4w` means `[delete][4][word]`:
```
        To err is human. To really foul up you need a computer. 
                         ------------------>
                                 d4w

        To err is human. you need a computer.
```
And similar usages are:
- `d2e`, means delete 2 words' end;
```
        To err is human. you need a computer. 
                        -------->
                           d2e

        To err is human. a computer.
```

- `d$`, means delete to the end of the line;
```
        To err is human. a computer. 
                       ------------>
                            d$

        To err is human 

```

#### Change Text
Another operator is `c`, change. It acts just like the `d` operator, but it leaves you in `Insert` mode:
- `cw`, changes a word;
```
        To err is human 
           ------->
             c2wbe<Esc>

        To be human
```
- `cc`, changes a line and leaves you in `Insert` mode;

The `r` is not an operator, it waits for you to type a character, and will replace the character under the cursor with it.
```
        there is somerhing grong here 
        rT           rt    rw

        There is something wrong here
```
For commands, you can use a count befor them:
```
        There is something wrong here 
                           5rx

        There is something xxxxx here
```

#### Repeating A Command
The `.` may be the most simple yet powerful commands in vim. It repeats the last change. For instance, suppose you are editing an HTML file and want to delete all the <B> tags:
```
                              To <B>generate</B> a table of <B>contents 
        f<   find first <     --->
        df>  delete to >         -->
        f<   find next <           --------->
        .    repeat df>                     --->
        f<   find next <                       ------------->
        .    repeat df>                                     -->
```

#### Visual Mode
##### Select characters
To delete simple items the operator-range works quite well. But often it's not so easy to decide which command will move over the text you want to change. Then you can use press `v` to enter the `Visual` mode.
You move the cursor over the text you want to work on. While you do this, the text is highlighted. Finally, you type the operator command.
```
                This is an examination sample of visual mode 
                               ---------->
                                 velllld

                This is an example of visual mode
```
##### Select Lines
If you want to work on whole lines, use `V` to start `Visual` mode.
```
                          +------------------------+
                          | text more text         |
                       >> | more text more text    | |
        selected lines >> | text text text         | | Vjj
                       >> | text more              | V
                          | more text more         |
                          +------------------------+
```

##### Select Blocks
If you want to work on a rectangular block of characters, use `CTRL-v` to start `Visual` mode. This will be really useful when you comment several code lines.

##### Go To Other Side
If you have selected some text in `Visual` mode, and discover that you need to change other end of seleqction, use `o` to go to **other** side.

##### Copy And Paste
Yanking is a vim name for copying, and you can use the operator `yw` to copy a word, a count is possible as usual.
```
        let sqr = LongVariable * 
                 -------------->
                       y2w

        let sqr = LongVariable * 
                               p

        let sqr = LongVariable * LongVariable
```
The `yy` command yanks a whole line, just like `dd` deletes a whole line.
And stil, you can first use visual mode to select some characters and then yank them.

##### Other Useful Commands
- `~`: Change case of the character under the cursor;
- `u`(visual mode): Make selected characters lower case;
- `U`(visual mode): Make selected characters upper case;
- `I`: Start `Insert` mode after moving the cursor to the first no-blank in the line;
- `A`: Start `Insert` mode after moving the cursor to the end of the line;
- `di(` or `di)`: Delete all characters between `()`;
- `di[` or `di]`: Delete all characters between `[]`;
- `di{` or `di}`: Delete all characters between `{}`;
- `da(` or `da)`: Delete all characters between `()` and `()`;
- `da[` or `da]`: Delete all characters between `[]` and `[]`;
- `da{` or `da}`: Delete all characters between `{}` and `{}`;

#### Macros

#### Replace

## Advanced Features

### Edit Multiple Files

### Split Windows

### Communicate With Terminal

### Code Jump

### Code Complete

### Fold

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

