<div align="center">

# CALL Documentation
CALL 0.1 essential release
| [Main page](../README.md) | [Table of contents](./README.md)

</div>

**WARNING**: This release is **not** a final release and you shouldn't use it!
it's just for developement/testing purposes

## Syntax
The CALL syntax is similar to assembly

### Comments
```asm
This isn't a comment
; This is a comment
```

### Instructions
```asm
[name] [param1] [param2] [param3] [...] [param255]
instr  50       51       52
```

### Variables
Variables start with the `@` token:
```asm
; To define a variable use the set instruction
; syntax: set [name:VAR] [value:ANY]
set @variable 1 ; this is a Variable
```

### Expressions
Expressions begin with `[` and end with `]`
```
set @variable [@a + @b]  ; expressions have C-style syntax
set @variable [@a == @b] ; you can use logics
set @varibale [@a >> 5]  ; bitwise

set @variable [@a == @b && @a == @c || @a == @d]
```

### Documentation
To document an instruction the syntax is:
```asm
; [instruction name]
;  [description]
;
;  syntax: [instruction name] [param1:type] [param2:type]
```
EXAMPLE:
```asm
; inc instruction
;  Includes a library (e.g. STanDard LIBrary)
;
;  syntax:  inc [library name:KEYWORD]
;  example:
    inc STDLIB ; includes STanDard LIBrary
```

### Markdown documentation
To document an instruction with markdown the syntax is
```markdown
# `inc` instruction
Includes a **library**, (e.g. STanDard LIBrary)

syntax: `inc [library:KEYWORD]`
example: `inc STDLIB`, includes STanDard LIBrary
```
