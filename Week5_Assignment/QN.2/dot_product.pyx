def dot_product(a, b):
    """
    Compute the dot product of two 1D arrays (vectors) of length n.
    a and b should be Python sequences of numbers (e.g., lists).
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")

    cdef Py_ssize_t i, n = len(a)
    cdef double s = 0.0
    cdef double x, y

    for i in range(n):
        x = a[i]
        y = b[i]
        s += x * y

    return s
