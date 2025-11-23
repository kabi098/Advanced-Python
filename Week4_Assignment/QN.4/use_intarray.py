# use_intarray.py
import intarray

class IntArray:
    """Python wrapper around the intarray capsule returned by the C extension."""
    def __init__(self, size):
        self._capsule = intarray.init(size)

    def __len__(self):
        return intarray.size(self._capsule)

    def __getitem__(self, idx):
        return intarray.get(self._capsule, idx)

    def __setitem__(self, idx, value):
        intarray.set(self._capsule, idx, value)

    def free(self):
        """Explicitly free the underlying C memory (idempotent)."""
        if self._capsule is None:
            return
        try:
            intarray.free(self._capsule)
        except (ValueError, TypeError):
            # Treat as already freed or invalid capsule; ignore
            pass
        finally:
            # Always drop our reference so Python wrapper knows it's gone
            self._capsule = None


    def __del__(self):
        # best-effort cleanup (no exceptions allowed here)
        try:
            self.free()
        except Exception:
            pass

    # context-manager support
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.free()
        return False  # don't suppress exceptions

# Example usage
if __name__ == "__main__":
    # Option A: explicit use
    arr = IntArray(5)
    print("size:", len(arr))
    for i in range(len(arr)):
        arr[i] = i * 10
    for i in range(len(arr)):
        print(f"arr[{i}] =", arr[i])

    # Explicit free (safe and idempotent)
    arr.free()
    # calling free again is safe and won't crash
    arr.free()

    # Option B: context manager (automatic clean-up)
    with IntArray(3) as a:
        a[0] = 111
        a[1] = 222
        a[2] = 333
        print("in context:", [a[i] for i in range(len(a))])
    # after the 'with' block the array is freed automatically
