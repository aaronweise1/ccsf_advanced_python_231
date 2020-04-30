#!/usr/bin/python
import sys
import os
import ntpath
from subprocess import call


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(sys.argv)
        print("After calling " + func.__name__)
    return function_wrapper


file_path = sys.argv[1]
file_name = str(ntpath.basename(file_path))
file_arguments = ''
for element in sys.argv[2:]:
    file_arguments = file_arguments + ',' + element
print(file_arguments)

if (os.path.exists(file_path)):
    print('inside')
    command = 'python ' + file_path + ' ' + file_arguments
    os.system(command)
    exit(0)
else:
    exit(1)
