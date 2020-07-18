---
title: Vim Tutor
date: 2018-04-20 18:07:10
mathjax: true
comments: true
categories:
  - tools
---

Vim is a very powerful editor that has many commands, too many to explain in a tutor such as this. This tutor is designed to describe enough of the commands that you will be able to easily use Vim as an all-purpose editor.
<!-- more -->

## Edit Commands

### Mode Select

Press the `Esc` to get in `Normal` mode，`i` to get in `Insert` mode

### Exit Vim

In `Normal` mode, type `:q <Enter>` to exit, `:q! <Enter>` to discard all changes and exit, `:wq <Enter>` to save all changes and exit

### Move Cursor

- Move cursor to left, right, up, down with `h, l, k, j`

- Number `0` move to the head of line, `$` to the end of line

### Delete Charactor

- Press `x` to delete the charactor under the cursor, `dw` to delete a word, `de` to delete from current to the end of the word, `d$` to delete from current to the end of line.

- Press `dd` to delete current line, `2dd` to delete current and next line

### Add Charactor

- Press `i` to insert text
- Press `a` to append text

### Excute Multiple Times

Adding number before commands repeats it that many times, for example, `2w` to move two words, `d2w` to delte two words

### Undo Commands

Press `u` to undo the last commands, `U` to fix a whole line, `Ctrl + R` to redo the commands

### Copy Commands

1. Press `v` to get in `Visual` mode and select charactors
2. Press `y` to copy the charactors
3. Press `p` to paste the charactors

### Move Commands

Press `p` to paste last deleted charactors, just like cut and paste

### Replace Commands

- Press `r` to replace a charactor
- Press `R` to replace many charactors

### Change Commands

Press `ce` to change words to the end


## File Commands

### Jump Commands

- `Ctrl + g` to display current line number
- `G<Number>` or `:<Number>` to jump to <Number> line

### Search Commands

- `/` to search to the end of file
- `n` to jump to next iterm, `N` to jump to previous iterm
- `Ctrl + o` to go back to previous place
- `%` to find a matching ), ], or }
- `:set ic` to ignore case, `:set noic` to not ignore case

### Replace Commands

- `:s/old/new` to replace the first old by new in a line, `:s/old/new/g` to replace all old by new in a line
- `:#,#s/old/new/g` to replace from # to # line
- `:%s/old/new/g` to replace all old by new in a file

### External Commands

`:!` followed by an external command to excute the command, for example: `:!ls`

### Save Commands

- `:w FILENAME` to save current file to <FILENAME>
- `v` to select multiple lines, `:w FILENAME` to save selected text to <FILENAME>

### Insert Commands

`:r FILENAME` to insert file's text in current place
