

log = '/etc/httpd/logs/access_log' #extracting the timestamps

timestamp = (line.split("-07")[0] for line in open(log)) #isolating the timestamp from the rest of the string 

def my_gen(timestamp): #building a generator
    n = 0
    print("Here come the next timestamp after the IP address:")
    yield 
    next(timestamp)

    n +=1
    print("Here come the next timestamp after the IP address:")
    yield
    next(timestamp)

    n +=1
    print("Here come the next timestamp after the IP address:")
    yield
    next(timestamp)
  
for n in timestamp:
 print(next(timestamp)) #yielding timestamps

# the only way for me to show successive timestamps was to print in batches of more than one, hence did not print one at a time.


