#!/usr/local/bin/python3
# Course   : CS 231 
# Homework : 3
# Due date  :  February 23, 2020
# Filename: hw3.py

"""
Write a program that demonstrates a generator yielding one timestamp at a time from /etc/httpd/logs/access_log
"""

def timestamp_generator():
	log_file = open('/etc/httpd/logs/access_log', 'r').readlines()
	for line in log_file:
		parts = line.split()
		# where the timestamp in the line
		outcome=parts[3:4]
		if (outcome is not None):
			# format the outcome not within [] and without the "[" in the beginning
			yield(" ".join(map(str, outcome)).replace("[", ""))



# create new generator
timestamp= timestamp_generator()

# demonstrate use of next()
# print the first timestamp of the file
print(next(timestamp_generator()))
# print the second timestamp of the file
print(next(timestamp_generator()))
# print the third timestamp of the file
print(next(timestamp_generator()))
# print the fourth timestamp of the file
print(next(timestamp_generator()))

# print/exhaust the rest of the timestamp of the file from the generator
# for value in timestamp:
# 	print(value)

