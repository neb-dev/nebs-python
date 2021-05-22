# pip3.9 install mysql-connector-python
import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

input_word = input("enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % input_word)

res = cursor.fetchall()

if res:
    for definition in res:
        print(definition[1])
else:
    print("word not found")