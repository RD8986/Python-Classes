import requests
import json

response = requests.get("https://api.sampleapis.com/coffee/hot")
response = response.json()

class Coffee:
    def __init__(self, data):
        self.__dict__ = data

def Get_Coffee_Data():
    for n in response:
        if n["title"] == "Cappuccino":
            data = Coffee(n)
            return data

vardata = Get_Coffee_Data()
print(json.dumps(vardata.__dict__, indent=2))
