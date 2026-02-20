students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]

def average(marks):

    return sum(marks) / len(marks)

def eligible_students(students, min_avg=60):

    return list(filter(lambda s: average(s["marks"]) >= min_avg, students))

def add_grace(marks, grace=5):

    return list(map(lambda m: m + grace, marks))

def total_updated_marks(students):
    eligible = eligible_students(students)

    updated_marks = [mark for s in eligible for mark in add_grace(s["marks"])]
    return sum(updated_marks)


print(total_updated_marks(students))
