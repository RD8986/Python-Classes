from .createstudentrecords import add_students_data
from .displaystudentrecords import display_student_data
from .searchstudentdata import search_student_data

def manage_studentrecord():
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
