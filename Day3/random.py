#The random module 

import random 


def random_number():
    return random.randint(1,100) # This line will generate a random number btween 1 and 99



def random_float():
    return random.random() # This will generate a random number between 0 and 0.99


x = random_number() 

print(x)

y = 4 *random_float()

print(y)