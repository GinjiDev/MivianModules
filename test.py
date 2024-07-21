from mivmodules import utils

password = utils.Utils()

print(password.generate_password_sync(length=10))

async def main():
    password_ = await password.generate_password_async(length=10)
    print(password_)
    
import asyncio

asyncio.run(main())