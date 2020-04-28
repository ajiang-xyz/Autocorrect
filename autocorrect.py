from collections import OrderedDict 
from fuzzywuzzy import fuzz
import os

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

def clear():
    # Test if using some linux distro
    if os.name == "posix":
        os.system("clear")

    # Some windows distro
    elif os.name == "nt":
        os.system("cls")
    else:
        # I really don't know
        print("I couldn't figure out what operating system you're using")

def getAutocorrect(text):

    # Loop over each word in the list
    candidates = {}
    with open('wordlist.txt') as words:
        for word in words:
            word.replace("\n", "")
            word = word.rstrip("\r\n")

            # Use Fuzzywuzzy to determine the percentage of "sameness"
            score = fuzz.ratio(word, text)
            candidates[word] = score

    # Determine the 5 words with the highest match percentage (closest to the word typed in)

    candidates = dict(OrderedDict(sorted(candidates.items())))
    edited = {}
    for score in candidates.values():
        if score >= 75:
            for key in getKeysByValue(candidates, score):
                edited[key] = score

    autocorrected = []
    scores = []
    for word in edited.keys():
        autocorrected.append(word)

    for score in edited.values():
        scores.append(score)

    # Return list of 5 words
    # autocorrected.reverse()
    # scores.reverse()

    sort = {autocorrected[i]: scores[i] for i in range(len(autocorrected))}
    sort = dict(OrderedDict(sorted(sort.items())))
    sort = {k: v for k, v in sorted(sort.items(), key=lambda item: item[1])}
    autocorrected = list(sort.keys())
    scores = list(sort.values())
    

    autocorrected.reverse()
    scores.reverse()
    return autocorrected, scores

def printAutocorrected(wordsList, scores):
    # Print it neatly
    words = ""

    for i in range(0, len(wordsList)):
        words += wordsList[i] + " ({0}%) ".format(scores[i])
    
    words = words.strip()
    words = words.replace(") ", "), ")

    print(words)


def main():
    clear()
    done = False
    while done == False:
        print(">>> ", end="")
        word = input("")
        if word == "clear":
            clear()
        elif word == "exit":
            clear()
            exit()
        else:
            print("Searching...", end="\r")
            autocorrected, scores = getAutocorrect(word)
            printAutocorrected(autocorrected, scores)

if __name__ == "__main__":
    main()