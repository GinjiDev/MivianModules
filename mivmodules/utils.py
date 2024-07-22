import secrets
import string
from mivmodules._constants import TRANSLIT_DICT

class Utils:
    def __init__(self, translit_dict: dict = TRANSLIT_DICT) -> None:
        self.translit_dict = translit_dict
    
    def _generate_password(self, length: int, digits: int = True) -> str:
        
        characters = string.ascii_letters + (string.digits if digits else '')
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        return password
    
    def generate_password_sync(self, length: int = 8, digits: int = True) -> str:
        return self._generate_password(length, digits)
    
    async def generate_password_async(self, length: int = 8, digits: int = True) -> str:
        return self._generate_password(length, digits)
    
    
    def _eval(self, expression: str = '0') -> int:
        return eval(expression)
    
    def eval_sync(self, expression: str = '0') -> int:
        return self._eval(expression)
    
    async def eval_async(self, expression: str = '0') -> int:
        return self._eval(expression)
    
    
    def _translit_to_cyrillic(self, translit: str) -> str:
        cyrillic = ''.join(self.translit_dict.get(char, char) for char in translit)
        return cyrillic
    
    def translit_to_cyrillic_sync(self, translit: str) -> str:
        return self._translit_to_cyrillic(translit)
    
    async def translit_to_cyrillic_async(self, translit: str) -> str:
        return self._translit_to_cyrillic(translit)
    
    
    def _word_count(self, text: str) -> int:
        return len(text.split())
    
    def word_count_sync(self, text: str) -> int:
        return self._word_count(text)
    
    async def word_count_async(self, text: str) -> int:
        return self._word_count(text)