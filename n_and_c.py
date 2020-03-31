# print("x | o\n")

# print("  1   2   3")
# print("A x |   |")
# print("-----------")
# print("B o | x | o")
# print("-----------")
# print("C o |   | x")


gameList = [
			['x','o','x'],
			['o','o',' '],
			['x','o','x'],
		   ]

rowLetterMap = ["A","B","C"]

print("   1  2  3")
for rowIndice,row in enumerate(gameList):
	print(rowLetterMap[rowIndice]),
	for item in row:
		print " " + item,
	print ""


print(raw_input(""))
# arr[1][2]
gameOn = True

# while(gameOn):



print("x wins")