from datetime import datetime, time

generator = (line.split(" ")[3].lstrip("[") for line in open('/etc/httpd/logs/access_log'))

def calculateseconds():
   while True:
      tm = datetime.strptime(next(generator), "%d/%b/%Y:%H:%M:%S").time()
      seconds = tm.hour * 3600 + tm.minute * 60 + tm.second
      yield seconds

for i in range(10):
   print(next(calculateseconds()))

