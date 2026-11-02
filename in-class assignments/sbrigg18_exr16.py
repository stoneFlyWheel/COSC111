def count_by_department(employees):
    """
    employees is a list of tuples: (name, department)
    Returns a dictionary mapping department -> number of employees
    """

    department_counter = {}

    for index in range(len(employees)):
        department = employees[index][1]
        if department in department_counter:
            department_counter[department] += 1
        else:
            department_counter[department] = 1

    return department_counter


# Test data and driver code (no changes needed below this line)
employees = [
    ("Alice", "Reactor Operations"),
    ("Ben", "Safety"),
    ("Carla", "Reactor Operations"),
    ("Dan", "Maintenance"),
    ("Elena", "Safety"),
    ("Frank", "Reactor Operations"),
]

result = count_by_department(employees)
print(result)

for department, count in result.items():
    print(department, ":", count)
