import json


def saveJson(var):
    with open("test.json", "w") as f:
        json.dump(var, f)


obj = {"Hello": "World"}
saveJson(obj)
<<<<<<< HEAD
=======
print("Hello World");
print("Hello, bitches");
>>>>>>> 459af19c7bf52574c16bbb605571df5ad5f32727
