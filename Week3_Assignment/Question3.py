import asyncio

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
    await asyncio.gather(
        print_numbers(),
        print_letters()
    )

# Run the main coroutine
asyncio.run(main())
