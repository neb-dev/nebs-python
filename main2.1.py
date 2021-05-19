# 3rd party modules
# pip3.9 install pandas
# modules or packages/libraries will be stored in the site-packages dir in the python installation

import time
import os
import pandas

while True:
    with open("files/temps.txt") as file:
        if os.path.exists("files/temps.txt"):
            print(file.read())
        else:
            print("file not found")
        time.sleep(5)
