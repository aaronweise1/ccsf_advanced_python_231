"""
Write a CSV-to-JSON translator that expects a CSV file as argument, 
and for each line, prints out a JSON object encapsulating that record
"""

import csv
import json
import sys
from os import path


def validateFilePath(file_path: str) -> bool:
    """
    Checks a file path to make sure it exists.
    """

    return path.exists(file_path)


def convertCSVtoJSON(file_path: str) -> None:
    """
    Converts each line of a CSV file to a JSON and prints it out
    """
    
    if not validateFilePath(file_path):
        print('File path does not exist. Please pass a csv file in.')
        return
    
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(json.dumps(row, indent=4))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No file paths provided.')
    else:
        convertCSVtoJSON(sys.argv[1])