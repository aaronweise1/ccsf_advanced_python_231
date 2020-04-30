#!/usr/bin/python3

'''
This program is not done! Sorry. I am trying to revamp an old program from a previous semester.
The program runs but still encounters a traceback related to the multiprocessing.Pool(),
the absolute file paths are being seen as a directory and it's not working. I don't really
undestand pools and workers yet. Thanks for your understanding! I will keep working on it. '''

import functools, sys, string, os, codecs, multiprocessing

myargs = [] #variable to store arguments as a list
positions = []

def checkencoding(list):
    for myarg in list:
        try:
            f=codecs.open(myarg, encoding="utf-8", errors="strict").readlines()
            print(f[1])
        except UnicodeDecodeError:
            print("invalid utf-8")

if __name__ == '__main__':
    #format string to output script name passed in as zeroeth argument
    print("\nThe script has the name %s \n" % (sys.argv[0]))

    #storing number of items passed into sys.argv when script run in command line
    arguments = len(sys.argv) -1

    #format string to print number of items passed in as arguments
    print('The script is called with %i argument(s).\n' % (arguments))

    #variable for comparison to number of arguments
    position = 1
    positions.append(position)

    #while loop executes if at least 1 arg passed in
    while (arguments >= position):
        myargs.append(sys.argv[position])
        print('Parameter %i: %s' % (position, sys.argv[position]))
        position = position + 1
        positions.append(position)

    #dictionary comprehension
    args_dict = {key:value for key, value in zip(myargs, positions)}
    #the myargs list as keys serves to eliminate duplicate argument names in dict
    print("\n", args_dict)

    newlist = []

    myanswer = list(args_dict.keys())
    print("\n", myanswer, "\n")

    #checkencoding(myargs)
    try:
        p = multiprocessing.Pool()
        result = p.map(checkencoding, myargs)
        print(result)
    except IsADirectoryError:
        print("Sorry, you encountered an error.")
