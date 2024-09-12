import json
path=r"./result.json"
marks = int(input("Please enter marks: "))
if marks >= 80:
    grade = "Merit with First Division"
    status = "Passed with Merit"
elif marks >= 60 and marks < 80:
    grade = "First Division"
    status = "Passed"
elif marks >= 45 and marks < 60:
    grade = "Second Division"
    status = "Passed"
else:
    grade = "Fail"
    status = "Fail"
result = {
    "marks": marks,
    "grade": grade,
    "status": status
}
with open(path, "w") as json_file:
    json.dump(result, json_file, indent=4)
    
print("Data saved to student_result.json")