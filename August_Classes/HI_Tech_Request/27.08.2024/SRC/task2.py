studentdata = {1: 4000, 2: 4000, 3: 15000, 4: 30000, 5: 10000, 6: 4000}
list=[]
for x in studentdata.values():
    list.append(x)
newdata=sorted(list)
print("Minimum Salary : ")
for x,y in studentdata.items():
    if y==newdata[0]:
        print(x,y)
print("\n Maximum Salary : ")
for x,y in studentdata.items():
    if y==newdata[-1]:
        print(x,y)

# lowsalary = 0
# highsalary = 0

# first_value = True
# for salary in studentdata.values():
#     if first_value:
#         lowsalary = salary
#         highsalary = salary
#         first_value = False
#     else:
#         if salary < lowsalary:
#             lowsalary = salary
#         if salary > highsalary:
#             highsalary = salary

# print("Minimum Salary:")
# for key, value in studentdata.items():
#     if value == lowsalary:
#         print(f"{key} : {value}")

# print("\nHighest Salary:")
# for key, value in studentdata.items():
#     if value == highsalary:
#         print(f"{key} : {value}")
