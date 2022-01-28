<div align="center">

# CALL Documentation
CALL 0.1 essential release
| [Main page](../README.md) | [Table of contents](./README.md)

</div>

**WARNING**: This release is **not** a final release and you shouldn't use it!
it's just for developement/testing purposes

In the example with [expressions](./exprs.md) uses labels:
```asm
lbl    Main
    set    @a, 1
    doiffh [@a == 1] jmp ax_is_1 ; if @a == 1 then jump to ax_is_1

loclbl ax_is_1
    jmp    POS

```
in CALL to define a label there is the `lbl` instruction and to define a
local label there is the `loclbl` instruction
```asm
; lbl instruction
;  Defines the given label
;
;  syntax:  lbl [label:KEYWORD]
;  example:
lbl my_label
    ; label code

; loclbl instruction
;  Defines the given local label
;
;  syntax:  loclbl [label:KEYWORD]
;  example:
lbl Hello ; parent label
    loclbl my_label ; child label
        ; label code

loclbl my_label ; child of Hello

;  example 2:
loclbl my_label ; invalid! orphan local label
```
to jump to a label there is the `jmp` instruction and to jump to a local
label there is the `locjmp` instruction
```asm
; jmp instruction
;  jumps to the given label
;
;  syntax:  jmp [label:KEYWORD]
;  example:
lbl my_label
    ; label code

    jmp my_label ; while (true)

; locjmp instruction
;  jumps to the given local label
;
;  syntax:  locjmp [label:KEYWORD]
;  example:
lbl Hello ; parent label
    loclbl my_label ; child label
        ; label code

        locjmp my_label
loclbl my_label ; child of Hello

;  example 2:
loclbl my_label ; invalid! orphaned child label

locjmp my_label ; invalid! orphaned child label
```
