array = []
userinput = input("Enter any five names separated by commas: ")
array = userinput.split(",")

unique_data = []

for name in array:
    if name not in unique_data:
        unique_data.append(name)

print("Unique data:", unique_data)



# print("Enter 10 numbers : ")
# for x in range(10):
#     userinput=int(input())
#     array.append(userinput)