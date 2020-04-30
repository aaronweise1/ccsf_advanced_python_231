#!/usr/local/bin/python3
# Course   : CS 231 
# Homework : 11
# Due date  :  April 19, 2020
# Filename: hw11.py

"""
 Write a universal wrapper program that expects its command line arguments to contain the absolute path to any program, followed by its arguments. The wrapper should run that program and report its exit value.
"""

import sys
import subprocess

#the whole command line arguments
list_args = sys.argv

# will run the program [the absolute path to any program, followed by its arguments] and report its exit value
def call(list_args):
    # reminder: first argument, list_args[0], is name of this script
    result = subprocess.call(list_args[1:], shell=False)
    print(result)
     # result = subprocess.call(list_args[1:], shell=False, stdout=subprocess.PIPE)
     # print(result.stdout.decode())

if __name__=="__main__" :
    if len(list_args) == 1: # no absolute path or arguments provided
        print("Please provide the absolute path to any program, " + 
            "\nfollowed by its arguments or without arguments." + 
            "\nExamples: \npython3 hw11.py /bin/ls -a " + 
            "\npython3 hw11.py /bin/ls *t" + 
            "\npython3 hw11.py /usr/local/bin/python3 hw9.py"
            + "\nExiting now.")
    else:   #there is absolute path and arguments provided
        print("\nThe command lines arguments:")
        print(*list_args, sep=" ")
        print("This script name is:", list_args[0])
        print("The absolute path of program, followed " + 
                "by its arguments are:")
        print(*list_args[1:], sep=" ")
        print("\nRunning:\n")
        call(list_args)