class Calculator:
    num = 100 # Class Variable

    #Default Constructor
#    def __init__(self):
#        print("I will be called automatically as I am default constructor")

    #Parametrized Constructor
    def __init__(self, a, b):
        self.firstDigit = a   # Instance Variable
        self.secondDigit = b  # Instance Variable

    def getData(self):
        print("I am now executing a method inside a class")

    def addDigit(self):
        return self.firstDigit + self.secondDigit + Calculator.num + self.num

#obj = Calculator()  # Invoking default Constructor
#obj.getData()  # Invoking method of a class using Object
#print(obj.num) # Invoking class Variable using class object

obj1 = Calculator(2, 3)  # Invoking Parametrized Constructor
print(f"The result is : {obj1.addDigit()}")

obj2 = Calculator(4, 5)  # Invoking Parametrized Constructor
print(f"The result is : {obj2.addDigit()}")