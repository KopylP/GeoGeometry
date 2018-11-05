import json
from typing import Dict


def saveJson(obj):
    with open("test.json", "w") as f:
        json.dump(obj, f)

obj = {"Hello": "World"}
saveJson(obj)