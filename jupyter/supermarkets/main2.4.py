# df6 = pandas.read_csv("data.txt", header=None) - 0,1,2,3,4,5 row and col headers
# df6.columns = ["ID", "Address", "City", "State", "Zip", "Country"] - custom column headers
# df6.set_index("ID", inplace=True) - inplace modifies current DataFrame
# OR
# df7 = df6.set_index("ID")
# df7 stores modified index to new DataFrame
# df7.set_index("Name", inplace=True, drop=False) - does not drop Name column when updating index to Name column