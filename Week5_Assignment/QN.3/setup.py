from setuptools import setup
from Cython.Build import cythonize

setup(
    name="sum_squares",
    ext_modules=cythonize("sum_squares.pyx", annotate=True),
    zip_safe=False,
)
