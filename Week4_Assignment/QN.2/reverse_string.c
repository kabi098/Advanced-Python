/* reverse_string.c */
#include <string.h>
#include <stddef.h>

int reverse_string(const char *in, char *out, size_t out_size) {
    if (!in || !out || out_size == 0) return -1;

    size_t len = strlen(in);
    size_t needed = len + 1; /* include NUL terminator */
    if (needed > out_size) return -2; /* caller's buffer too small */

    /* reverse */
    for (size_t i = 0; i < len; ++i) {
        out[i] = in[len - 1 - i];
    }
    out[len] = '\0';
    return 0;
}
