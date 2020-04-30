#!/usr/local/bin/python3
# Course   : CS 231 
# Homework : 12
# Due date  :  April 26, 2020
# Filename: hw12.py

"""
 Write a program that creates a pool of workers to all at once check whether or not the files whose pathnames are passed in are encoded in UTF-8
"""

import concurrent.futures
import sys
import codecs

 # check whether the pathname to files passed are encoded in UTF-8?
def isUTF8(pathname):
	try:	# Valid utf-8
		codecs.open(pathname, encoding='utf-8', errors='strict').readlines()
		print(pathname + ": \tValid utf-8")
	except UnicodeDecodeError:	# Invalid utf-8
		print(pathname + ": \tInvalid utf-8")

# list of pathnames from command line arguments
list_filename = sys.argv[1:]

pool = concurrent.futures.ThreadPoolExecutor()

if __name__=="__main__" :
	if len(sys.argv) < 2:	# no pathname provided
		print("Error! Please provide pathnames to files." +
		   	"\nExiting now.")
	else:	 # there are pathname provided
		print("RUNNING.........")
		pool.map(isUTF8,list_filename)