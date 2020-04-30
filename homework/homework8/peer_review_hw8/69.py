#himynameisjordan
#Decorate print() such that (A) it refuses t printanything under ten characters long and (B) only five calls are allowed, and demonstrate these restrictions when the program is run.


#define decorator function, using print w/out () as the func argument 
def decoratingPrint(print):
    #define inner function taking arbitrary no. of  arguments (*args = tuple)
    def wrapper(*args):
        #unpack tuple
        for arg in args:
            #test for char len >= 10
            if len(arg) >= 10:
                #func
                print(arg)
            else:
                continue
    #return modified function 
    return wrapper
#pie syntax 
@decoratingPrint
#test function that takes in arbitrary number of arguments (in this case: strings) that is then passed to the decoratingPrint function decorator
def testMe(*args):
    print(*args)

#test cases testing various string lengths
testMe('12345678910', '123456789', 'isthismorethanten', 'oristhisisless')
testMe('less', 'than', 'ten')
testMe('lessthanten?', 'notlessthanten?')
