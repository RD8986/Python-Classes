import os
import json

path = "./students_data.json"

def add_students_data():
    id = int(input("\nEnter student ID: "))
    name = input("\nEnter student's name: ")
    address = input("\nEnter student's address: ")
    number = int(input("\nEnter student mobile number: "))
    age = int(input("\nEnter student age: "))
    
    qualifications = []
    while True:
        qualification_name = input("\nEnter qualification (e.g., 10th, 12th etc.): ")
        passing_year = int(input("Enter passing year: "))
        percentage = input("Enter percentage: ")

        qualifications.append({
            "qualificationname": qualification_name,
            "passingyear": passing_year,
            "percentage": percentage
        })

        more = input("\nDo you want to add another qualification? (yes/no): ")
        if more.lower() != "yes":
            break

    new_data = {
        "ID": id,
        "Name": name,
        "Address": address,
        "Number": number,
        "Age": age,
        "EducationalQualification": qualifications
    }

    if os.path.exists(path):
        with open(path, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(new_data)

    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    
    print("\nStudent data added successfully!")
