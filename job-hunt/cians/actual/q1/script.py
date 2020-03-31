dataDict = {}

with open('x.csv', 'r') as x:
	fileList = x.readlines() 
	for line in fileList[1:]: #skip header: 
		dataDict[line.split(",")[0].title()] = line.split(",")[1].split("\n")[0]

with open('y.csv', 'r') as x:
	fileList = x.readlines() 
	for line in fileList[1:]: #skip header: 
		dataDict[line.split(",")[0].title()] = line.split(",")[1].split("\n")[0]


with open('a.csv','w+') as a:
	a.writelines("Name,Age\n")
	for name in dataDict:
		a.writelines(name + "," + dataDict[name] + "\n") 

print "a.csv generated"


with open('z.csv', 'r') as x:
	fileList = x.readlines() 
	for line in fileList[1:]: #skip header:
		age = ""
		if line.split(",")[0].title() in dataDict:
			age =  dataDict[line.split(",")[0].title()]
		dataDict[line.split(",")[0].title()] = age + "|" + line.split(",")[1].split("\n")[0]



with open('b.csv','w+') as b:
	b.writelines("Name,Age,Salary\n")
	for name in dataDict:
		nameAgeList = dataDict[name].split("|")
		age = nameAgeList[0]
		if len(nameAgeList) > 1:
			salary = dataDict[name].split("|")[1]
		else:
			salary = ""
		if age != "" and salary != "":
			b.writelines(name + "," + age + "," + salary + "\n")

print "b.csv generated"

with open('c.csv','w+') as c:
	c.writelines("Name,Age,Salary\n")
	for name in dataDict:
		nameAgeList = dataDict[name].split("|")
		age = nameAgeList[0]
		if len(nameAgeList) > 1:
			salary = dataDict[name].split("|")[1]
		else:
			salary = ""
		c.writelines(name + "," + age + "," + salary + "\n")

print "c.csv generated"

with open('d.csv','w+') as d:
	d.writelines("Name,Age,Salary\n")
	for name in dataDict:
		nameAgeList = dataDict[name].split("|")
		age = nameAgeList[0]
		if len(nameAgeList) > 1:
			salary = dataDict[name].split("|")[1]
		else:
			salary = ""
		if (age == "" and salary != "")or(age != "" and salary == "") :
			d.writelines(name + "," + age + "," + salary + "\n")

print "d.csv generated"


