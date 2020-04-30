from math import sin, pi

# @desc prints sinewave vertically. 15 is used to shift 
# and make the curve more visible
[print(' '*int((sin(x/pi)*15)+15) + '*') for x in range(30)]

