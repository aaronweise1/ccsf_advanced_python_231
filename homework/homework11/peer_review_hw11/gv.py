# example command should be in the format
# please try running:
# python3 hw11.py echo hi
import sys
import os

print ('There are ', len(sys.argv), 'items in sys argv.')
print ('which are:', str(sys.argv))
print('Path is ', str(sys.argv[1]))
arguments = ' '.join(sys.argv[2:])
print('Argument(s) is(are) ', arguments)

command = sys.argv[1]+' '+sys.argv[2]
os.system(command)
