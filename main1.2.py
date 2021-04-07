# Functions
def mean(value):
    # Conditionals
    if type(value) == dict:
        result = sum(value.values()) / len(value)
    elif type(value) == list:
        result = sum(value) / len(value)
    else:
        return print("invalid data type")
        
    return result

print(type(sum), type(mean))

my_list = [10, 100, 1000]
print(mean(my_list))

# result example sum(my_dictionary.values()) / len(my_dictionary)
my_dictionary = {"Josh": 20, "Jessica": 200, "Bailey": 2000}
print(mean(my_dictionary))

my_tuple = (30, 300, 3000)
print(mean(my_tuple))

x = 1
y = 1

# AND
if x == 1 and y == 1:
    print("Yes AND")
else:
    print("No AND")

# OR
if x == 1 or y == 2:
    print("Yes OR")
else:
    print("No OR")

# IN
def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))

# isinstance
x = "1"
if isinstance(x, int) or isinstance(x, float) or x == "1":
    print("Valid type!")
else:
    print("Not valid!")