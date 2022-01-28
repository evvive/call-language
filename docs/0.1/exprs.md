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

## Using expressions instead of `cmp`
In x86 assembly to compare 2 registers you use the `cmp` instruction
```
Main:
    mov ax, 1
    cmp ax, 1

    je  .ax_is_1

    hlt

    .ax_is_1
        ; if jumps here ax == 1 is true
        jmp $
```
since CALL is a more modern version of assembly you can do this:
```asm
lbl    Main
    set    @a, 1
    doiffh [@a == 1] jmp ax_is_1 ; if @a == 1 then jump to ax_is_1

loclbl ax_is_1
    jmp    POS

```
