
inputData = "ABC"

if inputData == "XYZ":
    print("I am in If block")
    print("The Expected meets Actual")
else:
    print("I am in Else Block")
    print("The Expected does not meet the Actual")

compareRange = 8

if compareRange >= 5:
    print("I am in If block")
    print("The If condition is satisfied")
else:
    print("I am in Else Block")
    print("The Expected does not meet the Actual")


# To Demonstarte the "else if" styntax in Python
score = 75

# Start with an 'if' statement
if score >= 90:
    print("Excellent! You got an A.")
# Use 'elif' to check another condition if the first one is False
elif score >= 80:
    print("Great job! You got a B.")
# You can have multiple 'elif' statements
elif score >= 70:
    print("Good effort! You got a C.")
elif score >= 60:
    print("You passed with a D.")
# Optionally, end with an 'else' block to handle all other cases
else:
    print("You did not pass.")
