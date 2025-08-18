#Dictonary is an unordered sequence of data which stores the data in the form of key-value pair
#It is similar to Java Collection type - Hash-Map concept
#It is written using curly braces "{}" in the form of key-va;ue pair
#It is very useful to retrieve data in an optimized way among a large set of data

dict1 = {1:"One", "Two":2, "III":"Three", 4:5}

print(dict1[1])  # output : One
print(dict1[4])  # output : 5
print(dict1["Two"])  # output : 2
print(dict1["III"])  # output : Three

#Adding values to a dictionary during run-time

dict2 = {}

dict2["FirstName"] = "Sachin"
dict2["LastName"] = "Tendulkar"
dict2["PlayerType"] = "Batsman"
dict2["Age"] = 50

print(dict2)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 50}

#To print only Keys from a dictionary
print(dict2.keys())  # output : dict_keys(['FirstName', 'LastName', 'PlayerType', 'Age'])

#To print only Values from a dictionary
print(dict2.values())  # output : dict_values(['Sachin', 'Tendulkar', 'Batsman', 50])

#To print both Key-Values of a Dictionary
print(dict2.items())  #  output : dict_items([('FirstName', 'Sachin'), ('LastName', 'Tendulkar'), ('PlayerType', 'Batsman'), ('Age', 50)])

#To print only dictionary Keys as list
print(list(dict2.keys()))  # Output : ['FirstName', 'LastName', 'PlayerType', 'Age']
#To print only dictionary Values as list
print(list(dict2.values()))  # Output : ['Sachin', 'Tendulkar', 'Batsman', 50]

#To retrieve and print all the Keys and Values pair from the dictionary
print([*dict2.keys()])  # output : ['FirstName', 'LastName', 'PlayerType', 'Age']
print([*dict2.values()]) # output : ['Sachin', 'Tendulkar', 'Batsman', 50]

#Copy dictionary
# 1. Creating reference object of the main dictionary
# In this case new dictionary object is not created instead the new object is created as a reference variable of the
# main dictionary object

alias = dict2
print(dict2)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 50}
print(alias)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 50}

dict2["Age"] = 55
print(dict2)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 55}
print(alias)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 55}

alias["Age"] = 56
print(dict2)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 56}
print(alias)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 56}


# 2. Creating a new variable and storing the dictionary data in the

copyData = dict2.copy()
print(dict2)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 56}
print(copyData)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 56}

dict2["Age"] = 57
print(dict2)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 57}
print(copyData)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 56}

copyData["Age"] = 58
print(dict2)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 57}
print(copyData)  # output : {'FirstName': 'Sachin', 'LastName': 'Tendulkar', 'PlayerType': 'Batsman', 'Age': 58}