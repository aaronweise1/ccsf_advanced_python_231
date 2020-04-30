"""
Write a program only one statement long (it can span multiple lines) that prints the
number of palindromes in /users/abrick/resources/english

This includes the single character at the head of each of 26 alphabetical sections of the file.
"""

print(len(list(filter(lambda x: x.rstrip() == x.rstrip()[::-1], open('/users/abrick/resources/english', 'r')))))
