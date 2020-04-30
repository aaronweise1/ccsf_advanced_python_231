"""
Write a program that creates a pool of workers to all at once 
check whether or not the files whose pathnames are passed in 
are encoded in UTF-8

I used this amazing resource to learn about concurrency: 
https://www.youtube.com/watch?v=IEEhzQoKtQU
"""

import sys 
from typing import List
from os import path
import codecs
import concurrent.futures

def validateFilePath(file_path: str) -> bool:
    """
    Checks a file path to make sure it exists.
    """

    return path.exists(file_path)


def fileEncodingCheck(file_path: str, encoding: str) -> str:
    """
    Verifies if a file is encoded in a particular encoding.
    """
    
    if validateFilePath(file_path):
        try:
            codecs.open(file_path, encoding=encoding, errors="strict").readlines()
            return file_path
        except UnicodeDecodeError:
            return None
            
    return None


def checkEncodings(file_paths: List[str], encoding: str) -> List[str]:
    """
    Takes a list of file paths and returns a new list
    with only those encoded in a selected encoding.
    """

    with concurrent.futures.ThreadPoolExecutor() as executor:
        utf_8_file_paths = executor.map(lambda file_path: fileEncodingCheck(file_path, encoding), file_paths)
        
    print('The following file paths are encoded in UTF-8:')
    for file_path in utf_8_file_paths:
        print(file_path)

    return utf_8_file_paths


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No file paths provided.')
    else:
        checkEncodings(sys.argv[1:], 'utf-8')