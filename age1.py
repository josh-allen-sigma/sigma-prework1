from datetime import datetime
input_date_str = "2020-09-01"
input_date = datetime.strptime(input_date_str + " 00:00", "%Y-%m-%d %H:%M")
current_date = datetime.now()
time_difference = current_date - input_date
yearsans = int(time_difference.total_seconds()//(60*60*24*365))
print(yearsans)
