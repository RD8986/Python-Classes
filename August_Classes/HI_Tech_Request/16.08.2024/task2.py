
import time


data= [
  {
    "LeadgenID": "3807711036143434",
    "created_time": "2024-08-20 15:12:40"
  },
  {
    "LeadgenID": "907026628115000",
    "created_time": "2024-08-20 00:49:35"
  },
  {
    "LeadgenID": "874997091189898",
    "created_time": "2024-08-16 00:25:12"
  },
  {
    "LeadgenID": "515829294158795",
    "created_time": "2024-08-20 22:16:08"
  },
  {
    "LeadgenID": "1501438320475000",
    "created_time": "2024-08-15 20:50:09"
  }
  
  ]

currenttime=time.strftime("%Y-%m-%d", time.localtime())
matches = 0

for entry in data:
    created_date = entry["created_time"].split(" ")[0]  
    if currenttime == created_date:
        matches += 1
print("Total data count : ", matches)