# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:e

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))  # June