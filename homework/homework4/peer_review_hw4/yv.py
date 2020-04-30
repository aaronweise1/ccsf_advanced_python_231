#!/usr/local/bin/python3
# Name: Greg Harrison
# Course: CS231
# Date: 3/1/2020
# File: text_wrapper.py
# Desc: A program to lazily rewrap text from the filename passed so that it
#   fits an 80 column window without breaking any words. Filename is
#   passed as first commandline argument.

import sys


def wrap_text(file):
    """
    Yields the next lines of text, containing as many words as possible.

    Note:
        file object should not contain any text that has a single string,
        more than 80 characters, that is unbroken by a space

    Args:
        param file: The file object with the text to be wrapped
    """

    # Split the text into paragraphs to retain paragraph format if paragraphs exist
    paragraphs = file.read().split('\n\n')

    for paragraph in paragraphs:

        # Remove all newline characters from paragraph. This effectively
        # turns paragraph into a line
        line = paragraph.replace('\n', ' ')

        while True:
            if len(line) > 80:
                # slice_position is the position of the last space in the first 80
                # characters of the line
                slice_position = line[:79].rfind(' ')

                yield line[:slice_position]

                # The line is now the remainder of the line that was not yielded
                line = line[(slice_position + 1):len(line)]
            else:
                # If the line has fewer than 80 characters, The line is yielded
                # with a newline character. This will place a blank row between
                # paragraphs. The while True loop is broken and when wrap_text
                # is called again, wrapping of the next paragraph will begin
                yield line + '\n'
                break


def print_wrapped_text(file_name):
    """Calls the wrap_text generator to print the document with text wrapping"""
    with open(file_name, "r") as text:
        for wrapped_line in wrap_text(text):
            print(wrapped_line)


# text file name will be given as the first command line argument
text_file = sys.argv[1]
print_wrapped_text(text_file)
