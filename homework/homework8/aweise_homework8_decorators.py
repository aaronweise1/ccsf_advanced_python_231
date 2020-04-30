"""
Decorate print() such that 
(A) it refuses to print anything under ten characters long and 
(B) only five calls are allowed, 
and demonstrate these restrictions when the program is run

Program will wrap print in two decorators. The first will count function calls and
return an exception after the call limit has been exceeded. The second will print
only if the character length is >=10
"""


class CallLimitError(Exception):
    """Exception raised when a function has been exceeded its call limit."""
    pass


# decorator that counts function calls and raises a CallLimitError exception if call_limit is exceeded
def countFunctionCalls(func, count=[0]):

    def incrementByOne(*args, **kwargs):
        call_limit = 5
        count[0] += 1
        if count[0] > call_limit:
            raise CallLimitError('Sorry, but you have exceeded your maximum of 5 print() calls.')
        else:
            return func(*args, **kwargs), count[0]
            
    return incrementByOne


# decorator that will print either strings >= 10 characters or an error message
def printDecorator(print_func):

    def printFunctionRestrictions(*args, **kwargs):
        if len(*args) >= 10:
            print_func(*args, **kwargs)
        else:
            print_func('I will not let you print less than 10 characters!')

    return printFunctionRestrictions


print = printDecorator(countFunctionCalls(print))
print('California') 
print('New York')
print('Washington')
print('Mississippi')
print('Hawaii')
print('Alaska')
print('Arizona')