# CS231
# Assignment# 13
# Write a CSV-to-JSON translator that expects a CSV file as argument,
# and for each line, prints out a JSON object encapsulating that record

import sys
import csv
import json

def printjson(path):
    csvfile = open(path, 'r')
    csvreader = csv.reader(csvfile) # Return a reader object which will iterate over lines in the given csv file.
    fieldnames = next(csvreader)  # Return a list of fields from cvs reader object ; assume csv first row contains the header
    reader = csv.DictReader(csvfile, fieldnames)    # Create an reader object that maps each row to a dict which the field names
    # Print one json object each line
    for row in reader:
        object = json.dumps(row)
        print(object)


args = sys.argv[1:]

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Please provide the path of the csv file.")
    else:
        filepath = sys.argv[1]  # Set the file path
        printjson(filepath)

