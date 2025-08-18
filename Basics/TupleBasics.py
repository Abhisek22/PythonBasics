# Tuple is also a versatile data type exclusive in Python, which can simultaneously hold
# different types of data.
# It is an ordered sequence of data written using round brackets ()
# and separated by comma (,)
#It functions same as List and the only difference is that the value stored in it are immutable
# thus its values cannot be updated or removed


# Storing data of different data types in a list
atpl = (1, 2, "bingo", 4.50, 5j, 2)

# Print values stored in specific index
print(atpl[0])  # Output is 1
print(atpl[2])  # Output is bingo
print(atpl[3])  # Output is 4.5

# Print last index value of a list
print(atpl[-1])  # Output is 5j

# Print sub-values of list as per the provided start index and end index
print(atpl[1:3])  # Output is [2, 'bingo']
print(atpl[:3])  # Output is [1, 2, 'bingo']
print(atpl[2:])  # Output is ['bingo', 4.5, 5j]
print(atpl[:])  # Output is [1, 2, 'bingo', 4.5, 5j]

# count the number of occurrence
print(atpl.count(2))