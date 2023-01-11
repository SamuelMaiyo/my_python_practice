# Dictionary: Key-value pair, Unordered, Mutable
mydict = {"name": "Max", "Age": 28, "City": "Ohio"}
print(mydict)

mydict_2 = dict(Name ="Mary", age = 26, City = "Boston")

value = mydict["name"]
print(value)

# Mutable
mydict["email"] = "max@gmail.com"
print(mydict)

# Delete items
del mydict["City"]
print(mydict)

mydict.pop("Age")
print(mydict)

mydict.popitem()
print(mydict)

#Check if key is in Dictionary
mydict_3 = dict(name ="Ted", age = 22, city = "New York")

if "name" in mydict_3:
    print(mydict_3["name"])

try:
    print(mydict_3["nime"])
except:
    print("Error")

# Looping
for key in mydict_3.keys():
    print(key)

for value in mydict_3.values():
    print(value)

for key, value in mydict_3.items():
    print(key, value)

# Copy a dictionary
mydict_3_cpy = mydict_3
print(mydict_3_cpy)

mydict_3_cpy["email"] = "ted@xyz.com"
print(mydict_3_cpy)
print(mydict_3)

mydict_3_cpy = mydict_3.copy()
mydict_3_cpy["Adress"] = "00100"
print(mydict_3_cpy)
print(mydict_3)

mydict_3_cpy = dict(mydict_3)
mydict_3_cpy["Gender"] = "Male"
print(mydict_3_cpy)
print(mydict_3)

# Merge 2 dictionaries
dict_1 = {"Name": "Max", "Age": 28, "Email": "max@xyz.com"}
dict_2 = dict(Name ="Mary", Age = 26, City = "Boston")

dict_1.update(dict_2)
print(dict_1)
print(dict_2)

# Using numbers as keys
dict_3 = {3: 9, 6: 36, 9: 81}
print(dict_3)

value = dict_3[3]
print(value)

# Use tuple as key

my_tuple = (8, 7)
dict_4 = {my_tuple: 15}
print(dict_4)