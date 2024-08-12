import os
import json

def top_three_students():
    path = "./students_data.json"
    if os.path.exists(path):
        with open(path, "r") as file:
            data = json.load(file)
        if not data:
            print("\nNo student data found!")
            return

        for student in data:
            qualifications = student.get("EducationalQualification", [])
            total_percentage = sum(float(q.get("percentage", 0)) for q in qualifications)
            student["TotalPercentage"] = total_percentage

        sorted_students = sorted(data, key=lambda student: student["TotalPercentage"], reverse=True)

        top_students = sorted_students[:3]
        
        if top_students:
            print("Top 3 Students based on percentage:")
            for student in top_students:
                print(f"\n Student ID: {student['ID']}, Name: {student['Name']}, Total Percentage: {student['TotalPercentage']}%")
            for student in top_students:
                print(json.dumps(student, indent=4))
        else:
            print("No students available.")
    else:
        print("\nNo student data found!")
