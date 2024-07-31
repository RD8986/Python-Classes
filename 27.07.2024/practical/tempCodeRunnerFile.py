import os
path = r"E:\Files"
user_i=int(input("\n Please enter any number to create files : "))
for x in range(1, user_i+1):
    filenum=x
    filepath=os.path.join(path, f"\{filenum}.txt")
    while os.path.exists(filepath):
        filenum+=1
        filepath=os.path.join(path, f"\{filenum}.txt")
        with open(filepath, "w") as object:
            object.write(f"This numbefr of file is : {filenum} ")
            
print("Task completed successfully")