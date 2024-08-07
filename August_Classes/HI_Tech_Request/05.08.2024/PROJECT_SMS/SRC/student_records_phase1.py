import os
import json

path = "./students_data.json"
print("\n 1. Register a new student")
print("\n 2. Display student data")
print("\n 3. Search data by mobile number")
print("\n 4. Exit")

def add_students_data():
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

def display_student_data():
    if os.path.exists(path):
        with open(path, "r") as file:
            data = json.load(file)
            print(json.dumps(data))
    else:
        print("\nNo student data found!")

def search_student_data():
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

def main():
    while True:
        choice = int(input("\nPlease enter your choice: "))
        
        if choice == 1:
            add_students_data()
        elif choice == 2:
            display_student_data()
        elif choice == 3:
            search_student_data()
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Please enter a valid input (1-4)")

main()
