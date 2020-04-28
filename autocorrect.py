from collections import OrderedDict 
import Levenshtein

def getAutocorrect(text):

    # Loop over each word in the list
    candidates = {}
    with open('wordlist.txt') as words:
        for word in words:

            # Use the Levenshtein function to get the number of different characters
            score = Levenshtein.jaro_winkler(text, word)
            candidates[score] = word

    # Determine the 5 words with the lowest score (closest to the word typed in)

    candidates = dict(OrderedDict(sorted(candidates.items())))
    edited = []
    for i in (-1, -2, -3, -4, -5):
        edited.append(list(candidates.values())[i])

    autocorrected = []
    for wordNewline in edited:
        word = wordNewline.replace("\n", "")
        autocorrected.append(word)

    # Return list of 5 words
    return autocorrected

def printAutocorrected(wordsList):
    # Print it neatly
    words = ""

    for word in wordsList:
        words += word + " "
    
    words = words.strip()
    words = words.replace(" ", ", ")

    print(words)


def main():
    pass

autocorrectedList = getAutocorrect("apogoetropims")
printAutocorrected(autocorrectedList)