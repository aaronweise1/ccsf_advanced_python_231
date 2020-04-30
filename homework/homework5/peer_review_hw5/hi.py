############################################################
#  CS231  Lab 5                                             #
#  Use yield and generator to timedelta datetime to seconds #
#  Write a generator that calculates the number of seconds  #
#  since midnight for events in /etc/httpd/logs/access_log  #
#                                                           #
#  Student Name:      James Lin  JamesLin288@gmail.com      #
#  Instructor Name:   Aaron Brick  uABrick@tccsf.edu          #
#############################################################

from datetime import timedelta, datetime, date, time, timezone

def csv_reader():
   logName = '/etc/httpd/logs/access_log'
   for line in open(logName, "r"):
#       pos = line.split(" ")[3].split("[")[1].find(":", 11,13)
       TimeStamp = line.split(" ")[3].split("[")[1].replace(":", " ", 1)
       Date = datetime.strptime(TimeStamp, '%d/%b/%Y %I:%M:%S').date()
       dateTime = datetime.strptime(TimeStamp, '%d/%b/%Y %I:%M:%S')
       Time = datetime.strptime(TimeStamp, '%d/%b/%Y %I:%M:%S').time()
       TotalSeconds = Time.hour *60*60 + Time.minute *60 + Time.second   
# above is to double check the total seconds vs. below 
       TimeDelta = timedelta(hours=Time.hour,minutes=Time.minute,seconds=Time.second)
       yield "Total Seconds = " + str( int(TimeDelta.total_seconds()) ) + "         =====>         Time = " + str(Time)

generator = csv_reader()
print ("Followding is the total seconds for each event retrieved from the log file: ")
for i in range (10):
   print (next(generator))


#############   Following is the sample output  ##############
#@hills ~]$ python3 CS231ToSecLab5.py 
#Followding is the total seconds for each event retrieved from the log file: 
#Total Seconds = 34560         =====>         Time = 09:36:00
#Total Seconds = 34560         =====>         Time = 09:36:00
#Total Seconds = 34561         =====>         Time = 09:36:01
#Total Seconds = 34696         =====>         Time = 09:38:16
#Total Seconds = 34697         =====>         Time = 09:38:17
#Total Seconds = 34698         =====>         Time = 09:38:18
#Total Seconds = 34739         =====>         Time = 09:38:59
#Total Seconds = 34947         =====>         Time = 09:42:27
#Total Seconds = 34948         =====>         Time = 09:42:28
#Total Seconds = 34948         =====>         Time = 09:42:28
#@hills ~]$ 
########## End of sample output   ###################
