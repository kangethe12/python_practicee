class Employee:
  Employeecount = 0
  def __init__(self, name, salary):
    self.name = name
    self.salary =salary
    Employee.Employeecount +=1

  def displaycount(self):
    print ("We have %d number of employess" % Employee.Employeecount)
  def displayemployee(self):
    print ("Name: ",self.name, ",Salary: ",self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Romelu Lukaku", 4000)
emp1.displayemployee()
emp2.displayemployee()
print ("We have %d number of employess" % Employee.Employeecount)