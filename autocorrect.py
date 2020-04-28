from collections import OrderedDict 
from fuzzywuzzy import fuzz

def getAutocorrect(text):

    # Loop over each word in the list
    candidates = {}
    with open('wordlist.txt') as words:
        for word in words:

            # Use Fuzzywuzzy to determine the percentage of "sameness"
            score = fuzz.ratio(word, text)
            candidates[score] = word

    # Determine the 5 words with the highest match percentage (closest to the word typed in)

    candidates = dict(OrderedDict(sorted(candidates.items())))
    edited = {}
    for score in candidates.keys():
        if score >= 75:
            edited[candidates[score]] = score

    autocorrected = []
    scores = []
    for wordNewline in edited.keys():
        word = wordNewline.replace("\n", "")
        autocorrected.append(word)

    for score in edited.values():
        scores.append(score)

    # Return list of 5 words
    autocorrected.reverse()
    scores.reverse()
    return autocorrected, scores

def printAutocorrected(wordsList, scores):
    # Print it neatly
    words = ""

    for i in range(0, len(wordsList)):
        words += wordsList[i] + "({0}) ".format(scores[i])
    
    words = words.strip()
    words = words.replace(" ", ", ")

    print(words)


def main():
    pass

autocorrectedList, scores = getAutocorrect("apogeotropims")
printAutocorrected(autocorrectedList, scores)