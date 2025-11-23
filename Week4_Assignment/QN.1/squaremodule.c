#include <Python.h>

/* C function: square a number */
static PyObject* square(PyObject* self, PyObject* args)
{
    double x;

    if (!PyArg_ParseTuple(args, "d", &x))
        return NULL;

    double result = x * x;

    return Py_BuildValue("d", result);
}

/* Methods table */
static PyMethodDef SquareMethods[] = {
    {"square", square, METH_VARARGS, "Return the square of a number."},
    {NULL, NULL, 0, NULL}
};

/* Module definition */
static struct PyModuleDef squaremodule = {
    PyModuleDef_HEAD_INIT,
    "squaremodule",       /* module name */
    "A module that squares numbers",  
    -1,
    SquareMethods
};

/* Initialization function */
PyMODINIT_FUNC PyInit_squaremodule(void)
{
    return PyModule_Create(&squaremodule);
}
