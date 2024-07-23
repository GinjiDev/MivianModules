from mivmodules import color
import asyncio


async def main():
    return await color.get_average_rgb_color(url="https://i.pinimg.com/236x/d9/15/61/d9156134f3a7f74ddc1cfc57902d1467.jpg")

print(asyncio.run(main()))