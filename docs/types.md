<div align="center">
# Types
| [Table of contents](./manual.md) | [Getting started](./getting_started.md) |
</div>
CALL is a dynamically typed language so you don't need to declare
variables like C or Java, that's how you declare a variable
```asm
set    @myvar 50           ; that's a number

setarr @myarr 1 2 3 4      ; that's a dynamic array

setdim @fixedarr 4 1 2 3 4 ; that's a fixed size array

getidx @myarr 0            ; get first index
```
