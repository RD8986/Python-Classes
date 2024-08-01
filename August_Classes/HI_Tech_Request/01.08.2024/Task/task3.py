import requests
import json
response=requests.get("https://api.sampleapis.com/coffee/hot")
data = response.json()
# user_i=input("Please input coffee name you wish : ")
for coffee in data:
    if coffee["title"].lower() == "cappuccino":
        print(coffee)