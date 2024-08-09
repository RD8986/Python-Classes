import os
import json

def deletestudentrecords():
    path = "./students_data.json"
    if os.path.exists(path):
        with open(path, "r") as file:
            data = json.load(file)
        
        id = int(input("Enter student ID: "))
        
        for x in data:
            if x["ID"] == id:
                data.remove(x)
                break
        
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Record with ID {id} has been deleted.")
    else:
        print("No Data Found ")
