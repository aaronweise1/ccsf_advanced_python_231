#!/usr/bin/env python

name = "/etc/httpd/logs/access_log"

def timestamp(filename):
 while True:
  line = filename.readline().split(" ")[3]	
  yield line

with open(name) as f:
 for i in range(50):
  print(next(timestamp(f)))
