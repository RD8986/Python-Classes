path=r"D:\Development\Live Class and Student Document\python\Files and OS\batch1.txt"
# data=open(path,'r')
# print(data.read())
# data.close()

with open(path,'r') as object:
     print(object.readlines())
     print(object.readline())
     print(object.read())