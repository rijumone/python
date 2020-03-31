gameList = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

gameOn = True

def isGameStillOn():
	# first check for ties
	blankFound =  False
	for r in range(3):
		for c in range(3):
			if gameList[r][c] == " ":
				blankFound = True
	if blankFound:
		# check all rows
		for row in gameList:
			if row[0] != " " and row[0] == row[1] == row [2]:
				return {'winner': row[0]}
		# check all columns
		for c in range(3):
			if gameList[0][c] != " " and gameList[0][c] == gameList[1][c] == gameList[2][c]:
				return {'winner': gameList[0][c]}
		# check diagonal 1
		if gameList[0][0] != " " and gameList[0][0] == gameList[1][1] == gameList[2][2]:
			return {'winner': gameList[0][c]}
		# check diagonal 2
		if gameList[0][2] != " " and gameList[0][2] == gameList[1][1] == gameList[2][0]:
			return {'winner': gameList[0][c]}

		return True
	else:
		return {'winner': 'tie'}		

while(gameOn):
	print "enter x or o as <value> <row> <column>"
	pInput = raw_input()
	pInput = pInput.split(" ") 
	if gameList[int(pInput[1])][int(pInput[2])] == " ":
		gameList[int(pInput[1])][int(pInput[2])] = pInput[0]
		for row in gameList:
			print row
		
		value = isGameStillOn()
		if type(value) is dict:
			print "winner is " + value['winner']
			gameOn = False
		else:
			gameOn = True
	else: 
		print "can't overwrite already filled slot"