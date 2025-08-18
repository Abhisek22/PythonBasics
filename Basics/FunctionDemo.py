#Functions or Methods are group of related statements that perform a specific task

#Declaring a function
def GreetMe():
    print("Good Morning")

#Calling a function
GreetMe()

#Declaring function with arguements
def GreetWithname(name):
    print("Good Morning "+name)

GreetWithname("Abhisek Ghosh")

#Declaring methods with arguement to add integers and return the value
def addNumbers(a,b):
    return a+b
print("{}{}".format("The summation of numbers are : ",addNumbers(2,3)))
print(f"The summation of numbers are : {addNumbers(125,250)}")