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
    autocorrected = []
    for i in range(0, 6):
        autocorrected.append(list(sorted(candidates.values()))[i])

    # Return list of 5 words
    return autocorrected
    