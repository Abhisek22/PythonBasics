#Count Lines in a File
#Objective: Count and print the number of lines in a file.
#Instructions:
#1. Use the attached text file "file1.txt"
#2. Write a Python script that opens the file, reads through it line by line,
# counts how many lines it has, and prints the total count.

with open('../Resources/file1.txt','r') as file:
    count = sum(1 for line in file)
    print(f'Total number of lines: {count}')
