class Employee:
    employee_count = 0

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.employee_count += 1

    def display_count(self):
        print("We have {} number of employees".format(Employee.employee_count))

    def display_employee(self):
        print("Name: ", self.name, "Salary: ", self.salary)

    def work(self):
        return "Do some work"


test_variable = "sample"


def sample_method():
    return "Sample method in employee class module"
