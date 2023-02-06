


#This program will print numbers from 1 to 100
# If the number is divisible by 5, print buzz instead of the number
# If the number is divisible by 3, print fizz instead of the number
# If the number is divisible by 3 and 5 print fizzbuzz instead of the number



for i in range(1,101):

    if i % 5 == 0 and i % 3 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)