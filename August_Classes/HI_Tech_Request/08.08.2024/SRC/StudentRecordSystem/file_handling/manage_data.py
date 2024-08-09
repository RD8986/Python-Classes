from .createstudentrecords import add_students_data
from .displaystudentrecords import display_student_data
from .searchstudentdata import search_student_data
from .deletestudentrecord import deletestudentrecords
def manage_studentrecord():
    print("\n 1. Register a new student")
    print("\n 2. Display student data")
    print("\n 3. Search data by mobile number")
    print("\n 4. Delete student record ")
    print("\n 5. Exit")
    while True:
        choice = int(input("\nPlease enter your choice: "))

        if choice == 1:
            add_students_data()
        elif choice == 2:
            display_student_data()
        elif choice == 3:
            search_student_data()
        elif choice == 4:
            deletestudentrecords()
        elif choice == 5:
            print("Exiting the program...")
            break
        else:
            print("Please enter a valid input (1-4)")
