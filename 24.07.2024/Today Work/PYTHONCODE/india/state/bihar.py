import sys
import os

#sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'indixpert'))

# source1 = r"E:\PYTHONCODE\indixpert\hitech\batch\batch1"
# source2 = r"E:\PYTHONCODE\indixpert\vots\batch\batch1"
# sys.path.append(source1)
# sys.path.append(source2)

# ALTERNATIVE USE 

sys.path.append(os.path.join(os.getcwd(),r"indixpert\hitech\batch\batch1"))
sys.path.append(os.path.join(os.getcwd(),r"indixpert\vots\batch\batch1"))

from hitech_student import get_Hi_Tech_Student_Data
from votsstudent import get_VOTS_Students_Data

print("1 Hitech Student")
print("2 Vots Student")

taskno=""
while taskno != 0:
    taskno=int(input("Please Enter Any Number: "))
    match taskno:
        case 1:
            get_Hi_Tech_Student_Data()
        case 2: 
            get_VOTS_Students_Data()
            