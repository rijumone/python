raw = []
dataDict = {}

with open('x.csv', 'r') as x:
	x.readline() # skip header
	raw.extend(x.readlines()) 

with open('y.csv', 'r') as y:
	y.readline() # skip header
	raw.extend(y.readlines()) 

with open('z.csv', 'r') as z:
	z.readline() # skip header
	raw.extend(z.readlines()) 

for entry in raw:
	entryList = entry.split(",") 
	if not entryList[1] in dataDict:
		dataDict[entryList[1]] = []
	score = int(entryList[2].split("\n")[0])
	name = entryList[0].split(" ")[0].title() + " " + entryList[0].split(" ")[1].title()
	dataDict[entryList[1]].append({
		'name':name,
		'score':score,
		})				

# cs = 0
for section in dataDict:
	cs = 0
	for student in dataDict[section]:
		print student


print raw
print dataDict