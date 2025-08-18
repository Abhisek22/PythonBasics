from ClassBasics import Calculator

# Inheriting Claculator class as parent class
class ChildClass (Calculator):
    num2 = 200

# Creating constructor of child class to invoke the parent class constructor.
# This is a rule that if parent class is having customized constructor then
# in child class we need to define a customized constructor to invoke Parent class constructor

    def __init__(self):
        Calculator.__init__(self,10,20)

# child class method defined to interact with parent class variable (num) & parent class method (addDigit())
    def getCompleteData(self):
        return self.num2 + self.num + self.addDigit()

obj01 = ChildClass()
print(obj01.getCompleteData())
