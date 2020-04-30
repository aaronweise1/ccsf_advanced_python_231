#!/usr/local/bin/python3
'''
Write a program only one statement long 
(it can span multiple lines) that prints
the number of palindromes in
/users/abrick/resources/english.
'''



'''
What is happening here?
 I am opening the ~abrick/resources/english file, and using len 
to count the number of palindromes(2 or more characters) in my unique 
list using list(set) and then printing the result.
'''
print('The number of palindromes this program found in /users/abrick/resources/english is', (len(list(set([word for word in open('/users/abrick/resources/english').read().splitlines() if word == word[:: - 1] and len(word) > 2])))))

"""
RU - 

Couple comments:
* Keeping the program to one line makes it a little more difficult to read.
    Breaking it down to multiple lines will make it much more readable.
* The output is incorrect. I believe it's because of your 'and len(word) > 2' condition.
    A word with 1 or 2 letters can still be a palindrome. ex: A or BB; both can be reversed
    and still be the same
* You have unnecessary type conversions. You first create a list, then convert it to a set, 
    then convert it back to a list. You can remove the list(set(...)) and still return the
    same result
"""