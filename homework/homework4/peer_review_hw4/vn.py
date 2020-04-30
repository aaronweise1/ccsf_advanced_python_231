#############################################################
#  CS231  Lab 4                                             #
#  Use textwrap, yield and generator ---                    #
#  -Write a program to lazily rewrap text from the filename #
#  passed so it fits an 80 column per line without breaking #
#  any words. Use generator yields the next lines of text   #
#                                                           #
#  Student Name:      James Lin  JamesLin288@gmail.com      #
#  Instructor Name:   Aaron Brick  ABrick@ccsf.edu          #
#############################################################
import os
import textwrap
import sys
import select

def file_reader():
   if (len(sys.argv) > 1):
      fileName = open(sys.argv[1], 'r').readlines()
      fileName = (' '.join(fileName))
#      fileSize = int(os.path.getsize(sys.argv[0]))/80  //calculates the size and know how many lines
   else:
      dirList = os.listdir("./")
      inputName = input("Please enter the name of the text file to be used: ")
      fileName = open(inputName, 'r').readlines()
      fileName = (' '.join(fileName))
#      fileSize = int(os.path.getsize(fileName))/80     // not able to get file size back to the main
   wrapper = textwrap.TextWrapper(width=80)
   word_list = wrapper.wrap(text=fileName)
#   fileWrap = textwrap.fill(fileName, width=80)    // fill- will create one single long line
   for line in word_list:
       yield line

lineGenerator = file_reader()
print (next(lineGenerator))
print (next(lineGenerator))

#print(sys.argv[0])
#print(int(os.path.getsize(sys.argv[0]))/80)
#print(sys.argv[1])
#print(int(os.path.getsize(sys.argv[1])/80))
#print(fileSize)
print ("Following is the wrapped file printed line by line: ")
for i in range (5):
    print (next(lineGenerator)) 

#############   Following is the sample output  ##############
#[jlin199@hills ~]$ python3 CS231Lab4WrapYield.py wraptest.txt
#This function wraps the input paragraph such that each line   in the paragraph
#is at most width characters long. The wrap method   returns a list of output
#Following is the wrapped file printed line by line: 
#lines. The returned list   is empty if the wrapped output has no content.  This
#function wraps the input paragraph such that each line  in the paragraph is at
#most width characters long. The wrap method  returns a list of output lines. The
#returned list  is empty if the wrapped output has no content.  This function
#wraps the input paragraph such that each line  in the paragraph is at most width

#[jlin199@hills ~]$ more wraptest.txt                <<=== original test file 
#This function wraps the input paragraph such that each line 
#in the paragraph is at most width characters long. The wrap method 
#returns a list of output lines. The returned list 
#is empty if the wrapped output has no content.
#This function wraps the input paragraph such that each line
#in the paragraph is at most width characters long. The wrap method
#returns a list of output lines. The returned list
#is empty if the wrapped output has no content.
#This function wraps the input paragraph such that each line
#in the paragraph is at most width characters long. The wrap method
#returns a list of output lines. The returned list
#is empty if the wrapped output has no content.

#[jlin199@hills ~]$ python3 CS231Lab4WrapYield.py 
#Please enter the name of the text file to be used: wraptest.txt
#This function wraps the input paragraph such that each line   in the paragraph
#is at most width characters long. The wrap method   returns a list of output
#Following is the wrapped file printed line by line: 
#lines. The returned list   is empty if the wrapped output has no content.  This
#function wraps the input paragraph such that each line  in the paragraph is at
#most width characters long. The wrap method  returns a list of output lines. The
#returned list  is empty if the wrapped output has no content.  This function
#wraps the input paragraph such that each line  in the paragraph is at most width

#[jlin199@hills ~]$ 
########## End of sample output   ###################
