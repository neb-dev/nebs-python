# create a file object
# txt_file = open("fruits.txt")

# fruit = txt_file.read()

# txt_file.close()

# with implicitly closes the file
with open("files/fruits.txt") as txt_file:
    fruit = txt_file.read()

# display file contents
print(fruit)