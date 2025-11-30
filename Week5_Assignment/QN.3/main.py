from time import perf_counter
import sys
import sum_squares

def timed(fn, *args):
    t0 = perf_counter()
    r = fn(*args)
    t1 = perf_counter()
    return r, t1 - t0

def main():
    n = 5
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except:
            pass

    print(f"Computing sum of squares up to n={n}")

    res_formula, t_formula = timed(sum_squares.sum_squares_formula, n)
    print(f"formula result: {res_formula} (time: {t_formula:.6f}s)")

    res_loop, t_loop = timed(sum_squares.sum_squares, n)
    print(f"loop result   : {res_loop} (time: {t_loop:.6f}s)")

    # quick check
    print("results match:", res_formula == res_loop)

if __name__ == "__main__":
    main()
