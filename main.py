import random
from tqdm import tqdm
import collections



wordslist = 'english'

f = open('wordlists/'+wordslist+'.txt') # Open file on read mode
words_list = f.read().split("\n") # Create a list containing all lines
f.close() # Close file

correct = "zwitterionic"


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


#Getting the most frequent characters of the list
most_frequent_characters = []
for line in words_list:
    if len(line) == len(correct):
        most_frequent_char = collections.Counter(line).most_common(3)
        most_frequent_characters.append(most_frequent_char[0])

sorted_by_second = sorted(most_frequent_characters, key=lambda tup: tup[1]) #https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
sorted_by_second.reverse()
sortedChars = []
for item in sorted_by_second:
    if item[0] not in sortedChars:
        sortedChars.append(item[0])

rightGuesses = 0

print(sortedChars)


def guessRecurs(pos:int, rightGuesses, badGuesses, wordArr):
    if rightGuesses < len(correct): currLtr = sortedChars[pos]
    if rightGuesses == len(correct):
        print("Guessed the word! The word was "+correct)
        print("right guesses",rightGuesses)
        print("bad guesses", badGuesses)
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
guessRecurs(0, 0, 0, defaultArr)