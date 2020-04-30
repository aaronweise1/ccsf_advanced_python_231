#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:29:24 2020

@author: RagwaElsayed
"""

#I have two programs: Assign.py and Assign_2.py

#!/usr/local/bin/python3
# NAME: Ragwa Elsayed
# FILE: is_palindrome.py
# DATE: <02/09/2020>
# DESC: Is Palindrome word assignment


def reverse(s): 
    return s[::-1] 
  
def is_palindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
    #count = 0
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    else:
        return False
    
assign1 = open('/users/abrick/resources/english').read()
#assign1 = open('/Users/RagwaElsayed/Documents/Rogy/CCSF/Spring20/AdvPy/assign1.txt').read()
pal= assign1.split('\n')

c = []
[c.append(i) for i in pal if is_palindrome(i)]
for i in c:
    if i == ' ':
        print('yes')
    if i == '':
        print('yes2')
print(len(c))

