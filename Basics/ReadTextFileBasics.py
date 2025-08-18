file = open('Resources/test.txt')

#Read all the content of the text file
#print(file.read())

#Read only specified bytes or characters out of the whole content of the text file
#print(file.read(5))

#Read the 1st line only
#print(file.readline())

#Read the 1st and 2nd line only
#Therfore it is clear that with readLine() method each line of the file will be read at
#each encounter
#print(file.readline())
#print(file.readline())

#To read every lines using readLine() method using loop and condition
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()

#To read and write every line of a file using readLines() method,
#which will store each lines in List
#and using loop we will be able to print the lines

lineList = file.readlines()
for line in lineList:
    print(line)

# Closing file to avoid Memory leaks and File to get corrupted
file.close()

