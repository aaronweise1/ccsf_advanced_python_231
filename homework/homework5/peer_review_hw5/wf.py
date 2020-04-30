event_time = (line.split(" ")[3][13::] for line in open('/etc/httpd/logs/access_log', "r"))


for _ in range(10):
  print (next(event_time))
