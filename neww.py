employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]

salaries = list(map(lambda emp: emp["salary"], employees))
min_salary = min(salaries)
max_salary = max(salaries)
filtered_salaries = list(filter(
    lambda salary: salary != min_salary and salary != max_salary,
    salaries
))
average_salary = sum(filtered_salaries) / len(filtered_salaries)

print("Average salary (excluding min and max):", average_salary)
