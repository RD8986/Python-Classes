path=r"E:\file\t.txt"


with open (path, "r+") as file:
    file.write("This is x mode one ")
    data=file.read()
    print(data)
print("File successfully created")
# Works properly


# with open (path, "w+") as file:
#     file.write("This is x mode one ")
#     data=file.read()
#     print(data)
# print("File successfully created")
# Writes but not read


# with open (path, "x+") as file:
#     file.write("This is x mode one ")
#     data=file.read()
#     print(data)
# print("File successfully created")
# error file exist

# with open (path, "a+") as file:
#     file.write("This is x mode one ")
#     data=file.read()
#     print(data)
# print("File successfully created")
# append but not read