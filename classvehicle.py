class Vehicle:
  name = ""
  kind = "car"
  color = ""
  value = 00.00
  def description (self):
    desc ="%s is a %s %s worth $%.2f." % (self.name,self.color,self.kind,self.value)
    return desc
car1 = Vehicle()
car1.name = "Fuso"
car1.color = "grey"
car1.kind = "lorry"
car1.value = 1000

car2 = Vehicle()
car2.name = "ferrari"
car2.color = "Red"
car2.kind = "convertible"
car2.value = 5000

print (car1.description())
print (car2.description())