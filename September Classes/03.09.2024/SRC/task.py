class Student_data:
    sid=int(input("Student Id : "))
    sname=input("Student name : ")
    saddress=input("Student Address : ")
    smobnum=int(input("Student mobile number : "))
    def __init__(self):
        self.sid
        self.sname
        self.saddress
        self.smobnum
    # def studentdetails(data):
    #     data.sid
    #     data.sname
    #     data.saddress
    #     data.smobnum
    #     return data
obj=Student_data()
# # vardata=obj.studentdetails()
# # vardata=Student_data.studentdetails()
# print(obj.sid)
# print(obj.sname)
# print(obj.saddress)
# print(obj.smobnum)
print(obj.__init__)