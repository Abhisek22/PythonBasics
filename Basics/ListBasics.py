# List is a versatile data type exclusive in Python, which can simultaneously hold
# different types of data.
# It is an ordered sequence of data written using square brackets ([])
# and separated by comma (,)


# Storing data of different data types in a list
al = [1, 2, "bingo", 4.50, 5j]

# Print values stored in specific index
print(al[0])  # Output is 1
print(al[2])  # Output is bingo
print(al[3])  # Output is 4.5

# Print last index value of a list
print(al[-1])  # Output is 5j

# Print sub-values of list as per the provided start index and end index
print(al[1:3])  # Output is [2, 'bingo']
print(al[:3])  # Output is [1, 2, 'bingo']
print(al[2:])  # Output is ['bingo', 4.5, 5j]
print(al[:])  # Output is [1, 2, 'bingo', 4.5, 5j]

# Insert value in list
al.insert(2, 'uncle')
print(al)  # Output is [1, 2, 'uncle', 'bingo', 4.5, 5j]

# Append value in list which will add new value at the last index of the lsit
al.append("End")
print(al)  # Output is [1, 2, 'uncle', 'bingo', 4.5, 5j, 'End']

# Replace or update any value in list
al[2] = 'UNCLE'
print(al)  # Output is [1, 2, 'UNCLE', 'bingo', 4.5, 5j, 'End']

# Merging list1 with list2
al2 = [10, 20, 'New_End']
al.extend(al2)
print(al)  # Output is [1, 2, 'UNCLE', 'bingo', 4.5, 5j, 'End', 10, 20, 'New_End']

# To Delete or Remove or Pop values from a list

# 1. del statement
# Purpose: Deletes items by index or slices. It can also delete the entire list object.
# Usage: del list_name[index] or del list_name[start:end] or del list_name.
# Return Value: Does not return the deleted element(s).

my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Deletes element at index 2 (value 3)
print(my_list)  # Output: [1, 2, 4, 5]
del my_list[0:2]  # Deletes elements from index 0 up to (but not including) index 2
print(my_list)  # Output: [4, 5]
del my_list  # Deletes the entire list object
#print(my_list) # This would raise a NameError as my_list no longer exists

# 2. pop() statement
# Purpose: Removes and returns an element at a specified index.
#         If no index is given, it removes and returns the last element.
# Usage: list_name.pop(index) or list_name.pop().
# Return Value: Returns the removed element.

my_list = [10, 20, 30, 40, 50]
removed_item = my_list.pop(1)  # Removes element at index 1 (value 20)
print(my_list)  # Output: [10, 30, 40, 50]
print(removed_item)  # Output: 20
last_item = my_list.pop()  # Removes the last element (value 50)
print(my_list)  # Output: [10, 30, 40]
print(last_item)  # Output: 50

# 3. remove() statement
# Purpose: Removes the first occurrence of a specified value from the list.
# Usage: list_name.remove(value).
# Return Value: Does not return any value (returns None)

my_list = ['apple', 'banana', 'orange', 'banana']
my_list.remove('banana')  # Removes the first 'banana'
print(my_list)  # Output: ['apple', 'orange', 'banana']
#my_list.remove('grape') # This would raise a ValueError if 'grape' is not in the list

#Erase all elemnets in a list
print(al)  # Output is [1, 2, 'UNCLE', 'bingo', 4.5, 5j, 'End', 10, 20, 'New_End']
al.clear()
print(al)  # Output is []
