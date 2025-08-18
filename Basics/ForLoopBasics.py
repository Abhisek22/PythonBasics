#Iterating List
# 1. Iterating through each List indexes using Loop

alst = [22, "ESCAPE", 45.9, 3j, 50, "1000"]
for item in alst:
    print(item)

# 2. Iteration with Index using range() and len()

for item in range(len(alst)):
    print(f"List Index is : {item} Value stored is : {alst[item]}")

# 3. Iteration with Index and Value using enumerate()

for item, value in enumerate(alst):
    print(f"Index : {item}, Value : {value}")

# 4. Iterating list and storing value to new list
# while applying filter to the existing list

original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list if x % 2 == 0]
print(squared_list) # Output: [4, 16]

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#Iterating Strings
# 1. Iterating through each String indexes using Loop

input = "Playground"

for item in input:
    print(item)

# 2. String Iteration with Index using range() and len()

for item in range(len(input)):
    print(f"String Index is : {item}, Value stored is : {input[item]}")

# 3. String Iteration with Index and Value using enumerate()

for item, char in enumerate(input):
    print(f"Index : {item}, Value : {char}")

#Summing Integers upto the provided range

summation = 0
for j in range(1,10,1):
    summation = summation + j
print ("{} {}".format("The total summation is : " , summation)) # Output : The total summation is :  45

#Applying Increment/Decrement in Forloop like i++/i--

for i in range(1,10,2):
    print(i) # Output : 1 3 5 7 9

for k in range(10,1,-2):
    print(k) # Output : 10 8 6 4 2

#Nested Loop

for l1 in range(1,4,1):
    for l2 in range(1,5,2):
        print(l2)