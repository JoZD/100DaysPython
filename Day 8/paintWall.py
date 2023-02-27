


#Calculate how many cans of paint are needed to paint a wall  1 can of paint = 5 m2




def calculate_howManyCans(wallHeight, wallWidth, coverage):
    numberOfcans = (int(wallHeight) * int(wallWidth)) / int(coverage)
    return numberOfcans



getHeight = input("Please enter the height of the wall you want to paint: \n")
getWidth = input("Please enter the width of the wall you want to paint: \n")
getCoverage = input("Please enter how many square meters can cover that can: \n")


print (f"{round(calculate_howManyCans(getHeight,getWidth,getCoverage))} are needed to paint that wall ")