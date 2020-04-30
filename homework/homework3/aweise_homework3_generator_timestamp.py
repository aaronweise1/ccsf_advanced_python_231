import re

def extractTimeFromLine(line):
    return re.search('(\[.+\])(\s)',line).group(0)

def getTimestamp(log_file):
    for line in log_file:
        yield extractTimeFromLine(line)

def getAllTimestamps():
    log_file = open('/etc/httpd/logs/access_log','r')
    
    # @desc for loop - would normally loop through the whole file, but it would take too long.
    # Iterating through the first 100 below to demonstrate yielding one timestamp at a time
    # for time in getTimestamp(log_file):
    #     print(time)
    
    i = 0
    while i < 100:
        print(next(getTimestamp(log_file)))
        i += 1
    log_file.close


getAllTimestamps()