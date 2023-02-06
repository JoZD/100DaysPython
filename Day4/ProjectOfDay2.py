# ------------- This program is a password generator ---------------------------------------

# ------------- This program is a password generator ---------------------------------------
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', ';', ':', '\'', '"', '\\', '|', ',', '.', '<', '>', '/', '?']



password = []


askForLetters = int(input("How many letters would you like? "))
askForNumbers = int(input("How many numbers would you like? "))
askForSymbols = int(input("How many symbols would you like? "))

password = []


for char in range( 1, askForLetters +1): #last number is not included in the range, therefore it's necesarry to include +1 
    random.choice(letters) #As choice will pick just one character within the list, however; it is in a loop, therefore it will pick up askforLetters times
    password += random.choice(letters)

for integ in range( 1, askForNumbers +1):
    random.choice(numbers)
    password += random.choice(str(numbers))

for symbo in range( 1, askForSymbols +1):  
    random.choice(symbols)
    password += random.choice(symbols)

random.shuffle(password) #This code shuffles all characters within the list and with a simple for loop, we can create a pss




givenPassword = ""

for char in password:
    givenPassword += char #This code will take the shuffled list, and will create a string with that 



print(givenPassword) #Shows the final password  :) 

