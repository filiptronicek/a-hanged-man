import random
from tqdm import tqdm
import collections
from re import search, compile
import string

wordslist = 'english'

f = open('wordlists/'+wordslist+'.txt') # Open file on read mode
words_list = f.read().split("\n") # Create a list containing all lines
f.close() # Close file

correct = "therapist"

used = []
finalString = []
bad = []

finalString.extend("_"*len(correct))

def filterOut(variable): 
    if (variable in used): 
        return False
    else: 
        return True

def FillIn(char, pos):
    for p in pos:
        finalString[p] = char
    print(finalString)

def recompile(wlist):
    print("got a list of length",str(len(wlist)))
    wl = []
    for w in (wlist):
        if len(w) == len(correct):
            wl.append(w)
        
    wlist = wl
    for u in finalString:
        if u != "_":
            r = compile(".*"+u)
            wlist = list(filter(r.search, wlist))
            print("New list:",str(len(wlist)))
            if len(wlist) < 10:
                print("Og list:",str(wlist))
    return wlist

def takeGuess(guess):   
    used.append(guess)
    if guess in correct:
        FillIn(guess,[pos for pos, char in enumerate(correct) if char == guess])
        return True
    else:
        bad.append(guess)
        return False

def rightGuesses():
    rGuesses = 0
    for letter in finalString:
        if letter != "_":
            rGuesses += 1
    return rGuesses
def getMostFrequent(wlist):
    freqchar = []
    for w in wlist:
        #if len(w) == len(correct):
        #freqchar = collections.Counter(w).most_common(len(set(w))))
        freqcharT = collections.Counter(w).most_common(len(set(w)))
        for i,f in enumerate(freqcharT):
            freqchar.append(freqcharT[i])

    sortedL = sorted(freqchar, key=lambda tup: tup[1]) #https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    sortedL.reverse()
    sortedChars = []
    for item in sortedL:
        if item[0] not in sortedChars:
            sortedChars.append(item[0])
    filtered = filter(filterOut, sortedChars) 
    return list(filtered)

def loop(tas, wList):
    print("sending a list of",str(len(wList)))
    wList = recompile(wList)
    if rightGuesses() < len(correct):
        try:
            letter = getMostFrequent(wList)[tas]
            tas += 1
        except IndexError:
            print("out of thing")
            letter = random.choice(string.ascii_lowercase)

        if letter not in used:
            print("Guessing",letter)
            print("used:"+str(used))
            print("bad:"+str(bad))
            takeGuess(letter)
    if len(used) != 26:
        loop(tas, wList)
            
loop(0, words_list)
#print(str(100*rightGuesses()/len(used))+"%")