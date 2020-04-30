from datetime import datetime


def Timestamp():
    temp = []
    log = '/etc/httpd/logs/access_log'
    read_file = open(log, 'r')
    start_time = datetime.now()
    for line in read_file:
        temp.append(line.strip())
    end_time = datetime.now()
    d = end_time - start_time
    yield 'Start Time: {}\nEnd Time: {}\nRun Time: {}\n'.format(start_time, end_time, d)


for time in Timestamp():
    print(time)
