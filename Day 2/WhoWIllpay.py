
#Determine who's gonna pay the bill randomly

import random

friends = [
    "Jane",
    "John",
    "Mary",
    "Mike",
]



def get_random_friend():
    x = random.randint(1,4)
    index = x -1
    return friends[index]


print(get_random_friend())