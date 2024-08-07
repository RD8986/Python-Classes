import os
import json

def add_students_data():
    path = "./students_data.json"
    id = int(input("\nEnter student ID: "))
    name = input("\nEnter student's name: ")
    address = input("\nEnter student's address: ")
    number = int(input("\nEnter student mobile number: "))
    age = int(input("\nEnter student age: "))

    new_data = {"ID": id, "Name": name, "Address": address, "Number": number, "Age": age}

    if os.path.exists(path):
        with open(path, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(new_data)

    with open(path, "w") as file:
        json.dump(data, file)
    
    print("\nStudent data added successfully!")