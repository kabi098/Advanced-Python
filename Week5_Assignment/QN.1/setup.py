from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

extensions = [
    Extension(
        "reverse_string",           # module name
        ["reverse_string.pyx"],
    )
]

setup(
    name="cython_reverse",
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
)