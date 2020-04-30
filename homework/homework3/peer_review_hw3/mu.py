# CS231 HW#3
# Write a program that demonstrates a generator yielding one timestamp at a time from /etc/httpd/logs/access_log

#Please wait for about 5 minutes or so for the program to run
#Please note that the Try Except below was not strictly necessary since StopIterator is a reasonable flag here but used it here to gracefully exit 

#!/usr/bin/env python3

log = '/etc/httpd/logs/access_log'


timestamps = (line.split(" ")[3].strip('[') for line in open(log))

run = 0
try:
   while True:
      print(next(timestamps))
      run += 1
except StopIteration:
    pass
finally:
    del run
