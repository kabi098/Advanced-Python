// intarraymodule.c
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <stddef.h>

/* --- Simple C IntArray library --- */
typedef struct {
    size_t size;
    int *data;
} IntArray;

static IntArray *intarray_new(size_t size) {
    IntArray *arr = (IntArray *)malloc(sizeof(IntArray));
    if (!arr) return NULL;
    arr->data = (int *)malloc(sizeof(int) * size);
    if (!arr->data) { free(arr); return NULL; }
    arr->size = size;
    for (size_t i = 0; i < size; ++i) arr->data[i] = 0;
    return arr;
}

static void intarray_free(IntArray *arr) {
    if (!arr) return;
    free(arr->data);
    free(arr);
}

static int intarray_set(IntArray *arr, size_t idx, int value) {
    if (!arr || idx >= arr->size) return -1;
    arr->data[idx] = value;
    return 0;
}

static int intarray_get(IntArray *arr, size_t idx, int *out) {
    if (!arr || idx >= arr->size || !out) return -1;
    *out = arr->data[idx];
    return 0;
}

/* --- Python wrapper --- */

static const char *INTARRAY_CAPSULE_NAME = "intarray.IntArray";

/* Capsule destructor - will free native memory if pointer still valid.
   It must handle a NULL pointer gracefully (no-op). */
static void intarray_capsule_destructor(PyObject *capsule) {
    if (!capsule) return;
    /* If capsule isn't valid or has NULL pointer, treat as already freed. */
#if PY_VERSION_HEX >= 0x03070000
    if (!PyCapsule_IsValid(capsule, INTARRAY_CAPSULE_NAME)) return;
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(capsule, INTARRAY_CAPSULE_NAME);
    if (arr) {
        intarray_free(arr);
        /* Set pointer to NULL so subsequent destructor calls are no-ops */
        PyCapsule_SetPointer(capsule, NULL);
    }
#else
    /* For older Pythons, be defensive: try to get pointer and clear errors */
    PyErr_Clear();
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(capsule, INTARRAY_CAPSULE_NAME);
    if (arr) {
        intarray_free(arr);
        PyCapsule_SetPointer(capsule, NULL);
    } else {
        PyErr_Clear();
    }
#endif
}

/* init(size) -> capsule */
static PyObject *py_intarray_init(PyObject *self, PyObject *args) {
    Py_ssize_t size;
    if (!PyArg_ParseTuple(args, "n", &size)) return NULL;
    if (size < 0) {
        PyErr_SetString(PyExc_ValueError, "size must be non-negative");
        return NULL;
    }
    IntArray *arr = intarray_new((size_t)size);
    if (!arr) {
        PyErr_SetString(PyExc_MemoryError, "failed to allocate IntArray");
        return NULL;
    }
    PyObject *capsule = PyCapsule_New((void *)arr, INTARRAY_CAPSULE_NAME, intarray_capsule_destructor);
    if (!capsule) {
        intarray_free(arr);
        return NULL;
    }
    return capsule;
}

/* Helper: validate capsule and return pointer or NULL (with exception) */
static IntArray *get_intarray_from_capsule_checked(PyObject *capsule) {
    if (!PyCapsule_CheckExact(capsule)) {
        PyErr_SetString(PyExc_TypeError, "expected an IntArray capsule");
        return NULL;
    }
#if PY_VERSION_HEX >= 0x03070000
    if (!PyCapsule_IsValid(capsule, INTARRAY_CAPSULE_NAME)) {
        PyErr_SetString(PyExc_ValueError, "invalid or already freed IntArray capsule");
        return NULL;
    }
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(capsule, INTARRAY_CAPSULE_NAME);
    if (!arr) {
        PyErr_SetString(PyExc_ValueError, "IntArray capsule has NULL pointer");
        return NULL;
    }
    return arr;
#else
    PyErr_Clear();
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(capsule, INTARRAY_CAPSULE_NAME);
    if (!arr) {
        PyErr_SetString(PyExc_ValueError, "invalid or already freed IntArray capsule");
        return NULL;
    }
    return arr;
#endif
}

