# Write a generator that calculates the number of seconds since midnight 
# for events in access_log, and show the first ten when the program is run
#
# NOTE: There seemed to be some ambiguity in the discussion forum as to what 
# 'midnight' is supposed to represent in the prompt. I'm making the assumption 
# that midnight represents the most recent midnight that has occurred (i.e., if
# it's 5am on March 7th, the most recent midnight will be 12am on March 7th)
# and calculating the time in seconds from the event log timestamp.

import re
import datetime


def genSecondsSinceMidnight(access_log):
    log_file = open(access_log, 'r')
    timestamps = getTimestamp(log_file)
    for i in range(10):
        print(computeTimeSinceMidnight(next(timestamps)))
    log_file.close()


def getTimestamp(log_file):
    for line in log_file:
        yield extractTimeFromLine(line)


def extractTimeFromLine(line):
    regex_time = re.search('(\d+)\/(\w+)\/(\d+):(\d+):(\d+):(\d+)', line)
    time_format = '%d/%b/%Y:%H:%M:%S'
    time = datetime.datetime.strptime(regex_time.group(0), time_format)
    return time

# @desc 'midnight' is represented as the most recent midnight
# that has occurred (i.e., if it's 5am on March 7th, the most 
# recent midnight will be 12am on March 7th)
def computeTimeSinceMidnight(time):
    midnight = datetime.datetime.now().replace(
        hour = 0, 
        minute = 0,
        second = 0, 
        )
    return (midnight - time).total_seconds()


access_log = '/etc/httpd/logs/access_log'
genSecondsSinceMidnight(access_log)