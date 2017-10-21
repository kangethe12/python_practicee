class Employee:
    employeecount = 0

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.employeecount += 1

    def displaycount(self):
        print("We have {} number of employees".format(Employee.employeecount))

    def displayemployee(self):
        print("Name: ", self.name, "Salary: ", self.salary)

    def work(self):
        return "do some work"


emp1 = Employee("Zara", 2000, 23)
emp2 = Employee("Romelu Lukaku", 4000, 34)
print(emp1.employeecount)
print("We have {} number of employees".format(Employee.employeecount))
