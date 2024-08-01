import requests
import json
res=requests.get("https://api.sampleapis.com/codingresources/codingResources")
# if res.status_code==200:
#     print("\n Data Response capture successfully \n")
#     print(res.json())
# else:
#     print("Data Response capture failed")
print(res.json())
# print(res.text)
# print(res.content)