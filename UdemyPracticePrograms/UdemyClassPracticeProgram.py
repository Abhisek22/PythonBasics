# Understanding class creation in Python
#Objective: Create a basic calculator class to perform
# addition, subtraction, multiplication, and division.
#Instructions:
#1. Create a class named BasicCalculator.
#2. Define a constructor that initializes two numbers. Use numbers 10 & 5
#3. Implement methods for:
# Addition
# Subtraction
# Multiplication
# Division
#4. Each method should return the result of the operation.
#5. Create an instance of the BasicCalculator class and demonstrate the
# functionality of each method.

class BasicCalculator:

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
    def addition(self):
        return (self.firstNumber + self.secondNumber)
    def subtraction(self):
        return (self.firstNumber - self.secondNumber)
    def multiplication(self):
        return (self.firstNumber * self.secondNumber)
    def division(self):
        return (self.firstNumber / self.secondNumber)

obj = BasicCalculator(10, 5)
print(f"Addition: 10 + 5 = {obj.addition()}")
print(f"Subtraction: 10 - 5 = {obj.subtraction()}")
print(f"Multiplication: 10 * 5 = {obj.multiplication()}")
print(f"Division: 10 / 5 = {obj.division()}")