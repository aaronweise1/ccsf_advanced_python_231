"""
Write a universal wrapper program that expects its 
command line arguments to contain the absolute path 
to any program, followed by its arguments. The wrapper 
should run that program and report its exit value
"""

import sys
from subprocess import call


def executeExternalProgram(file_path, arguments=None):
    """
    Contructs a python3 call to a program from command line.
    First argument is the file path. Subsequent arguments are
    passed through as arguments.
    """
    call_command = ['python3', '{file_path}'.format(file_path=file_path)]
    for arg in arguments:
        call_command.append(arg)
    exit_value = call(call_command)
    if exit_value == 0:
        print('\nProgram has successfully run. Exiting.')
    else:
        print('\nProgram has run unsuccessfully with an error.')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No program provided. Please provide a filepath to one.')
    else:
        file_path = sys.argv[1]
        executeExternalProgram(sys.argv[1], sys.argv[2:])