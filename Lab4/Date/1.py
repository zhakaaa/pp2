from datetime import timedelta, date
print("Current time: ", date.today())
print("Five day ago: ", date.today() + timedelta(days=-5))