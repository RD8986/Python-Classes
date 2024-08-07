import os

path = "./students_data.txt"

def add_students_data():
    id = input("\nEnter student ID: ")
    name = input("\nEnter student's name: ")
    address = input("\nEnter student's address: ")
    number = input("\nEnter student mobile number: ")
    age = input("\nEnter student age: ")

    new_data = f"ID: {id}, Name: {name}, Address: {address}, Number: {number}, Age: {age}\n"

    with open(path, "a") as file:
        file.write(new_data)
    
    print("\nStudent data added successfully!")

def display_student_data():
    if os.path.exists(path):
        with open(path, "r") as file:
            data = file.read()
            print(data)
    else:
        print("\nNo student data found!")

def find_student_by_mobile():
    search_number = input("\nEnter the student mobile number to search: ")
    
    if os.path.exists(path):
        with open(path, "r") as file:
            found = False
            for line in file:
                if f"Number: {search_number}," in line:
                    print("\nStudent data found:")
                    print(line)
                    found = True
                    break
            if not found:
                print("\nNo student found with the given mobile number.")
    else:
        print("\nNo student data found!")

def main():
    while True:
        print("\n 1. Register a new student")
        print("\n 2. Display student data")
        print("\n 3. Search Student by Mobile Number")
        print("\n 4. Exit")
        
        choice = int(input("\nPlease enter your choice: "))
        
        if choice == 1:
            add_students_data()
        elif choice == 2:
            display_student_data()
        elif choice == 3:
            find_student_by_mobile()
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Please enter a valid input (1-4)")

main()
