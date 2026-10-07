class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 500


class Manager(Employee):
    def calculate_salary(self):
        return super().calculate_salary() + 300


class Developer(Employee):
    def calculate_salary(self):
        return 40 * 25


manager = Manager("Alice")
developer = Developer("Bob")

print(f"{manager.name} Salary: ${manager.calculate_salary()}")
print(f"{developer.name} Salary: ${developer.calculate_salary()}")
