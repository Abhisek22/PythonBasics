#Working with Lists
#1. Create a list named fruits that contains below five different fruit names (strings).
#2. "apple", "banana", "cherry", "date", "elderberry"
#3. print the first and last elements of the list.
#4. Use slicing to print the second and third fruits from the list.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit: "+fruits[0])
print("Last fruit: "+fruits[-1])
print(f"Fruits from index 1 to 2: {fruits[1:3]}")