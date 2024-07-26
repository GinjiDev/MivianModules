import aiohttp
import numpy
import imageio

async def get_average_rgb_color(url: str) -> str | None:
    if not url: return (0, 0, 0)

    async with aiohttp.ClientSession() as session:
        data = await session.get(url)
        avatar_data = await data.read()

    avatar_img = imageio.imread(avatar_data, format="JPG")
    avatar_img = avatar_img.astype(numpy.uint8)

    avg_color = numpy.mean(avatar_img, axis=(0, 1))
    avg_r, avg_g, avg_b = map(int, avg_color[:3])

    return avg_r, avg_g, avg_b