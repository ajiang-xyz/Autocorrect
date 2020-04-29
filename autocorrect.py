from collections import OrderedDict 
from fuzzywuzzy import fuzz
import datetime
import os

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

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
    if len(wordsList) > 0:
        # Print it neatly
        editedScores = []
        for score in scores:
            score = str(score) + "%"
            editedScores.append(score)

        for word1,score1,word2,score2,word3,score3 in zip(wordsList[::3], editedScores[::3], wordsList[1::3], editedScores[1::3], wordsList[2::3], editedScores[2::3]):
            print("{:<} {:<30}{:<} {:<30}{:<} {:}".format(word1,score1,word2,score2,word3,score3))
    else:
        print("We couldn't find anything :(")

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

def initialize():
    clear

    # Get all the current time and date info
    currentYear = datetime.date.today().year
    currentMonth = datetime.date.today().month
    currentMonth = datetime.date(currentYear, currentMonth, 1).strftime('%b')
    currentDay = datetime.date.today().day
    time = datetime.datetime.now().strftime("%H:%M").split(":")
    currentTime = ""
    if int(time[0]) - 12 > 0:
        currentTime += str(int(time[0]) - 12)
        currentTime += ":" + time[1]
        currentTime += " PM"
    else:
        currentTime += time[0]
        currentTime += ":" + time[1]
        currentTime += "AM"

    # Display all the fancy stuffs :D
    header = """Autocorrect Beta (built on Python) {0}  {1} {2}, {3} 
Type "help" or "credits" for more information.""".format(currentTime, currentMonth, currentDay, currentYear)

    print(header)

def getHelp():
    print("")
    print("Type in a word and the program will print possible spellings and their accuracy percentage")
    print("")
    print("    Type 'exit' to exit this program")
    print("    Type 'clear' to clear the screen")
    print("    Type 'help' to receive this help message again")
    print("    Type 'credit' to see credits for this program")
    print("")

def getCredits():
    print("")
    print("Written in Python by Yixuan-LULU and GeorgeFreidrick :D")
    print("")

def prompt():
    clear()
    initialize()
    done = False
    while done == False:
        print(">>> ", end="")
        word = input("")
        if word == "clear":
            clear()
        elif word == "exit":
            clear()
            exit()
        elif word == "help":
            getHelp()
        elif word == "credits":
            getCredits()
        else:
            print("Searching...", end="")
            autocorrected, scores = getAutocorrect(word)
            print("\r            ")
            printAutocorrected(autocorrected, scores)
            print("")

if __name__ == "__main__":
    prompt()