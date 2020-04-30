"""
Implement two algorithms which demonstrably reach the same 
conclusion and use profile or cProfile to time them both.

I broke away from the readings to learn how to make my own
profile decorator from https://www.youtube.com/watch?v=8qEnExGLZfY. 
I wrap two functions that remove duplicates with this decorator. 
"""

import random
import cProfile
import pstats
import io


def profileFunction(func):
    """
    Decorator used to profile a given function and 
    prints the results ordered by cumulitive time.
    """

    def profile(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        function_return = func(*args, **kwargs)
        prof.disable()
        io_stream = io.StringIO()
        sortby = 'cumulative'
        stats = pstats.Stats(prof, stream=io_stream).sort_stats(sortby)
        stats.print_stats()
        print(io_stream.getvalue())
        return function_return

    return profile


@profileFunction
def dedupeNumbersSlow(num_list):
    """
    Dedupes a given list of numbers and returns the duplicates.
    This function is slower because it uses nested loops.
    """

    dupes = []
    while num_list:
        num = num_list.pop()
        if num in num_list:
            if num not in dupes:
                dupes.append(num)
    return dupes


@profileFunction
def dedupeNumbersFast(num_list):
    """
    Dedupes a given list of numbers and returns the duplicates.
    This function is faster because it uses dictionary lookups.
    """

    dupes = []
    seen_dict = {}
    for num in num_list:
        if num in seen_dict:
            seen_dict[num] += 1
        else:
            seen_dict[num] = 1
    for num in seen_dict:
        if seen_dict[num] > 1:
            dupes.append(num)
    return dupes




num_list = [random.randrange(0,100) for num in range(500000)]
dedupeNumbersSlow(num_list)
dedupeNumbersFast(num_list)

