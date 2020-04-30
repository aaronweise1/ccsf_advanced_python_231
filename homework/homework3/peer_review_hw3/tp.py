# here, timestamp is considered as a date + time of an event if you wnat to get only time, change slice from [1::] to [13::]


timestamp_atatime = (line.split(" ")[3][1::] for line in open('/etc/httpd/logs/access_log', "r"))

for _ in range(10):
  print (next(timestamp_atatime))
