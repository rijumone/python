import datetime
from datetime import date

def calculate_age(born):
	today = date.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

dataDict = {}

with open('2.csv', 'r') as x:
	fileList = x.readlines() 
	for line in fileList[1:]: #skip header:
		lineList = line.split(",") 
		# print lineList
		salary = int(lineList[1])
		dob = lineList[2].split("\n")[0]
		if not dob == "":
			age = calculate_age(datetime.datetime.strptime(dob, '%d%b%Y').date())
		else:
			age = 100
		salary_remark = "Okay"
		if salary > 40000 and salary < 50000:
			salary_remark = "Growing"
		elif salary >= 50000:
			salary_remark = "Good enough"
		dataDict[lineList[0]] = {
									'salary':salary,
									'dob':dob,
									'age':age,
									'salary_remark' :salary_remark
									}

with open('out.csv','w+') as b:
	b.writelines("Name,Age,dob,Salary,SalaryRemark\n")
	for name in dataDict:
		b.writelines(name + "," + str(dataDict[name]['age']) + "," + dataDict[name]['dob'] + "," + str(dataDict[name]['salary']) + "," + dataDict[name]['salary_remark'] + "\n")

print "out.csv generated"
