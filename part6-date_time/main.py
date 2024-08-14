# Date and time in Python

import datetime as dt

# Get current date and time
today = dt.date.today()
print(today)

# Manually create a date
my_birthday = dt.date(1990, 1, 1)
print(my_birthday)

# Show day
print(f"{my_birthday:%A}")
