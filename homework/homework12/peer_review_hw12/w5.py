#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
'''
Assignment: Write a program that creates a pool of workers
to all at once check whether or not the files
whose pathnames are passed in are encoded in UTF-8
Approach:
a)define a function that find & print the encode type of a given file
b) run a pool of  concurrent workers that check all files at once
'''
import concurrent.futures
#list path to files
import time
from multiprocessing.pool import Pool
#define the files
f1="/users/abrick/resources/english"
f2="/etc/httpd/logs/access_log" 
f3="/users/abrick/resources/american-english-insane-ascii"
f4="/users/abrick/resources/american-english-small"
lst=[f1, f2, f3, f4]
#define a function finding encoding
def isencoded(pth):
    try:
        f = open(pth)
        print("Encoding:"+repr(f)) # find encoding & print it
    except :
        print("An error occured for file"+pth)
        pass
    finally:
       f.close()



#define a pool of workers as much as needed
pool = concurrent.futures.ThreadPoolExecutor(max_workers=len(lst))
#map the pool to the function isencoded
print(list(pool.map(isencoded, lst)))


