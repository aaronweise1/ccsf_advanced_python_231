# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:22:47 2020  @author: Mary Liu
Decorate print() such that 
(A) it refuses to print anything under ten characters long
(B) only five calls are allowed, and demonstrate these restrictions 
    when the program is run
"""
def long_words(func):
    # Define and return a new function that allows 5 calls and 10(or more) characters 
    def wrapper_long_words(*args):
        count = 0       
        for arg in args:
            if len(arg) > 9 and count < 5:
                func(arg)
                count +=1
    return wrapper_long_words

@long_words    # show_words=long_words(show_words)
def show_words(word):
    print(word)

#create the list and pass it to the function show_words.        
my_list = ('hello', 'kindergarten', 'apple', 'importance', 'dictionaries', 'princesses', 'tournaments', 'punctuation', 'kindergarteners')
show_words(*my_list)
