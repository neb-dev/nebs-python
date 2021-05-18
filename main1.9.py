# create a file object
txt_file = open("files/fruits.txt")

# read file
fruit = txt_file.read()

# print content
print(fruit)

# close file object
txt_file.close()


# with implicitly closes the file
with open("files/fruits.txt") as fruit_file:
    # pass an int to the read function to read a specific number of chars
    fruit = fruit_file.read()

# display file contents
# print(fruit)

# open parameter "w" means write (r or read is default)
with open("files/vegetables.txt", "w") as veg_file:
    veg = veg_file.write("tomato\ncucumber\nonion")

# print(veg)


# function that counts the occurance of a char in a text file - c is char / f is filepath
def char_in_file(c, f):
    with open(f) as txt_file:
        content = txt_file.read()
        res = content.count(c)
        return res

print(char_in_file("a", "files/bears.txt"))

with open("files/bears.txt") as file:
    # content = file.read(90)
    content = file.read()

with open("files/first.txt", "w") as file:
    file.write(content[:90])
