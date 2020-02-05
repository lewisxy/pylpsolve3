#from distutils.core import setup, Extension
from setuptools import setup, Extension
import platform

# On POSIX (tested with gcc(Linux) and clang(macOS)), set WIN32 to "NOWIN32"
# enable "hash.c"
# On Windows, setuptools will use msvc, and it will statically link .lib files to .pyd
# WIN32 must be set to "WIN32"
# disable "hash.c" otherwise it will cause error
# the provided library are compiled with vscode 2019, not sure it works
# on older machines during linking

# get client's platform
def getPlatform():
    _os = platform.system()
    if _os == "Windows":
        if platform.architecture()[0] == "64bit":
            return "win64"
        else:
            return "win32"
    if _os == "Linux":
        if platform.architecture()[0] == "64bit":
            return "ux64"
        else:
            return "ux32"
    if _os == "Darwin":  # macOS
        if platform.architecture()[0] == "64bit":
            return "osx64"
        else:
            return "osx32"
    raise Exception("Unknown or unsupported system: ".format(_os))

# detecting whether numpy exist for current python (running this script)
def getNumpy():
    try:
        import numpy
    except Exception:
        return ("NONUMPY", "N/A")
    # <...>/site-packages/numpy/core/include
    numpyIncludePath = numpy.__file__[:-12] + "/core/include"
    return ("NUMPY", numpyIncludePath)

# PLATFORM = ["win32", "win64", "ux32", "ux64", "osx32", "osx64"]
PLATFORM = getPlatform()
# NUMPY = ["NUMPY", "NONUMPY"]
NUMPY, NUMPYPATH = getNumpy()
# WIN32 = ["WIN32", "NOWIN32"]
if "win" in PLATFORM:
    # this has to be turned on windows (even for 64 bit windows)
    # otherwise code won't compile
    WIN32 = 'WIN32'
else:
    WIN32 = 'NOWIN32'
LPSOLVE55 = 'lib/' + PLATFORM

print("""
BUILD_INFO:

PLATFORM={plat}
NUMPY={np}
NUMPYPATH={npp}
WIN32={win}
LPSOLVE55={lp}

""".format(plat=PLATFORM, np=NUMPY, npp=NUMPYPATH, win=WIN32, lp=LPSOLVE55))

if NUMPYPATH == "N/A":
    include_dirs = ['includes/lpsolve']
else:
    include_dirs = ['includes/lpsolve', NUMPYPATH]

# Original package information
# setup(name = "lpsolve55",
#     version = "5.5.0.10",
#     description = "Linear Program Solver, Interface to lpsolve",
#     author = "Peter Notebaert",
#     author_email = "lpsolve@peno.be",
#     url = "http://www.peno.be/",
#     ...
# )
#with open("README.md", "r") as fh:
#    long_description = fh.read()

setup(name = "pylpsolve3",
    version = "0.0.1",
    description = "Python 3 wrapper for lpsolve, see README.md for detail",
    #long_description = long_description,
    #long_description_content_type="text/markdown",
    author = "lewisxy",
    url = "https://github.com/lewisxy/pylpsolve3",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
    ],
    packages = ['pylpsolve3'],
    python_requires = '>=3.4',
    ext_modules = [Extension("lpsolve55",
        ["lpsolve.c", "pythonmod.c"],
        define_macros = [('PYTHON', '1'), (WIN32, '1'), ('NODEBUG', '1'), ('DINLINE', 'static'), (NUMPY, '1'), ('_CRT_SECURE_NO_WARNINGS', '1')],
        include_dirs = include_dirs,
        library_dirs = [LPSOLVE55],
        libraries = ["lpsolve55"])
    ]
)
