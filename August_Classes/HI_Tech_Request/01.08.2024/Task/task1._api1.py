import requests
import json
response=requests.get("https://api.sampleapis.com/coffee/hot")
# print(response.status_code)
# print(response.json())
# print(response.text)
# print(response)
if response.status_code == 200:
    print("Data Response Successfully")
else:
    print("Data Response Failes")