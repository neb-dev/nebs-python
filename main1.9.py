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

# x creates new file but does not add to existing
# a appends to an existing file
# + allows for appending to a file (read and write)
with open("files/vegetables.txt", "a+") as veg_file:
    veg_file.write("\nokra")
    # place cursor at start of file, otherwise result will print nothing due to the cursor being at the end of the file
    veg_file.seek(0)
    result = veg_file.read()

print(result)


# function that counts the occurance of a char in a text file - c is char / f is filepath
def char_in_file(c, f):
    with open(f) as txt_file:
        content = txt_file.read()
        res = content.count(c)
        return res

# print(char_in_file("a", "files/bears.txt"))

with open("files/bears.txt") as file:
    # content = file.read(90)
    content = file.read()

with open("files/first.txt", "w") as file:
    file.write(content[:90])

# append own content to file
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)
