if 1==1:
     import math
     for nbr in [(math.sin(math.radians(x)) + 2) for x in range(-90,800,15)]:
          z = int(nbr*10)
          print("."*(z-1),"*")	
else:
     print("Wow! 1 doesn't equal 1....umkay...")

