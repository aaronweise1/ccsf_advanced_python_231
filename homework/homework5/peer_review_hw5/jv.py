import datetime as dt

timestamp_atatime = (line.split(" ")[3][13:] for line in open('/etc/httpd/logs/access_log', "r"))

for _ in range(10):
  list_hr_min_sec = (next(timestamp_atatime)).split(':')
  tdelta_hr_min_sec = dt.timedelta(hours=int(list_hr_min_sec[0]),minutes=int(list_hr_min_sec[1]), seconds=int(list_hr_min_sec[2]))
  print(tdelta_hr_min_sec.seconds) 
