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
```

## Directives
In CALL there are directives like C/C++, all directives start are `d + [name]`
```asm
!include "./myfile.call.asm" ; include file
```

## Expressions
In CALL there are expressions:
```asm
instr [ [expression] ] ; expression structure

instr [@a + @b]        ; arithmetic expression

instr [@a | @b]        ; bitwise expression

instr [@a == @b]       ; logic expression
```
