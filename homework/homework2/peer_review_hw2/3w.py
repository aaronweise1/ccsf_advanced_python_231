import math

for x in range(0, 360):
    r = math.radians(x)
    sin = math.sin(r)
    value = round(float('{}'.format(sin * 100))) // 2
    print((value + 50) * " ", end="*\n")
