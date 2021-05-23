# df6 = pandas.read_csv("data.txt", header=None) - 0,1,2,3,4,5 row and col headers
# df6.columns = ["ID", "Address", "City", "State", "Zip", "Country"] - custom column headers
# df6.set_index("ID", inplace=True) - inplace modifies current DataFrame
# OR
# df7 = df6.set_index("ID")
# df7 stores modified index to new DataFrame
# df7.set_index("Country", inplace=True, drop=False) - does not drop Name column when updating index to Name column

# Label Based Indexing
# df6.loc["3":"5", "State":"Zip"] - returns range of rows and cols
# df6.loc[1,"Address"] - returns cell
# df6.loc[:, "Address"] all index rows and all Address columns
# list(df6.loc[:, "Address"]) - creates a list of Address column values

# Position Based Indexing
# df6.iloc[1:3, 1:3] - lowerbound exclusive meaning 1st index not included in result
# df6.iloc[:, 1:2] - returns all of the City column (1 = Address, 2 = City) lowerbound Address is not included

# Delete
# df6.drop(1, 0) - deletes first row(0)
# df6.drop("Address", 1) - deletes Address column(1)
# df6.drop(df6.index[0:3], 0) - deletes first 3 rows(0)
# df6.drop(df6.columns[0:2], 1) - deletes first 2 columns(1)

# Add Column
# df6.shape - returns Tuple (#,#) (# of rows, # of columns)
# df6["Time Zone"] = df6.shape[0] * ["Pacific"] - shape[0] returns first value of Tuple (# of rows) * List of value ["Pacific"]
# df6["Time Zone"] = df6["Time Zone"] + " " + "Daylight Time" - updates Time Zone column values

# Add Row
# df6_t = df6.T - swaps headers with index and headers for index (transpose)
# df6_t[7]=["My Address", "My City", "My State", "My Zip", "My Country", "My Timezone"] - add column
# df6 = df6_t.T - swap indexs back to headers and headers back to indexs


