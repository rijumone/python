class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary



print "Employee.__doc__:", Employee.__doc__

# "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
emp2 = Employee("Manni", 5000)


emp1.displayEmployee()

print "Total Employee %d" % Employee.empCount

emp1.age = 7  # Add an 'age' attribute.

print hasattr(emp1, 'age')    # Returns true if 'age' attribute exists

getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8 , if attr does not exist then it will be created
delattr(emp1, 'age')    # Delete attribute 'age'



print "=========================================================================================="



class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method