import datetime
from datetime import datetime, timedelta
import re


ts = (line[line.find("[")+1 : line.find(" -0700")] for line in open('/etc/httpd/logs/access_log','r'))

for i in ts:
    hr = int(i[12:14])
    min = int(i[15:17])
    sec = int(i[18:20])
    total_sec = 60*60*hr + 60*min + sec
    print (total_sec)
