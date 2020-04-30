print(len([x for x in open("/users/abrick/resources/english").read().splitlines() if x == x[::-1]]))
