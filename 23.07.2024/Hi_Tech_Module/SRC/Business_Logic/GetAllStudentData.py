import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'HUB'))

import hitech_students
import vots_students

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