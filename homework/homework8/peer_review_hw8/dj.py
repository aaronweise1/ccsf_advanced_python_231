#CS 231
#assignment 8
#Decorate print() such that 1) it refuses to print anything under 10 characters long and 2) only five calls are allowed.
 

import functools

#this decorator counts the number of times print() is called and limits those calls to five.
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        if wrapper_count_calls.num_calls <= 5:
        	print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        	return func(*args, **kwargs)
        else:
        	print(f"Sorry, you are limited to 5 calls of {func.__name__!r}")
        
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

#this decorator limits print() to print strings more than 10 characters long.
def count_chars(func):
    @functools.wraps(func)
    def wrapper_count_chars(*args, **kwargs):
        if len(*args, **kwargs) > 10:
            return func(*args, **kwargs)
        else:
            print(f"You must enter more than 10 characters in order to call {func.__name__!r}")
    return wrapper_count_chars   

@count_calls
@count_chars
def print_stuff(*args, **kwargs):
    print(*args, **kwargs)
   


print_stuff("be safe")
print_stuff("stay indoors")
print_stuff("wash your hands")
print_stuff("for 20 seconds")
print_stuff("don't touch your face")
print_stuff("practice social distancing")


