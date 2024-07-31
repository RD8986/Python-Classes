# user_i = int(input("Please enter a number between 1 and 5: "))

# if 1 <= user_i <= 5:
#     for a in range(1, user_i + 1):
#         path = f"E:\\Files\\{a}.txt"
#         with open(path, "w") as file:
#             file.write("This is my file")
#     print("Files have been created.")
# else:
#     print("Error: Number must be between 1 and 5.")


path=r"E:\Files"
input=int(input("Please enter any number: "))
for x in range(1,input+1):
    with open(path + f"\{x}.txt","w") as object:
        object.write(f"the file number is {x} ")
    print("Successfully Created")