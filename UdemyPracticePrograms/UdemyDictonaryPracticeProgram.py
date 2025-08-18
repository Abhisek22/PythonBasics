#Understanding Dictionaries
#1. Create a dictionary named car with the following keys:
# make, model, year, and color. Assign appropriate values to each key.
#   "make": "Toyota",
#    "model": "Camry",
#    "year": 2020,
#    "color": "Blue"
#2. Print the value associated with the model key.
#3. Add a new key called owner and assign it the name "Rahul".
#4. Print the entire dictionary.

car = {"make": "Toyota", "model": "Camry", "year": 2020, "color": "Blue"}
print("Car model: "+car["model"])
car["owner"] = "Rahul"
print(f"Updated car dictionary: {car}")