#predict what will happen
x = 1
def f1():
    print x
def f2():
    y = x+1
    print y
def f3():
    x = x + 1
    print x

#globals() prints dict containing all namespace and values

def s1(s):
    s = s + "world"
    return s

def s2(s):
    s+= "world"
    return s

s = "hello"
#print(s1(s))
#print(s2(s))
#print(s)
# ^ shows the lines are compiled first, thats how the global s is defined     

def sl1(l):
    l = l + [4]
    print l

def sl2(l):
    l += [4]
    print l

l = [1,2,3]
#print l
#sl1(l)
#print l
#sl2(l)
#print l
# += modified the global list, thou += did not modify the global string because strings cannot be modified.


#*************************"actual lesson"*************************************
#closures
def outer():
    def inner():
        print "this is the inner func"
    print "this is outer func"
    return inner #will not run the inner fxn, but return a pointer to inner
#    return inner() inner() will run the inner fxn
#a = outer(), will set a = pointer to inner. a() will run inner()

def f(x):
    return x*x

square = f

def apply(f,x):
    return f(x)

#apply(square,2) -> 4. square is pointer to f(), apply uses f() and 2

def outer2():
    i = 10
    def inner(x):
        return x + i
    return inner

def make_adder(n):
    def inner(x):
        return n + x
    return inner
add5 = make_adder(5) #add5(3) -> 8
add7 = make_adder(7) #add7(3) -> 10

import random

def get_name():
    names = ['tom','sue','alan','scott','sara','howie','ben']
    return random.choice(names)

def getSentence():
    sentences = ['see the ball','be the ball','eat the ball']
    return random.choice(sentences)
# 'problem' none of names are capitalized
#solution V
def capital(func):
    def inner():
        s = func()
        return s.capitalize()
    return inner

sent2 = capital(getSentence)
name2 = capital(get_name)

@capital #magic
def gn():
    names=['tom','sue','alan','scott','sara','howie','ben']
    return ranodom.choice(names)

blah = """

"""
