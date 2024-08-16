import json
totalrecord=[]
while True:
    dictdata={}
    company={}
    payable={}
    company["employeename"]=input("Please enter employee name: ")
    payable["salary"]=int(input("Please input Employee Salary: "))
    payable["bonus"]=int(input("Please enter Bonus: "))
    company["payable"]=payable
    dictdata["company"]=company
    totalrecord.append(dictdata)
    inp=input("Do you want to continue: press Y (Continue)/ N (Exit)")
    if inp.lower()=="n":
        print(json.dumps(totalrecord,indent=2))#seperator
        break