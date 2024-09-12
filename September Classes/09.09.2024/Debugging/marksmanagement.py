def markckeck():
    marks = int(input("Please enter student marks: "))

    if marks > 100 or marks < 0:
        print("Please enter correct marks")
    elif marks >= 80:
        print("Merit with First Division")
    elif marks >= 60:
        print("First Division")
    elif marks >= 45:
        print("Second Division")
    else:
        print("Fail")
markckeck()
