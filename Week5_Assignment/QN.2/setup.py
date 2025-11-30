from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "dot_product",              # module name
        ["dot_product.pyx"],        # Cython source file
    )
]

setup(
    name="cython_dot_product",
    ext_modules= cythonize(
        extensions,
        compiler_directives={"language_level": "3"},
    ),
)
