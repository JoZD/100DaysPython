


# Loop from 1 to 100, and add all even numbers as a summatory


summatory = 0


#This little algorithm checks for the reminder of the tested number, if == 0, then it adds the number to the summatory

for number in range(1,101): #This also can be replaced as this: range(2,101,2) the t
    if number % 2 == 0:
        summatory += number

print(summatory)