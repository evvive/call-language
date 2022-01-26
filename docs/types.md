<div align="center">

# Types
| [Table of contents](./manual.md) | [Getting started](./getting_started.md) | [Syntax](./syntax.md) |

</div>

CALL is a dynamically typed language so you don't need to declare
variables like C or Java, that's how you declare a variable
```asm
set    @myvar 50           ; that's a number

set    @mystring "Hello"   ; that's a string

setarr @myarr 1 2 3 4      ; that's a dynamic array

setdim @fixedarr 4 1 2 3 4 ; that's a fixed size array

getidx @myarr 0            ; get first index
```

## Variable naming
If you want to name a variable in CALL you should follow these standards:
```asm
set    @camelCase 1         ; not good
set    @camel_case 1        ; good

set    @include_variable 1  ; variable name shouldn't include variable in
                            ; their name (not good)

set    @include 1           ; good

set    @UPPER_VARIABLE 1    ; that's a constant
```

## Types
Now that you know how to declare variables we'll see the different types:
 - `F64` float64, example: `3.44444`
 - `STR` string, example: `Hello, World`
 - `FLA` flag (boolean), example: `TRUE`
 - `NULL` null (void), `NULL`
