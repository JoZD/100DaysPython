#Playing rock paper scissors 


import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


selection = input("Welcole to Rock, paper scissors: Please, select 1 for rock, 2 for paper or 3 for scissors: \n") # Select input  from user 

hand = int(selection) 
if hand == 1:
    print(f"Your choice: \n {rock}")
elif hand == 2:
    print(f"Your choice: \n {paper}")
elif hand == 3:  
    print(f"Your choice: \n {scissors}")


computerchoise = random.randint(1,3) #Select input from computer based on random 

if computerchoise == 1:
    print(f"Computer choice: \n {rock}")
elif computerchoise == 2:
    print(f"Computer choice: \n {paper}")
elif computerchoise == 3:
    print(f"Computer choice: \n {scissors}")



#Determine a winner 

#Draw scenarios 


if computerchoise == 1 and hand == 1:
    print(f"\n Draw!")

elif computerchoise == 2 and hand == 2:
    print(f"\n Draw!")

elif computerchoise == 3 and hand == 3:
    print(f"\n Draw!")

#Computer win scenarios 

elif computerchoise == 1 and hand == 2:
    print(f"You win! :D")


elif computerchoise == 1 and hand == 3:
    print(f"Computer wins! ):")


elif computerchoise == 2 and hand == 1:
    print(f"Computer wins! ):")

elif computerchoise == 2 and hand == 3:
    print(f"You win! :D")


elif computerchoise == 3 and hand == 1:
    print(f"You win! :D")


elif computerchoise == 3 and hand == 2:
    print(f"Computer wins! ):")


