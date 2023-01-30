

#Type checking and type conversion


# if we want to use, for example, len(), it must be with a string, otherwise it will cause an error


x = "Jhon"
y = 10

print(len(x))

print(len(y)) # This will cause an error




#Checking the data type: 

print(type(x)) # String 
print(type(y)) #Integer


#If we want to get the lenght of an integer, we can create a new variable, and convert that integer to a string


integerToString = str(y) #This will allow you to use this as a string

#We can also convert a string to an integer 

a = "100"

float(a)
int(a)