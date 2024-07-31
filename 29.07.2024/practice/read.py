# path=r"E:\JSON_DATA\dwsample2json.json"

# with open(path, "r") as file:
#     data=file.read()
#     print(data)

import json

path = r"E:\JSON_DATA\dwsample2json.json"

with open(path, "r") as file:
    data = json.load(file)

subjects = data["quiz"].keys()

for subject in subjects:
    print(subject)
