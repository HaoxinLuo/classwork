def triplet():
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                if a*a + b*b == c*c:
                    print a,b,c

def sqlist(l): #in the small
    result=[]
    for item in l:
        result.append(item*item)
    return result

def sqlist2(l):
    return [x*x for x in l]
# l = range(50)
# [item for item in l if item%5==0 if item%3==0]
# [0,15,30,45]

#gui allergo?

