#!/usr/bin/python3

import functools, sys, string, os

# these empty lists created to later print out arguments passed in with this program
myargs = [] # list stores arguments as a list
positions = [] # list stores positions of arguments as a list

class function_wrapper(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __call__(self, *args, **kwargs):
        return self.wrapped(*args, **kwargs)

@function_wrapper
def function():
    # should match what user passed in as first argument
    print("\nThe absolute path is ", os.path.abspath(__file__))
    arguments = len(sys.argv) -1
    print("\nYou passed in " + str(arguments) + " argument(s)\n")
    position = 1
    positions.append(position)
    # while loop executes when at least 1 arg passed in when script run
    while (arguments >= position):
        myargs.append(sys.argv[position])
        print('Argument %i: %s' % (position, sys.argv[position]))
        position = position + 1
        positions.append(position)
    #ex = exit(0)
    print('\nexit(0)\n')
    sys.exit()

if __name__ == '__main__':
    function_wrapper(function())
    
