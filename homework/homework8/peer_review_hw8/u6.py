# CS231
# Assignment# 8
#  Decorate print() such that (A) it refuses to print anything under ten characters long and
#  (B) only five calls are allowed, and demonstrate these restrictions when the program is run


def max_calls(limit):
    count = [0]

    def inner_decorator(func):
        def filter_len(*args):
            if count[0] < limit:
                count[0] += 1
                args = tuple([arg for arg in args if len(str(arg)) >= 10])
                return func(*args)
        return filter_len
    return inner_decorator


def print_args(*args):
    print(*args, sep=', ')


print("Call original print_args() 10 times:")
for i in range(0,10):
    print_args("demonstrate", "these", "restrictions", "when", "the", "program", "is", "run")

print()

# Decorate the print_args function
@max_calls(5)
def print_args(*args):
    print(*args, sep=', ')


print("Call decorated print_args() 10 times:")
# Try to call the decorated print_args function 10 times, should only print 5 times
for i in range(0,10):
    print_args("demonstrate", "these", "restrictions", "when", "the", "program", "is", "run")









