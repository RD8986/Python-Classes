import os
import json
def search_student_data():
    path = "./students_data.json"
    if os.path.exists(path):
        search_number = int(input("\nEnter the student mobile number to search: "))
        with open(path, "r") as file:
            data = json.load(file)
            found = False
            for student in data:
                if student["Number"] == search_number:
                    print("\nStudent found:")
                    print(json.dumps(student))
                    found = True
                    break
            if not found:
                print("\nStudent with mobile number", search_number, "not found.")
    else:
        print("\nNo student data found!")
