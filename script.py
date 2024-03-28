## Hangman
import re

wordToGuess = "pottery"

print("Welcome to Hangman! You have a " + str(len(wordToGuess)) + "-letter word to guess. ")

def callInput(wordToGuess, attempts=6, lettersShown=[]):
    if attempts == 0:
        print("You ran out of attempts! The word was \"" + wordToGuess + "\"")
        exit()
    
    currentString = "_"*len(wordToGuess)
    for letter in lettersShown:
        for currentLetter in re.finditer(letter, wordToGuess.lower()):
            currentString = list(currentString)
            currentString[currentLetter.start()] = letter.upper()
            currentString = "".join(currentString)

    if "_" not in currentString:
        print("You won! The word is \"" + currentString + "\"!")
        exit()

    print(currentString + "\n")
    letterInput = input("You have " + str(attempts) + " attempts left, Choose a letter or guess the word: ")

    if len(letterInput) == 1:
        if not letterInput.lower() in wordToGuess.lower(): 
            print("Wrong guess! You have 5 more attempts to go.\n")
            callInput(wordToGuess, attempts-1, lettersShown)

        if letterInput.lower() in lettersShown: 
            print("You already guessed that.")
            callInput(wordToGuess, attempts, lettersShown)

        print("Correct guess!")

        lettersShown.append(letterInput.lower())
        callInput(wordToGuess, attempts-1, lettersShown)

    elif letterInput.lower() == wordToGuess.lower():
        print("You won! The word was \"" + wordToGuess.upper() + "\"!")
        exit()
    else: 
        print("Not a correct form of guessing, Guess with either a letter or the word itself.")
        callInput(wordToGuess, attempts, lettersShown)

callInput("pottery")