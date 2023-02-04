

#More practices with lists, this is a treasure map, that allows you to hide a treasure

print("\n\n")
row1 = ["🍀","🍀","🍀"]     # 1 2 
row2 = ["🍀","🍀","🍀"]
row3 = ["🍀","🍀","🍀"]

map = [row1, row2, row3]




position = input("Where do you want to hide the treasure? Please use the format colum, row eg. 23 (Colum 2, row 3): \n")

treasure = "X"


index = int(position) - 11

indexstr = [int(d) for d in str(index)] # This converts every d in  index, that previously was defined as string 

print(index)

print(f"The treasure will be placed at position {position}")

map[int(indexstr[1])][int(indexstr[0])]  = treasure

print(f"{row1}\n {row2}\n {row3}")

