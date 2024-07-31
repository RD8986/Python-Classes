from HiTech import hitech_students
from VOTS import vots_students

print("1 Hitech Student")
print("2 Vots Student")
taskno=""
while taskno != 0:
    taskno=int(input("Please Enter Any Number: "))
    match taskno:
        case 1:
            hitech_students.get_Hi_Tech_Student_Data()
        case 2: 
            vots_students.get_VOTS_Students_Data()