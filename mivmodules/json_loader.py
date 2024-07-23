import json

class SyncJSONHandler:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        
    def read(self) -> dict:
        try:
            with open(self.filepath, 'r') as file:
                content = file.read()
                return json.loads(content)
        except Exception as e:
            print(e)
            return {}
        
class AsyncJSONHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath
        
    async def read(self) -> dict:
        try:
            with open(self.filepath, 'r') as file:
                content = file.read()
                return json.loads(content)
        except Exception as e:
            print(e)
            return {}