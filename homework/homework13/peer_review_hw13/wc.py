#!/usr/bin/python
# yesona mata
# python programname csvfile
# program converts each row in csvfile to a json object and prints it.


import sys 
import json
import csv

def csv2json(document):
	with open(document) as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			print(json.dumps(row,indent=4))

if __name__ == "__main__":
        csv2json(sys.argv[1])