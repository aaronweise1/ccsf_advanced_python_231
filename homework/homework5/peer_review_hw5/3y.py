import time
from datetime import datetime

time_list = []

with open('/etc/httpd/logs/access_log') as f: #open the file for reading
    for line in f.readlines()[0:10]: #traverse each line out of the top 10 lines
        time_list.append(line.split()[3][1:21]) #first we split the line and then choose the datetime element
        print(time_list)

seconds_since_midnight=[] #an empty list initialized to store the time difference in seconds
for i in time_list: #iterate the lsit of datetimes we had extracted earlier
    sec = (datetime.strptime(i,'%d/%b/%Y:%H:%M:%S') - datetime.strptime(i,'%d/%b/%Y:%H:%M:%S').replace(hour=0, minute=0, second=0, microsecond=0))
    seconds_since_midnight.append(sec.seconds) #append the difference in seconds to the list
print(seconds_since_midnight)


