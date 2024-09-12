class Student:
    studentName="Amit"
    studentAddress="Bihar"
    studentid=1

    @classmethod
    def printdata(cls):
        print(cls.studentid)
        print(cls.studentName)
        print(cls.studentAddress)

obj=Student()
obj.printdata()