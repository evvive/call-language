<div align="center">

# CALL Documentation
CALL 0.1 essential release
| [Main page](../README.md) | [Table of contents](./README.md)

</div>

**WARNING**: This release is **not** a final release and you shouldn't use it!
it's just for developement/testing purposes

In CALL you can use expressions to do more complex operations:
```asm
; @a = (((@b + @c) / @a) << 5) ** 2
set @a [@b + @c / @a << 5 ** 2]
```
**NOTE**: There isn't priority, expressions are **always** executed from
left to right
