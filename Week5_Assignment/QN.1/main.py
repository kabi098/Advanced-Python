import reverse_string

if __name__ == "__main__":
    tests = [
        "Hari",
        "Kabi",        # unicode test (Nepali/Hindi)
        "Advance", 
        "King",
        "Hello, Ram"
    ]
    for t in tests:
        print(f"original: {t!r} -> reversed: {reverse_string.reverse_string(t)!r}")