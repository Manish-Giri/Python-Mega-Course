import os, json

data = json.load(open("data.json"))
print(len(data))

print(data["hunger"])