import sys
import csv
import json

csv_input = sys.argv[1]
json_output = "output.json"

def convert(input, output):
    csv_rows = []
    with open(input) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
    with open(output, "w") as f:
        f.write(json.dumps(csv_rows, sort_keys=False, indent=4, separators=(',', ': ')))

convert(csv_input,json_output)
print("File " + csv_input + " converted and saved as " + json_output)