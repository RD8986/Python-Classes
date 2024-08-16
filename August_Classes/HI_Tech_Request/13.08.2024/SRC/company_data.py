import json

final_data = []

def save_emp_data():
    emp_name = input("Enter employee name: ")
    salary = input("Enter employee salary: ")
    bonus = input("Enter bonus percent: ")
    new_entry = {"Employee Name": emp_name, "Payable": [{"Salary": salary, "Bonus": bonus}]}
    final_data.append({"Indixpert": new_entry})
    print("\nData added successfully")

def display_emp_data():
    print(json.dumps(final_data, indent=4))

def manage_emp_data():
    while True:
        print("\n1. Save employee data")
        print("2. Display employee data")
        print("3. Exit")
        choice = int(input("\nPlease enter your choice: "))

        if choice == 1:
            save_emp_data()
        elif choice == 2:
            display_emp_data()
        elif choice == 3:
            break
        else:
            print("Please enter a choice between 1 to 3.")

manage_emp_data()
