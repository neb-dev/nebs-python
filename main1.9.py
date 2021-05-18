# create a file object
# txt_file = open("fruits.txt")

# fruit = txt_file.read()

# txt_file.close()

# with implicitly closes the file
with open("files/fruits.txt") as fruit_file:
    fruit = fruit_file.read()

# display file contents
print(fruit)

with open("files/vegetables.txt", "w") as veg_file:
    veg = veg_file.write("tomato\ncucumber\nonion")

print(veg)