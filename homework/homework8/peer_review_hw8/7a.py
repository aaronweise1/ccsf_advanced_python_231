#############################################################
#  CS231  Lab 9                                             #
# Decorate print() such that (A) it refuses to print        #
# anything under ten characters long and (B) only five calls# 
# are allowed, and demonstrate these restrictions when the  #
# program is run                                            #
#                                                           #
#  Student Name:      James Lin  JamesLin288@gmail.com      #
#  Instructor Name:   Aaron Brick  ABrick@ccsf.edu          #
#############################################################

def func1 (*arg):
    l = list(arg)
    str = ''.join(l)
    print ("\n########################")
    if (len(str) > 9):
       print("You entered {} characters long:".format(len(str)))
       print("The secret is doctors and nurses are our heroes")
    else:
       print("###### No secret #####")
#pass1 = input ("Please enter a password it has at least 10 characters long to see the secret:  ")
print ("Please enter a password it has at least 10 characters long to see the secret:  ")
pass1 = "abcdef"
func1(pass1)

pass2 = "abcdefghijkl"
func1 (pass2)

class fcount2(object):
    def __init__(self, inner_func):
        self.inner_func = inner_func
        self.count = 0
        self.block_count =0
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.inner_func(*args, **kwargs)
    def __enter__(self):
        self.block_count += 1
        return self
    def __exit__(self, exception_type, exception_value, tb):
        if exception_type is not None:
            return False
        return self

sep = '\n*************************'
@fcount2
def f(n):
    return n+1
print (sep)
for n in range(5):
    print (f(n))
print ('Function Call count =',f.count)

