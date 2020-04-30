import textwrap
import sys
#one liner
data = sys.argv[1]
tw = (textwrap.fill(line.replace("/"," "), width=80) for line in open(data,'r'))

for i in tw:
    print (i)

# Alternative (expand logic):
# data = sys.argv[1]
# def textwraper(data,width=80):
#     f = open(data,'rb')
#     for line in f:
#         print line
#         new_line = line.replace("/"," ")
#         yield (textwrap.fill(new_line, width))
#     f.close()
#
# for x in textwraper(data,width=80):
#     print (x)
