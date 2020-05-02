import random
from tqdm import tqdm
import collections
from re import search


wordslist = 'english'

f = open('wordlists/'+wordslist+'.txt') # Open file on read mode
words_list = f.read().split("\n") # Create a list containing all lines
f.close() # Close file

correct = "guesses"

def getFreq(letterAr):
    #Getting the most frequent characters of the list
    most_frequent_characters = []
    for line in words_list:
        if len(line) == len(correct):
            if letterAr.count('_') != len(letterAr):
                for letter in letterAr:
                    letter = letter.replace("_","A-Z")
                    #if letter != "A-Z":
                        #print("Searching for ["+letter+"] in " + line)
                    if search("["+letter+"]", line):
                        if len(correct) > 2:
                            most_frequent_char = collections.Counter(line).most_common(len(set(line)))
                            for char in most_frequent_char:
                                if letter == char[0]:
                                    most_frequent_characters.append(char)
                                else:
                                    most_frequent_characters.append(most_frequent_char[0])

                        else:
                            most_frequent_char = collections.Counter(line).most_common(1)
                            most_frequent_characters.append(most_frequent_char[0])
                        
            else:
                most_frequent_char = collections.Counter(line).most_common(1)
                most_frequent_characters.append(most_frequent_char[0])

    sorted_by_second = sorted(most_frequent_characters, key=lambda tup: tup[1]) #https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    sorted_by_second.reverse()
    sortedChars = []
    for item in sorted_by_second:
        if item[0] not in sortedChars:
            sortedChars.append(item[0])

    print(sortedChars)
    return sortedChars


rightGuesses = 0


def guess(guess_val, wordArr):
    arrOut = ""
    if guess_val in correct:
        for occ in [pos for pos, char in enumerate(correct) if char == guess_val]:
            wordArr[occ] = guess_val
        for c in wordArr:
            arrOut += c
        
        print(arrOut)
        return correct.count(guess_val)

    else:
        return False

def guessRecurs(pos:int, rightGuesses, badGuesses, wordArr):
    if rightGuesses == 0:
        currLtr = all_freq[pos]    
    if rightGuesses < len(correct):
        currLtr = getFreq(wordArr)[pos]
    if rightGuesses == len(correct):
        print("Guessed the word! The word was "+correct)
        print("right guesses:",rightGuesses)
        print("bad guesses:", badGuesses)
    else:
        if currLtr in wordArr:
            guessRecurs(pos +1, rightGuesses, badGuesses, wordArr)
        else:
            guessResp = guess(currLtr, wordArr)
            if type(guessResp) == int:
                rightGuesses += guessResp
            else:
                badGuesses += 1
            guessRecurs(pos +1, rightGuesses, badGuesses, wordArr)
defaultArr = []
for a in correct:
    defaultArr.append('_')
all_freq = getFreq(defaultArr)
guessRecurs(0, 0, 0, defaultArr)