def dn():
#    print("b4 defining inner")
    def inner(x):
#        print("running inner")
        return 2*x
    return inner

a = dn()

def triple(n):
    def double(x):
        return n*x
    return double

def test(n):
    def inner():
        return n() + " " + n()
    return inner

@test
def blah():
    return "works"

def printargs(*args,**kwargs):
    print args
    print kwargs

#printargs(1,2,number=3) -> (1,2) {'number':3}


def argprinter(func):
#    @wraps(func)
    def wrapper(*args,**kwargs):
        print "in wrapper"
        print args
        print kwargs
        return func(*args,**kwargs)
    return wrapper

@argprinter
def printargs(*args,**kwargs):
    print "in printargs:"
    print args
    print kwargs

@argprinter
def addtwo(x,y):
    return x + y

@argprinter
def addtwo2(x=10,y=20):
    return x + y
