#CS231
#Assignment 4

#Write a program to lazily rewrap text from the filename passed 
#so that it fits an 80 column window without breaking any words. 
#Use a generator that yields the next lines of text, each containing 
#as many words as possible 

import re
import sys

def wrap(s): #use regex and .join to wrap the text within 80 characters without breaking words
    linewrap = "\n".join(line.strip() for line in re.findall(r'.{1,80}(?:\s+|$)', s))
    yield linewrap

f = open(sys.argv[1], 'r')

for line in f:
    result = wrap(line)
    print(next(result))

f.close()
