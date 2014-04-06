import cProfile
import random
def trip(n): #no duplicate
    l = []
    [l.append((a,b,c)) for a in range(1,n) for b in range(1,n) for c in range(1,n) if a*a+ b*b == c*c if (a,b,c) not in l if (b,a,c) not in l]
    return l


def quickSort(l):
    if (len(l) < 2):
        return l
    p = l[random.randrange(len(l))]
    return quickSort([x for x in l if x<p])+[x for x in l if x==p]+quickSort([x for x in l if x>p])

def randList(n):
    return [random.randrange(10000) for x in range(n)]

def check(l):
    c = l[0]
    ans = True
    for x in range(len(l)):
        if 
            
    return [ans] + [len(l)] + [l]
    
