<div align="center">

# CALL Documentation
CALL 0.1 essential release
| [Main page](../README.md) | [Table of contents](./README.md)

</div>

**WARNING**: This release is **not** a final release and you shouldn't use it!
it's just for developement/testing purposes

## Stack
In CALL we have 2 stacks:
 - **Master stack**, the stack used by the interpreter and by STDLIB for basic
   operations
 - **User stack**, the stack used by the user to store data

### Accessing the master stack
You can `push` and `pop` to the master stack with these instructions:
```asm
; mpush instruction
;  Pushs to master stack
;
;  syntax:  mpush [value:ANY]
;  example:
    mpush "flex"
    mpush [@a == @b]

; mpop instruction
;  Pops last index of master stack
;
;  syntax:  mpop [variable:VAR|NULL]
;  example:
    mpop @mark
    mpop @flex
```
