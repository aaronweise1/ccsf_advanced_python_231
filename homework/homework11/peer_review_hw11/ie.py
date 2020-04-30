#!/usr/bin/env python3

#Current:
#Write a universal wrapper program that expects its command line arguments to contain the absolute path to any program, followed by its arguments. The wrapper should run that program and report its exit value

import sys, subprocess, os
from shutil import which

#Check if a program was provided as an argument
if len(sys.argv) < 2:
    print("No arguments provided.")
    print("Syntax: 'python3 (this program's name).py (program) [arguments (optional)]'")
    print("Ex: 'python3 hwb-cs231.py ls -l'")
    exit()

#Dictionary of common exit status
exit_stat = {
    0: "Success",
    1: "Error",
    2: "Misuse of shell builtins",
    126: "Command invoked cannot execute",
    127: "Command not found",
    128: "Invalid argument for 'exit'",
    130: "Terminated by Ctrl+C"
}

#Create list to hold arguments. All instance of 'command' can be replaced with sys.argv[1:]
command = []
for n in sys.argv[1:]:
    command.append(n)

#Check if program exists (using 'which') and if an absolute path was provided
if which(os.path.abspath(command[0])) != None and command[0] == os.path.abspath(command[0]):
    #Store exit status in variable
    stat = subprocess.call(command)
    #Print exit status and meaning
    print("Exit status: " + str(stat) + ', ', exit_stat[stat])
else:
    print("Program does not exist in given path. Please provide a valid program or a correct path to a program.")
    print("Terminating program...")
