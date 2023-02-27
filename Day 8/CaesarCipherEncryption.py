
from art import logo


# Encryption and  decryption with ceaser cipher encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b',
             'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd',
               'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar (text, shift, direction):
    """Encrypt or decrypt a message"""

    encryptedWord = ""

    for char in text:
        if direction == 'encode':
            index = 0
            if char in alphabet:
                index = alphabet.index(char)
                index = index + shift
                encryptedWord += alphabet[index]
            else:
                encryptedWord += char

        elif direction == 'decode':
            index = 0
            if char in alphabet:
                index = alphabet.index(char)
                index = index - shift
                encryptedWord += alphabet[index]
            else:
                encryptedWord += char
        


    print(encryptedWord) 




def play ():
    print(f"{logo} \n \n \n")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    flag = input("\n Do you want to run the program again y/n ?: ")

    if flag == 'y':
        play()
    else:
        print("Ok! See you later uwu")
    

play()



        
        


