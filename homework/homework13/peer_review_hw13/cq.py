# To test this program run python3 this_file your_file.csv

import sys 
import csv 
import json

def translate_csv_to_json(input_file_csv, output_file_json):

    data = []
    with open(input_file_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temr_dict = dict(row)
            data.append(temr_dict)
            print(temr_dict)

    with open(output_file_json, 'w') as json_file:
      json_file.write(json.dumps(data, indent=4))

if __name__ == "__main__":
  if len(sys.argv) > 1:
      input_file_csv = sys.argv[1]
      output_file_json = f"{input_file_csv.split('.')[0]}.json"
      translate_csv_to_json(input_file_csv, output_file_json)

  print(__name__)
