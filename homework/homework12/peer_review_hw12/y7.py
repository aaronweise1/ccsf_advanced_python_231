# -*- coding: utf-8 -*-
"""
Created on Apr 23 23:36:31 2020   @author: Mary Liu
Write a program that creates a pool of workers to all at once check whether
or not the files whose pathnames are passed in are encoded in UTF-8
"""

import concurrent.futures

def check_encode_ascii(p):
    #check if encode ascii works and return the path
    try:   
        p1 = p.encode('ascii', 'strict')
        p1.decode('ascii', 'strict')
        return p   
    except UnicodeEncodeError:
        pass
    else:
        return None 

def check_encode_utf8(p):
    #encoding with ascii works will return None
    #check if encoding utf-8 works and return the path
    try:
        p1 = p.encode('ascii', 'strict')
        p1.decode('ascii', 'strict')    
    except UnicodeEncodeError:
        p1 = p.encode('utf-8', 'strict')
        p1.decode('utf-8', 'strict')
        return p
    else:
        return None
    
paths=["/usr/bin", "/usr/local/möre", "/möre/var/tmp", "/this/is/a/test", "/你/好", "/my/direct"]
       
pool = concurrent.futures.ThreadPoolExecutor()

print("The following directories are encoded in ascii:")
results_ascii = pool.map(check_encode_ascii, paths)
for i in results_ascii:
    if i != None:
        print(i)
print()        
print("The following directories are encoded in utf-8:")
results_utf8 = pool.map(check_encode_utf8, paths)
for i in results_utf8:
    if i != None:
        print(i)

        
