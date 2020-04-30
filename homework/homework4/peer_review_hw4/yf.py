"""
Write a program to lazily rewrap text from the filename passed so that it fits an 80
column window without breaking any words. Use a generator that yields the next lines of
text, each containing as many words as possible


I ran out of time on this assingment.  I missed the point about reading a line and 
instead went for the approach of reading words.  Then couldn't figure out how to assemble
them properly.

"""



# have to import sys to read the arguments passed
import sys
import re
import textwrap 
# filename passed would be in one-th position
file = sys.argv[1]
text = open(file)

# generator function
def readtext():
    for line in text.readlines():
        for word in re.split(r'\s+', line):
            yield word

words = readtext()

# just printing 100 as a test, no need to print a full document
# this doesn't yet work.  I haven't figured out how to keep the words 
# on the same line until I reach the width of 80.
for _ in range(100):
     print(textwrap.fill(next(words), width=80))
     