"""
Decorate print() such that (A) it refuses to print anything under ten characters long
and (B) only five calls are allowed, and demonstrate these restrictions when the program is run
"""

""" 
I tried to solve the puzzle for individual word length.
I had trouble this week.  I was so optimistic that I could easily solve the length problem.
The reading seemed to be really clear, but somehow, when taking the learning from
"Understanding '*', '*args', '**' and '**kwargs'", and trying to move it from a standalone
function to a a function inside a decorator, I couldn't get the words to be read individually.
Python appeared only interested in the length of the first word, even in my "for arg in args" context.
I will hope to see some solid examples on Tuesday when I look at peer work.

"""

import functools

# this is a decorator that counts the number of times the function being decorated is called (stateful).
# further, there is an if clause to evaluate when that number gets to five
# this is based on the Primer on Decorators reading
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        if wrapper_count_calls.num_calls < 6:
            return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

# this decorator attempts to refuses to pass along any input less than ten characters
def print_big(func):
    @functools.wraps(func)
    def wrapper_print_big(*args, **kwargs):
        print(*args)
        wordlist = []
        for arg in args:
            if len(arg) > 9:
                wordlist.append(arg)
        return func(wordlist)
    return wrapper_print_big

  
@count_calls
@print_big
def printall(*args, **kwargs):
    print(*args, **kwargs)

a = ('short')
b = ('longerxxxxxxxxx')
c = ('longfirstword other words', 'two', 'three', 'all', 'short')
d = ('one', 'two', 'three', 'some', 'longlastword')
e = ('anotherlongone')
f = ('thisshouldnotprint')
g = ('northis')

printall(a)
printall(b)
printall(c)
printall(d)
printall(e)
# these are the sixth and seventh calls that shouldn't run
printall(f)
printall(g)

