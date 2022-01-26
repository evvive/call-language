<div align="center">

# Syntax
| [Table of contents](./manual.md) | [Getting started](./getting_started.md) | [Syntax](./syntax.md) |

</div>

## Code structure
This is how a basic code structure looks:
```asm
deff Main ; function executed by interpreter
par  NULL ; no parameters

; program main part

ret  0   ; always return a value
```
## Instructions
In the code structure above there are several **instructions**:
 - `deff`
 - `par`
 - `ret`
Every instruction has **parameters**, parameters are strings, variables,
numbers, flags:
```asm
[instruction name] [param1] [param2] [param3]
^^^^^^^^^^^^^^^^^  ^^^^^^^^ ^^^^^^^^ ^^^^^^^^
     DEFF            Main     NULL     NULL

deff Main
```

## Comments
In CALL there are only single line comments like in assembly:
```
; comment
deff MyFunction ; comment
```

## Variables
Variables starts always with `@`, **constants** are all UPPER CASE and
**variables** are all lowercase
```asm
set  @my_variable 1 ; use set instruction to set a variable
setk @KONSTANT    1 ; use setk instruction to set a constant

set  @NO_KONSTANT   ; error!
setk @konstant      ; error!

setp @%pointer      ; that's a pointer (more in manual)
```

## Directives
In CALL there are directives like C/C++
```asm
!include "./myfile.call.asm" ; include file

!call                        ; print CALL message

!define instr                ; define instruction
!par    @a @b                ; define params

!ret                         ; instruction dont return a value
```
