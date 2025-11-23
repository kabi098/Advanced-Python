import asyncio

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

# Run the coroutine
asyncio.run(print_numbers())
