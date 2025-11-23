import asyncio

async def print_letters():
    letters = ['A', 'B', 'C', 'D', 'E']
    for letter in letters:
        print(letter)
        await asyncio.sleep(1.5)
# Run the coroutine
asyncio.run(print_letters())