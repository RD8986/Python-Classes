# import os

# path = r"E:\tesfile"
# user_i = int(input("\nPlease enter any number to create files: "))
# for x in range(1, user_i + 1):
#     filenum = x
#     filepath = os.path.join(path, f"{filenum}.txt")
#     while os.path.exists(filepath):
#         filenum += 1
#         filepath = os.path.join(path, f"{filenum}.txt")
#     with open(filepath, "w") as file_object:
#         file_object.write(f"This number of file is: {filenum} ")
            
# print("Task completed successfully")

import glob
path=r"E:\tesfile"
input=int(input("Please enter any number: "))

data=[x for x in  glob.glob(path +f"\*")] 
y=len(data)

for x in range(y+1,(y+input+1)):  
    with open(path + f"\{x}.txt","a") as object:
         object.write(f"the file number is {x} ")
         
print("Successfully Created")