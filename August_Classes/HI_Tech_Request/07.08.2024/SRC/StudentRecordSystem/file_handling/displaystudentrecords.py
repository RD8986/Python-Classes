import os
import json
def display_student_data():
    path = "./students_data.json"
    if os.path.exists(path):
        with open(path, "r") as file:
            data = json.load(file)
            print(json.dumps(data))
    else:
        print("\nNo student data found!")

