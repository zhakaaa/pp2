# Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)   # 2024
print(x.strftime("%A")) # Wednesday
