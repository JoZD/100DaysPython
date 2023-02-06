#Based on a list of grades, get the highest grade


grades = [90, 80, 85, 92, 88, 75, 95, 86, 70, 80, 95, 82, 89, 72, 78, 65, 87, 81, 92, 76, 99]


#This little algorithm will replace the value of the variable just in case that the last number is lower that the one that it's being evaluated
#otherwise, it won't change
highest_grade = 0 

for grade in grades:
    if grade > highest_grade:
        highest_grade = grade


print(highest_grade)


#This little algorithm will replace the value of the variable just in case that the last number is lower that the one that it's being evaluated             