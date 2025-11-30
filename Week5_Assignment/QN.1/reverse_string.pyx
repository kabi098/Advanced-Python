def reverse_string(str s):
    """
    Reverse a Python unicode string and return the result.
    Implemented in Cython with typed indices for a small speedup.
    """
    cdef Py_ssize_t n = len(s)
    cdef Py_ssize_t i
    cdef list chars = [None] * n
    for i in range(n):
        chars[i] = s[n - 1 - i]
    return ''.join(chars)