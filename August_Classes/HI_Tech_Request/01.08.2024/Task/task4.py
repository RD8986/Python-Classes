import requests
import json
res = requests.get("https://api.sampleapis.com/codingresources/codingResources")
rdata = res.json()
for x in rdata:
    if "types" in x and "meeting" in x["types"]:
        for key, value in x.items():
            print(f"{key}: {value}")

# for x in rdata:
#     for y in x["types"]:
#         if y=="meeting":
#             print(x)