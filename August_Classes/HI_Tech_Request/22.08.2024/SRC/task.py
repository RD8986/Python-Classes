# array = []
# userinput = input("Enter any five names separated by commas: ")
# array = userinput.split(",")

# unique_data = []

# for name in array:
#     if name not in unique_data:
#         unique_data.append(name)

# print("Unique data:", unique_data)
# import numpy as np
# sizeofarray=int(input("Please enter the size of array : "))
# array1=input(f"Please enter {sizeofarray} integers seprated by spaces : ")
# # array=array1.split()
# unique_integers=[]
# for x in array1.split():
#     if x not in unique_integers:
#         unique_integers.append(x)
# newarray=" ".join(unique_integers)
# print(newarray)

arraysize=int(input())
array=input()
unique_integers=[]
unique_integers.append(array.split())
sorteddata=sorted(unique_integers)
output=" ".join(unique_integers)


# print("Enter 10 numbers : ")
# for x in range(10):
#     userinput=int(input())
#     array.append(userinput)