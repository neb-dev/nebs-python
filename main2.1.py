# 3rd party modules
# pip3.9 install pandas
# modules or packages/libraries will be stored in the site-packages dir in the python installation

import time
import os
import pandas

while True:
    with open("files/temps.csv") as file:
        if os.path.exists("files/temps.csv"):
            data = pandas.read_csv("files/temps.csv")
            print(data.mean()) # print(data.mean()["st1"]) will print st1 column mean
        else:
            print("file not found")
        time.sleep(5)

# import pandas
# data = pandas.read_csv("files/temps.csv")
# data = prints view of temps.csv content
# type(data) = <class 'pandas.core.frame.DataFrame'>
# DataFrame is a unique data type to the pandas lib