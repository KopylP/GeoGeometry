import json


def saveJson(var):
    with open("test.json", "w") as f:
        json.dump(var, f)


obj = {"Hello": "World"}
saveJson(obj)
