# Built In Modules
# import sys
# sys.builtin_module_names
import time
import os

while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as file:
            print(file.read())
    else:
        print("file not found")
    time.sleep(5)

# os modules
# import os
# sys.prefix
# open /Library/Frameworks/Python.framework/Versions/3.9
# dir > python3.9 > os.py
# dir(os)
# os.path.exists("files/vegetables.txt") = True