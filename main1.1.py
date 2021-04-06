seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)
print(seconds)

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)

# Index
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

# Slice
temperatures = [90.9, 88.5, 88, 92.7, 99]
print(temperatures[0:2])
print(temperatures[:2])
print(temperatures[3:5])
print(temperatures[3:])

# Negative Indexes
print(temperatures[-1])
print(temperatures[-5])
print(temperatures[-2:])
print(temperatures[-4:-2])
print(temperatures[:-1])

# String Indexes
name = "Norque"
print(name[1])

# Chain Index
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week[-3][0])

names = ["Joshua", "Jessica", "Bailey"][-2][-1]
print(names)

# Dictionary Indexes
last_names = {"Matt": "Smith", "Joann": "Richardson", "Mike": "McDonald"}
print(last_names["Matt"])

# Converting Data Types
# Tuple to List
tuple_data = (1, 2, 3)
tuple_to_list = list(tuple_data)
print(tuple_to_list)

# List to Tuple
list_data = [1.4, 2, 3.3]
list_to_tuple = tuple(list_data)
print(list_to_tuple)

# List to Dictionary
list_of_lists = [["Gregory", "Paladin"], ["Bekenar", "Cryptlord"]]
list_to_dictionary = dict(list_of_lists)
print(list_to_dictionary)