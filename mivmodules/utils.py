import random
import string

class Utils:
    def __init__(self) -> None:
        pass
    
    def _generate_password(self, length: int) -> str:
        
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        
        return password
    
    def generate_password_sync(self, length: int = 8) -> str:
        return self._generate_password(length)
    
    async def generate_password_async(self, length: int = 8) -> str:
        return self._generate_password(length)
    