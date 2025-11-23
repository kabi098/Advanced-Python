# setup.py
from setuptools import setup, Extension
import sys
import pybind11

extra_compile_args = []
extra_link_args = []

# Add C++ standard flag in a cross-platform friendly way
if sys.platform == "win32":
    extra_compile_args = ["/std:c++17"]
else:
    extra_compile_args = ["-std=c++17"]

ext_modules = [
    Extension(
        "concatcpp",
        ["concat.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    )
]

setup(
    name="concatcpp",
    version="0.1",
    description="C++ string concat exposed to Python with pybind11",
    ext_modules=ext_modules,
)
