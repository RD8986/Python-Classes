import csv
path=r"D:\Development\Live Class and Student Document\python\Files and OS\industry.csv"
newvar=True
listdata=[]
with open(path,'r') as f:
    data=csv.DictReader(f,delimiter=",")
    for row in data:
        listdata.append(row)
        # dictdata={}
        # dictdata["industryname"]=row[0]
        # dictdata["Indistryid"]=row[1]
        # if newvar:
        #    newvar=False
        # else:   
        #    listdata.append(dictdata)
    


print(listdata)