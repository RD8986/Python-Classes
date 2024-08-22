import requests
import json
data = requests.get("https://api.sampleapis.com/cartoons/cartoons2D")
jdata=data.json()
creator_name = input("Please enter a creator name: ")
for x in jdata:
    if x["creator"][0].lower()==creator_name.lower():
        print(x)
# if data.status_code == 200:
#     json_data = data.json()
#     creator_name = input("Please enter a creator name: ")

#     if creator_name:
#         found = False
#         for cartoon in json_data:
#             if cartoon["creator"][0].lower() == creator_name.lower():
#                 print(json.dumps(cartoon, indent=4))
#                 found = True
        
#         if not found:
#             print(f"No cartoons found by creator '{creator_name}'.")

#     else:
#         print("Creator name cannot be empty.")
# else:
#     print(f"Failed to fetch data. Status code: {data.status_code}")
    

