""" 
Write a CSV-to-JSON translator that expects a CSV file as argument, and for each line,
prints out a JSON object encapsulating that record
"""

import csv, json, io, sys

if len(sys.argv) < 2:
    print("Please pass a .csv file on the command line.")
    sys.exit (1)
else:
    with io.open(sys.argv[1], "r", encoding='utf-8-sig') as csvfile:
    # practice version
    # with io.open("Miles_Of_Streets.csv", "r", encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(json.dumps(row, indent=4))
        

