# Student Performance Analyzer
# Non-Agriculture Python Test Code

def calculate_total(marks):
    return sum(marks)

def calculate_average(total, subjects):
    return total / subjects

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def result_status(marks):
    if min(marks) < 35:
        return "Fail"
    return "Pass"


# -------- Main Program --------
print("📘 Student Performance Analyzer 📘")

name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

marks = []
for i in range(subjects):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(total, subjects)
grade = calculate_grade(average)
status = result_status(marks)

print("\n📊 Result Summary")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
print("Result:", status)
