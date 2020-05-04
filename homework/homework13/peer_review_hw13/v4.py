#############################################################
#  CS231  Lab 14                                            #
#  Convert CSV to JSON - JavaScript Object Node             #
#  -Write a program to translate any CSV file to JSON file  #
#  passed in comma seperate lines and translate each line   #
#  to JavaScript Oject                                      #
#                                                           #
#  Student Name:      James Lin  JamesLin288@gmail.com      #
#  Instructor Name:   Aaron Brick  ABrick@ccsf.edu          #
#############################################################
import os
import textwrap
import sys
import select
import csv, json

def file_reader():
   if (len(sys.argv) > 1):
      CSVFile = open(sys.argv[1], 'r').readlines()
      JsonFile = open('JsonOut.json', 'w')
      inputName = sys.argv[1]
   else:
      dirList = os.listdir("./")
      inputName = input("Please enter the name of the text file to be used: ")
      CSVFile = open(inputName, 'r').readlines()
      JsonFile = open('JsonOut.json', 'w')
   reader = csv.DictReader(CSVFile)
   for row in reader:
       JsonDump = json.dump(row, JsonFile)
       JsonFile.write('\n')
#       print (row)    <-- uncomment
#   JsonFile = open('JsonDumps.json', 'w') 
#   y = json.dumps(reader,JsonFile)
#   print(y)

   return inputName

CsvJsonFile = file_reader()
print("In Your Current Working Directory: ")
os.system('pwd')
print("The File JsonOut.json Contains The Following Data: ")
os.system('more JsonOut.json')
#ComJsonFile = open('ComJsonOut.json', 'w')
#dumpsJsonFile = open('dumpsJsonOut.json','w')    <-- uncomment

#json_data = [json.dump(d, ComJsonFile) for d in csv.DictReader(open(CsvJsonFile))]
#json_data = [ComJsonFile.write(json.dumps(d, ComJsonFile)) for d in csv.DictReader(open(CsvJsonFile))]
#json_data = [print(json.dumps(d, ComJsonFile)) for d in csv.DictReader(open(CsvJsonFile))]
print ("+++++++++++++++++++++++++")
print ("Live -- screen print again:  ")
json_data = [print(json.dumps(d)) for d in csv.DictReader(open(CsvJsonFile))]
#json_data = [print(json.dump(d, ComJsonFile)) for d in csv.DictReader(open(CsvJsonFile))]
#json_dump = [dumpsJsonFile.write(json.dumps(d, dumpsJsonFile) +'\n') for d in csv.DictReader(open(CsvJsonFile))]  <-- uncomment


