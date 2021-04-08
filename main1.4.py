# For Loop
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

users = {"Josh": 190229, "Jessica": 181220, "Bailey": 171221}
for user in users.items(): # .keys() .values()
    print(user)

for key, value in users.items():
    print("{}'s user ID is: {}".format(key, value)) # print(f"{key}'s user ID is: {value}")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

phone_numbers = {"John Smith": "+376829299289", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print("{}".format(value.replace("+", "00")))