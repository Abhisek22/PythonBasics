str = "Abhisek Ghosh"

print(str) # Output : Abhisek Ghosh

print(str[2]) # Output : h

print(str[0:7]) # Output : Abhisek

str2 = " Quality Analyst"
newstr = str+str2
print(newstr) # Output : Abhisek Ghosh Quality Analyst

str3 = "Ghosh"

print(str3 in str) # Output : True
print(str in str2) # Output : False

newVar = newstr.split(" ")
print(newVar) # Output : ['Abhisek', 'Ghosh', 'Quality', 'Analyst']

str4 = "  Great  "
str5 = "  War  "
print(str4.strip()+str5.strip())  # Output : GreatWar
print(str4.lstrip())  # Output : Great
print(str5.rstrip())  # Output :   War
