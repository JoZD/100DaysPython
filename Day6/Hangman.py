
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["python", "hangman", "computer", "programming", "variable", "function", "loop", "list", "tuple", "dictionary"]

word = random.choice(words) #Select a random word from the list

print(word)



ListedWord = [] #

#This creates a list wtih blank spaces only, 
for char in word: 
    ListedWord.append('_')

print(ListedWord)

#These is to take the guess letter of the user 




#Check if the word is contained in the word, if so, take the index and substitute that indext with the word being evaluated


counter = 0
failedGuesses = []
wellGuesses = []

active = True

while '_' in ListedWord:
    if counter == 7:
        print("You lost")
        active = False
        break

    guess = input("Please enter a guess: \n").strip().lower()

    for index, char in enumerate(word):
        if guess == char:
            ListedWord[index] = char
            print(ListedWord)


    if guess not in ListedWord:
        if guess in failedGuesses:
            print(f"You already guessed {guess}")

        else:

            print(f"You guessed {guess} that is not in the list, you loose a live")
            failedGuesses.append(guess)
            print("You lost a live madafaker\n")
            print(stages[6 - counter])
            print(ListedWord)

            counter += 1







            

if active == True:
    print(f"You win!")







