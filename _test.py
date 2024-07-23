from mivmodules import json_loader

load = json_loader.SyncJSONHandler(filepath="js.json").read()

print(load.get('test1', 0))