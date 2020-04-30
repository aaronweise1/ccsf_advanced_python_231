from datetime import timedelta, datetime, date, time
def readfile ():
   log = '/etc/httpd/logs/access_log'
   for line in open(log, "r"):
       EventStamp = line.split(" ")[3].split("[")[1].replace(":", " ", 1)
       dateTime = datetime.strptime(EventStamp, '%d/%b/%Y %I:%M:%S')
       Event = datetime.strptime(EventStamp, '%d/%b/%Y %I:%M:%S').time()
       EventDelta = timedelta(hours=Event.hour,minutes=Event.minute,seconds=Event.second)
       yield str( int(EventDelta.total_seconds()) ) + "          " + str(Event)

event = readfile()
print ("The first 10 total seconds of the events in the acces_log: ")
for index in range (10):
   print (next(event))
