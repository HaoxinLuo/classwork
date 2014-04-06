
def Hzip():
    L1 = [1,2,3,4]
    L2 = [10,20,30,40,50]
    return zip(L1,L2) #[(1,10),(2,20),(3,30)]

def m2(m): #returns True if more than 3 conse elements has diff > 30
    diffs = [abs(x-y) for x in m for y in m[1:] if abs(x-y) >= 30]
    return len(diffs)>= 3

def build_corpus(fn):
    wordString = open(fn).read().lower()
    letters = "abcdefghijklmnopqrstuvwxyz" #space or no?
    wordString = [x for x in wordstring if x in letters] #creates list of all letters
    wordString =  "".join(wordString)
    wordList = wordString.split()

    tuples = zip(wordList,wordList[1:],wordList[2:])
    corpus = {}
    [add_word(corpus,(x,y),z) for (x,y,z) in tuples]


def add_word(corpus,key,value):
    x= """
    if corpus.has_key(key):
    corpus[key].append(value)
    else:
    corpus[key]=[value]
    """
    corpus.setdefault(key,[])
    corpus[key].append(value)
    
