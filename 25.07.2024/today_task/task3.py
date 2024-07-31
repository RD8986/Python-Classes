import csv
path=r"D:\Development\Live Class and Student Document\python\Files and OS\industry.csv"
newvar=True
listdata=[]
with open(path,'r') as f:
    data=csv.reader(f,delimiter=",")
    for row in data:
        dictdata={}
        dictdata["industryname"]=row[0]
        dictdata["Indistryid"]=row[1]
        if newvar:
           newvar=False
        else:   
           listdata.append(dictdata)
    


print(listdata)
        
        
    


#{"industryname":"Legal", "Indistryid":1}