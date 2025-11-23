import asyncio
import time

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

async def print_letters():
    letters = ['A', 'B', 'C', 'D', 'E']
    for letter in letters:
        print(letter)
        await asyncio.sleep(1.5)

async def main():
    start_time = time.perf_counter()   # Start timer

    await asyncio.gather(
        print_numbers(),
        print_letters()
    )

    end_time = time.perf_counter()     # End timer
    total_time = end_time - start_time

    print(f"Total time taken: {total_time:.2f} seconds")

asyncio.run(main())
