<div align="center">

# Hello World explanation
| [Table of contents](./manual.md) | [Getting started](./getting_started.md) | [Syntax](./syntax.md) |

</div>

Probably you've copied the Hello World program but you don't know what it does
well you are in the right place
```asm
inc  STDLIB                      ; Include the standard library

deff Main                        ; Define the main function
par  NULL                        ; without any parameter

call PrintLN NULL "Hello, World" ; nothing = PrintLN("Hello, World")
                                 ; NULL is required!

ret  0                           ; return 0
```
the program above in C
```c
#include <STDLIB>

int main(void) {
    NULL = PrintLN("Hello, World");

    return 0;
}

```

**NOTES**: You should always return or the interpreter is going to crash
even if the function hasn't parameters you should always
```asm
par NULL
```
