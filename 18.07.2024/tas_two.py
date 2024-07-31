# studentlist=["Anand","Amit","Faiz","Mani","Khushi","Roshani","Nisha","Mazda"]

# set1=set(num)
# set2=set(num2)

# common=set1.intersection(set2)
# print("Common elements : ", common)

num=[2,1,3,5,7]
num2=[1,3,9,10,11,12]

duplicate_values=[]

for x in num:
    for x in num2:
        if x not in duplicate_values:
            duplicate_values.append(x)
            
print(duplicate_values)
        