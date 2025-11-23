# setup.py
from setuptools import setup, Extension
import sys

extra_compile_args = []
if sys.platform != "win32":
    extra_compile_args = ["-std=c11", "-O2"]

ext_modules = [
    Extension(
        "intarray",
        ["intarraymodule.c"],
        extra_compile_args=extra_compile_args,
        language="c"
    )
]

setup(
    name="intarray",
    version="0.1",
    description="C-backed simple integer array (init/set/get/free)",
    ext_modules=ext_modules,
)
