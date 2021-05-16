# create a file object
# txt_file = open("fruits.txt")

# fruit = txt_file.read()

# txt_file.close()

# with
with open("fruits.txt") as txt_file:
    fruit = txt_file.read()

# display file contents
print(fruit)