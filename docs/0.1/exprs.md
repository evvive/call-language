<div align="center">

# (1) CALL 0.1 Docs: Syntax rules

| [Main page](../README.md) | [Table of contents](./README.md) |

This release is **not** a final release and you shouldn't use it!
it's just for developement/testing purposes

</div>
<hr>

In CALL you can use expressions to do more complex operations:
```asm
; @a = (((@b + @c) / @a) << 5) ** 2
set @a [@b + @c / @a << 5 ** 2]
```
**NOTE**: There isn't priority, expressions are **always** executed from
left to right

## Using expressions instead of `cmp`
In x86 assembly to compare 2 registers you use the `cmp` instruction
```asm
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

<hr>
<div align="center">

CALL 0.1 essential release<BR>
| [Next](../README.md) | [Previous](./README.md) |

</div>