/* set(capsule, index, value) */
static PyObject *py_intarray_set(PyObject *self, PyObject *args) {
    PyObject *capsule;
    Py_ssize_t idx;
    long value;
    if (!PyArg_ParseTuple(args, "Onl", &capsule, &idx, &value)) return NULL;
    IntArray *arr = get_intarray_from_capsule_checked(capsule);
    if (!arr) return NULL;
    if (idx < 0 || (size_t)idx >= arr->size) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }
    if (intarray_set(arr, (size_t)idx, (int)value) != 0) {
        PyErr_SetString(PyExc_RuntimeError, "failed to set value");
        return NULL;
    }
    Py_RETURN_NONE;
}

/* get(capsule, index) -> int */
static PyObject *py_intarray_get(PyObject *self, PyObject *args) {
    PyObject *capsule;
    Py_ssize_t idx;
    if (!PyArg_ParseTuple(args, "On", &capsule, &idx)) return NULL;
    IntArray *arr = get_intarray_from_capsule_checked(capsule);
    if (!arr) return NULL;
    if (idx < 0 || (size_t)idx >= arr->size) {
        PyErr_SetString(PyExc_IndexError, "index out of range");
        return NULL;
    }
    int out;
    if (intarray_get(arr, (size_t)idx, &out) != 0) {
        PyErr_SetString(PyExc_RuntimeError, "failed to get value");
        return NULL;
    }
    return PyLong_FromLong((long)out);
}

/* size(capsule) -> int */
static PyObject *py_intarray_size(PyObject *self, PyObject *args) {
    PyObject *capsule;
    if (!PyArg_ParseTuple(args, "O", &capsule)) return NULL;
    IntArray *arr = get_intarray_from_capsule_checked(capsule);
    if (!arr) return NULL;
    return PyLong_FromSize_t(arr->size);
}

/* py_free(capsule) -> None ; idempotent and safe */
static PyObject *py_intarray_free(PyObject *self, PyObject *args) {
    PyObject *capsule;
    if (!PyArg_ParseTuple(args, "O", &capsule)) return NULL;

    if (!PyCapsule_CheckExact(capsule)) {
        PyErr_SetString(PyExc_TypeError, "expected an IntArray capsule");
        return NULL;
    }

#if PY_VERSION_HEX >= 0x03070000
    /* If not valid (wrong name or NULL pointer), treat as already freed (no-op) */
    if (!PyCapsule_IsValid(capsule, INTARRAY_CAPSULE_NAME)) {
        Py_RETURN_NONE;
    }
#endif

    /* Try to get pointer (this will not raise if capsule is valid) */
    PyErr_Clear();
    IntArray *arr = (IntArray *)PyCapsule_GetPointer(capsule, INTARRAY_CAPSULE_NAME);
    if (!arr) {
        /* Already freed or no pointer; clear any error and return */
        PyErr_Clear();
        Py_RETURN_NONE;
    }

    /* Free native memory */
    intarray_free(arr);

    /* Invalidate capsule pointer — only attempt if we had a non-NULL pointer */
    if (PyCapsule_SetPointer(capsule, NULL) != 0) {
        /* If this fails (rare), clear the error and return None rather than raising */
        PyErr_Clear();
    }

    Py_RETURN_NONE;
}



/* Methods table and module init */
static PyMethodDef IntArrayMethods[] = {
    {"init", py_intarray_init, METH_VARARGS, "Create a new IntArray: init(size) -> capsule"},
    {"set",  py_intarray_set,  METH_VARARGS, "Set value: set(capsule, index, value)"},
    {"get",  py_intarray_get,  METH_VARARGS, "Get value: get(capsule, index) -> int"},
    {"size", py_intarray_size, METH_VARARGS, "Get size: size(capsule) -> int"},
    {"free", py_intarray_free, METH_VARARGS, "Free array: free(capsule) (idempotent)"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef intarraymodule = {
    PyModuleDef_HEAD_INIT,
    "intarray",
    "C-backed simple integer array (init/set/get/free)",
    -1,
    IntArrayMethods
};

PyMODINIT_FUNC PyInit_intarray(void) {
    return PyModule_Create(&intarraymodule);
}
