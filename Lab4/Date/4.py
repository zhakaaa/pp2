from datetime import datetime, timedelta, date

today = datetime.now()

tomorrow = datetime.now() + timedelta(days=+1,hours=+4,minutes=+10)

difference = tomorrow - today

seconds = difference.total_seconds()

print(f"First date: {today} \n Second date: {tomorrow} \n Difference in seconds : {seconds}")