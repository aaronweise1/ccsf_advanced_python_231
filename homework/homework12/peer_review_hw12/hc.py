#!/bin/python3
#yesona mata

# Program that checks the string encoding of different file-names
# python3 program file1 file3 .. 

from concurrent.futures import ThreadPoolExecutor
import sys
import subprocess

def filecode(filepath):

        proc = subprocess.check_output(["/usr/bin/file",filepath])
        if 'UTF-8' in str(proc):
                return 'utf-8'
        return 'Not Utf-8'
if __name__ == "__main__":
    
    fileNames = sys.argv[1:]     
    
    # create a thread pool and 
    # pass the filenames 

    pool = ThreadPoolExecutor()
    print(list(pool.map(filecode,fileNames)))