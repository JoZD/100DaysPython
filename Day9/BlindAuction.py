import os



# Write a program for blind auction 

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

auctions = { }


print(logo)

while True:
    key = input("Please enter your name: ")
    value = input("Please enter your auction number: $")

    auctions[key] = value

    flag = input("Any other auction will be offered? y/n ")
    if flag == 'y':
        os.system('cls')
    elif flag == 'n':
        os.system('cls')
        break




#Look for the highest bidder
for key, value in auctions.items():
    if int(value) > winner:
        winner = int(value)


#Find the winner
print(winner)

for key, value in auctions.items():
    if int(value) == winner:
        print(f"The winner is {key} with an ammount of {value}!")


