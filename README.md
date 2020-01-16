# pylpsolve3

pylpsolve3 is a Python 3 wrapper for [lpsolve][origsite]. 
This implementation is based on the [original python module][origdoc] implemented by 
the authors of lpsolve.

## Install

### Using pip (currently unavailable)
Make sure you are using the pip of Python 3. It will not work on Python 2.
```
python3 -m pip install pylpsolve3
```

### Manually
Download the source code and run `python3 setup.py install`
You will need a working C compiler to do this.
If you are on Windows, only MSVC is supported,
so you will need to install Visual Studio or Visual Studio build tools.
The static libraries (`liblpsolve55`) required for building this package
for Windows (`win32`, `win64`), MacOS (`osx64`), and x86_64 Linux(`ux64`)
is provided here for the ease of installation. If you want to build your
own library, please read the [below](#how-to-build-library) section.

## Usage
You can still use the original syntax according to [official documentation][origdoc].
However, due to the limitation of unicode problems, all API calls with string need
to be changed into bytes.
e.g.
```
# Python 2
from lpsolve55 import *
res = lpsolve('set_col_name', lp, ['COLONE', 'COLTWO', 'COLTHREE', 'COLFOUR'])
...
res = lpsolve('solve', lp)
```
need to be changed into
```
# Python 3
from lpsolve55 import *
# 'b' before string literal turns them to byte literal
# you need to do this for all string literals, including those in array
res = lpsolve(b'set_col_name', lp, [b'COLONE', b'COLTWO', b'COLTHREE', b'COLFOUR'])
...
res = lpsolve(b'solve', lp)
```

Due to this limitation, and generally ugly syntax, I added a wrapper for this in `__init__.py`.
You can use the below code for the above example.
```
# Python 3
import pylpsolve3 as lpsolve
res = lpsolve.set_col_name(lp, ['COLONE', 'COLTWO', 'COLTHREE', 'COLFOUR'])
...
res = lpsolve.solve(lp)
```

In general, the syntax `lpsolve('func', ...)` can be replaced into `lpsolve.func(...)`

The function names and unicode-byte conversion is handled internally by the wrapper.
**However, you should not use non-ASCII character for variables names in lpsolve** like below.
```
# using non-ASCII charcters is not recommended
res = lpsolve.set_col_name(lp, ['一', '二', '三', '四'])
```
Although the above code may work in Python, if you try to write this to a file with
`write_lp` and read it again, the program will throw an error.

## How to build library

### Unix (Linux)
1. Download latest source code from [here][source-code].
2. extract content `tar xzvf lp_solve_5.5.2.5_source.tar.gz`
3. go to directory `lpsolve55`
4. open `ccc`, on line 40, add `-fPIC` after `$c`
4. run `sh ccc` to build, output is in `/bin/ux32` or `/bin/ux64`
The static library `liblpsolve55.a` is what you need

### Windows
1. Follow the first 3 steps for Unix
2. Open `lib.vcproj` in Visual Studio, you may see a few warnings about migration.
Just ignore them and let Visual Studio do the work.
3. Choose the platform and type of library you want to build (`win32/x64`, `Debug/Release`)
and click `build solution` under `build` menu.
There should be a file `liblpsolve55.lib` under `<Win32/x64>/<Debug/Release>`
4. You will need to rename this file to `lpsolve55.lib` if you want to use it to build
this package

[source-code]: https://sourceforge.net/projects/lpsolve/files/lpsolve/5.5.2.5/lp_solve_5.5.2.5_source.tar.gz/download
[origsite]: https://sourceforge.net/projects/lpsolve/
[origdoc]: http://lpsolve.sourceforge.net/5.5/Python.htm