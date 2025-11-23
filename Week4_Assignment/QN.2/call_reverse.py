# call_reverse.py
import os
import platform
from ctypes import CDLL, c_char_p, c_size_t, create_string_buffer, c_int

# pick library filename based on platform
_system = platform.system()
libfile = {
    "Linux": "libreverse.so",
    "Darwin": "libreverse.dylib",
    "Windows": "reverse.dll"
}.get(_system)

if libfile is None:
    raise RuntimeError(f"Unsupported platform: {_system}")

libpath = os.path.join(os.getcwd(), libfile)
if not os.path.exists(libpath):
    raise FileNotFoundError(f"Shared library not found: {libpath}")

lib = CDLL(libpath)

# Declare argument and return types for safety
# int reverse_string(const char *in, char *out, size_t out_size)
lib.reverse_string.argtypes = [c_char_p, c_char_p, c_size_t]
lib.reverse_string.restype = c_int

# Input and output buffers
input_str = "Hello, ctypes!"
input_bytes = input_str.encode('utf-8')

# allocate a buffer large enough for result
OUT_SIZE = 256
out_buf = create_string_buffer(OUT_SIZE)

# call the C function
ret = lib.reverse_string(input_bytes, out_buf, OUT_SIZE)

if ret == 0:
    # success
    print("C function returned 0 (success).")
    print("Input :", input_str)
    print("Output:", out_buf.value.decode('utf-8'))
elif ret == -2:
    print("Output buffer too small.")
else:
    print("Error from C function:", ret)
