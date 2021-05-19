# Built In Modules
# import sys
# sys.builtin_module_names
import time

while True:
    with open("files/vegetables.txt") as file:
        print(file.read())
        time.sleep(5)