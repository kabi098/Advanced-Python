from setuptools import setup, Extension

module = Extension(
    "squaremodule",
    sources=["squaremodule.c"]
)

setup(
    name="squaremodule",
    version="1.0",
    description="A Python interface to a C function that squares numbers",
    ext_modules=[module]
)
