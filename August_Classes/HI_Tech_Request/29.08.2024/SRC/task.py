import os
from datetime import datetime

paths = [r"E:\Students Name\hitechstudent.txt", 
         r"E:\Students Name\votsstudent.txt"]
path3 = r"E:\Students Name\Final_Student.txt"

findata = []
modified_times = []

for path in paths:
    mod_time = os.path.getmtime(path)
    modified_times.append((path, mod_time))

if modified_times[0][1] > modified_times[1][1]:
    first_file = modified_times[1][0]
    last_file = modified_times[0][0]
else:
    first_file = modified_times[0][0]
    last_file = modified_times[1][0]

def display_file_info(modified_times):
    print("File Modification Information:")
    for file_info in modified_times:
        file_name = file_info[0]
        mod_time = datetime.fromtimestamp(file_info[1]).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{file_name} was last modified on: {mod_time}")

display_file_info(modified_times)

with open(first_file, 'r') as file:
    findata.extend(file.readlines())

with open(last_file, 'r') as file:
    findata.extend(file.readlines())

with open(path3, "w") as file:
    file.writelines(findata)

print("Success")
