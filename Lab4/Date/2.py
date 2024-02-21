from datetime import timedelta, date
print("Yesterday: ", date.today() + timedelta(days=-1))
print("Today: ", date.today())
print("Tomorrow: ", date.today() + timedelta(days=+1))