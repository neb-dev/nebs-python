# create a file object
txt_file = open("fruits.txt")

fruit = txt_file.read()

txt_file.close()

# display file contents
print(fruit)