#continued from 2/12

def build_corpus(fn):
    wordString = open(fn).read().lower()
    letters = "abcdefghijklmnopqrstuvwxyz" #space or no?
    wordString = [x for x in wordstring if x in letters] #creates list of all letters
    wordString =  "".join(wordString)
    wordList = wordString.split()
    #returns multiple lists, w/ 1,2,...,n off sets
    L = [wordString[x:] for x in range(n)]
    #turns List with elements of other lists into a tuple w/ all lists.
    tuples = zip(*L)
    asdf = """
    tuples = zip(wordList,wordList[1:],wordList[2:])
    corpus = {}
    [add_word(corpus,(x,y),z) for (x,y,z) in tuples]
    for(x,y,z) in tuples:
        add_word(corpus,(x,y),z)
        """

def add_word(corpus,key,value):
    x= """
    if corpus.has_key(key):
    corpus[key].append(value)
    else:
    corpus[key]=[value]
    """
    corpus.setdefault(key,[])
    corpus[key].append(value)

def makePass():
    key = random.choice(corpus.keys())
    tet = " ".join(key)
    for i in range(200):
        next = random.choice(corpus[key])
        text = text + " " + next
        key = list(key)
        key = key[1:]
        key.append(next)
        key = tuple(key)
    print(text)

#*args says this is a tuple w/ all the arguments. eg: printArgs([1,A,blah],zz) -> ([1,A,blah],zz)
def printArgs(*args):
    return args
