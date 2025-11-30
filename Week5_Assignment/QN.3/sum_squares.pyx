# sum_squares.pyx
# Cython implementation of sum of squares

# Loop implementation using C integers for speed
cdef long long _sum_squares_loop(long long n):
    cdef long long i, s = 0
    for i in range(1, n + 1):
        s += i * i
    return s

# Expose a Python-callable function (fast C backend)
cpdef long long sum_squares(long long n):
    """Return sum_{i=1..n} i^2 using fast C loop."""
    if n <= 0:
        return 0
    return _sum_squares_loop(n)

# Also expose formula version (constant time) for correctness & speed
cpdef long long sum_squares_formula(long long n):
    """Return sum_{i=1..n} i^2 using closed-form formula."""
    if n <= 0:
        return 0
    # Use 128-bit intermediate on some platforms is not needed in Python,
    # but in C-level long long we assume n is reasonable.
    return (n * (n + 1) * (2 * n + 1)) // 6
