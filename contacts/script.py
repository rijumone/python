headers = ["Name","Given Name","Additional Name","Family Name","Yomi Name","Given Name Yomi","Additional Name Yomi","Family Name Yomi","Name Prefix","Name Suffix","Initials","Nickname","Short Name","Maiden Name","Birthday","Gender","Location","Billing Information","Directory Server","Mileage","Occupation","Hobby","Sensitivity","Priority","Subject","Notes","Group Membership","E-mail 1 - Type","E-mail 1 - Value","Phone 1 - Type","Phone 1 - Value"]

# print headers

dataDict = {}

with open("exportinfo.csv") as file:  
	lineList = file.readlines()


for line in lineList:
	lineElements = line.replace("\n","").split(",")
	if lineElements[0].strip() != "name" and lineElements[0].strip() != "": 
		# print lineElements
		dataDict[lineElements[0].replace(" ","")+lineElements[3]+lineElements[4]]=lineElements



finalCsv = ""
		

for header in headers:
	finalCsv += header + ","

finalCsv = finalCsv.rstrip(",")
finalCsv += "\n"

for contact in dataDict:
	print contact
	# print dataDict[contact]
	finalCsv +=  dataDict[contact][0] + ",,,,,,,,,,,,,,," + dataDict[contact][1] + "," + dataDict[contact][5] + ",,,,,,,,,age: " + dataDict[contact][2] + ",,* ," +  dataDict[contact][4] + ",," + dataDict[contact][3] + "\n"

with open('p_sample_google_contact.csv', 'w') as f:
	f.write(finalCsv)

# print finalCsv

# print len(dataDict)