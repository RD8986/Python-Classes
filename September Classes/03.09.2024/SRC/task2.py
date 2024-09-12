class Person:
    name=input("Enter a person you want to greet : ")
    age=int(input("Age : "))
    def greet(self):
        print(f"Welcome to IndiXpert : {self.name} \n Age : {self.age}")
        
obj=Person()
obj.greet()