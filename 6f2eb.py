def fib(n): #38 is ~limit
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    a = 1
    b = 1
    while(n>1):
        c = a + b
        a = b
        b = c
        n = n-1
    return a

def fib3(n,a=1,b=1):
    if n ==1:
        return a
    else:
        return fib3(n-1,b,a+b)

###my version. w/o wrapper? @_@ 
def fib4(n): #memoization(dynamic programming)
    t={}
    def inner(n):
        if n in t:
            return t[n]
        if n <= 2:
            return 1
        t[n] = inner(n-1) + inner(n-2)
        return t[n]
    return inner(n)


###same as above. Z version
def memoize(func):
    t = {}
    def wrapper(*args):
        if args in t:
            return t[args]
        else:
            t[args] = func(*args)
            return t[args]
    return wrapper

@memoize #the same as fib5 = memorize(fib5)
def fib5(n):
    if n <= 2:
        return 1
    else:
        return fib5(n-1) + fib5(n-2)


@memoize
def ricslength(s1,s2,i,j): #somehow don't work properly?
    if i>=len(s1) or j>=len(s2):
        return 0
    elif s1[i] == s2[j]:
        return 1 + ricslength(s1,s2,i+1,j+1)
    else:
        return max(ricslength(s1,s2,i,j+1),ricslength(s1,s2,i+1,j))
    
