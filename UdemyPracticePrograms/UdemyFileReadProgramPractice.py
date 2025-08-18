#Read and Print File Contents
#Objective: Write a program to read the contents of a file and
# print it to the console.
#Instructions:
#1. Sample file file1.txt is provided with this assignment.
#2. Write a Python script that opens the file and reads all its contents.
#3. Print the entire content of the file.

with open('../Resources/file1.txt','r') as file:
    content = file.read()
    print(content)
