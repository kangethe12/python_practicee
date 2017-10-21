from employee_class import Employee, test_variable


class Admin(Employee):

    def __init__(self, name, salary, age, head):
        super().__init__(name, salary, age)
        self.head = head

    def authorize_salary(self):
        return "Get paid"

    def hire_employee(self, employee):
        return "{}, you're hired!".format(employee)

    def fire_employee(self, employee):
        return "{}, you're fired!".format(employee)

    def work(self):
        role = "Manage my juniors"
        return role


admin = Admin("Mike", 10000, 34, "Sales")
print(type(admin))
# print(admin.authorize_salary())
# print(admin.display_employee())
# print(admin.work())
# print(test_variable)

