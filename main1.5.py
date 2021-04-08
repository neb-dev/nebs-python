# While Loop
password = ""
# len(password) <= 8 produces true when 8 characters is entered and therefor will continue to loop
while len(password) < 8: 
    password = input("enter password (must be at least 8 characters): ")
    print(len(password))

# Break/Continue

while True:
    username = input("enter your username: ")
    if len(username) < 6:
        continue
    else:
        break

from datetime import datetime, date, time, timezone

# Datetime
print(datetime.now())