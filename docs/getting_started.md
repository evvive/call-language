# Getting started in CALL
Getting started with the call language

## Installing it on your system
### Requirements
Windows/MacOS
 - `git` Git CLI [here](https://git-scm.com/)
 - `python3` Python 3 [here](https://www.python.org/)

Linux
```bash
sudo apt install git python3 # Debian
sudo dnf install git python3 # Fedora
sudo pacman -S git python3   # Arch linux
```

To install CALL clone the git repository in your home directory
```bash
# Linux & MacOS
git clone https://github.com/evvive/call-language ~/CALL
```
```batch
rem Windows
rem Clone in the current directory
git clone https://github.com/evvive/call-language
```

Now with your favorite text editor create a new file and copy this example
```asm
; Hello, World program
inc  STDLIB

deff Main
par  NULL

call PrintLN NULL "Hello, World"

ret  0
```
See the manual to get an in-depth explanation on how this works
