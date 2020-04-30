print(len(list(item for item in open("/users/abrick/resources/english", "r").readlines() if item.rstrip() == item.rstrip()[::-1])))

"""
3f - 

Couple comments:
* Good and clean. Produces the correct result.
* The one-line statement is a bit long, maybe break it up to multiple lines
    for readability
* Nit: To make your list declaration cleaner, you can write '[item for item in ...]', 
    versus 'list(item for item in...)'
"""