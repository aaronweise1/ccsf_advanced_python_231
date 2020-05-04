import csv
import json
import sys

data = {}
file = open(sys.argv[1])
reader = csv.DictReader(file)
field = reader.fieldnames
for row in reader:
    id = row['id']
    data[id] = row
j = json.dumps(data, indent=4)
print(j)

# test_file
# id,first_name,last_name,department,salary
# 1,Tim,Marks,Sales,50000
# 2,John,Steward,Customer Service,65000
# 3,Jenny,Laines,Engineering,100000
