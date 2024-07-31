# import hi_tech_students
# import vots_tech_students

# x = ""

# while x != 0:
#     x = int(input("Enter 1 for Hi-Tech students, 2 for VOTS students, or 0 to exit: "))

#     if x == 1:
#         for student in hi_tech_students.Hi_Tech_Students:
#             print("Hi-Tech Student Details:")
#             print(student)
#     elif x == 2:
#         for student in vots_tech_students.vots_students:
#             print("VOTS Student Details:")
#             print(student)
#     elif x != 0:
#         print("Invalid input. Please enter 1 or 2.")

import hi_tech_students
import vots_tech_students

print("1 Hitech Student")
print("2 Vots Student")


taskno=int(input("Please Enter Any Number: "))
match taskno:
    case 1:
        hi_tech_students.Gethitechstudent()
    case 2: 
        vots_tech_students.GetVotsStudents()