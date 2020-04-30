# CS231
# Assignment# 12
# Write a program that creates a pool of workers to all at once
# check whether or not the files whose pathnames are passed in are encoded in UTF-8
import unicodedata
import sys
import concurrent.futures

filepath = sys.argv[1]
lines = open(filepath).readlines()

def checkcoding(str):
    try:
        str.encode(encoding='utf-8', errors='strict')
        print("content is UTF-8")
    except UnicodeError:
        print("content is not UTF-8")

pool = concurrent.futures.ThreadPoolExecutor()

print(list(pool.map(checkcoding,lines)),
      list(zip(lines,pool.map(checkcoding,lines))))
