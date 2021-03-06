#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
# Write a program that demonstrates a generator yielding one timestamp at a time from /etc/httpd/logs/access_log
import re
from timeit import default_timer as timer
#give the path of the file
log = '/etc/httpd/logs/access_log'
nb = 10000 #fix the number of lines to scan
ct = 0 #create a counter for the number of timestamps found
start3 =timer() #note the start time
gen =(line for line in   open(log)) #create a generator for reading the line of the file
#use the generator to go line by line up to nb lines
while ct < nb:
    #search the time stamp which is in the 1st brackets [] using regex in the next line of the generator
    match = re.search('\[(.*?)\]', next(gen))
    if  match is not None:
        print(match.group(1)) #if  found it print it
        ct = ct + 1   #increase counter by 1
    else :
        break #stop no more lines
#at the end print the number of lines/timestamps shown and the processing time taken
end3 =timer()
pt = (end3 - start3) #this is the running time in seconds
print()
print(f" {ct} timestamps shown in {pt} seconds\n")