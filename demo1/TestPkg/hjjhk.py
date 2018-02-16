import datetime

from datetime import timedelta

string_date = "20/Jan/2018"

str_name = datetime.datetime.strptime(string_date, "%d/%b/%Y")
print str_name



k = datetime.datetime.now() - timedelta(hours=3,minutes=15,microseconds=60)
start_day = str(k.day)
print k.strftime("%d/%b/%y")



