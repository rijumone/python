dataDict = {}

with open('data.csv', 'r') as x:
	fileList = x.readlines() 
	for line in fileList[1:]: #skip header:
		lineList = line.split(",") 
		if lineList[0] not in dataDict:
			dataDict[lineList[0]] = {}
		if 'n_ac' not in dataDict[lineList[0]]:
			dataDict[lineList[0]]['n_ac'] = 0
		if 'bal' not in dataDict[lineList[0]]:
			dataDict[lineList[0]]['bal'] = 0.0
		
		dataDict[lineList[0]]['n_ac'] += 1
		dataDict[lineList[0]]['bal'] += float(lineList[2])


with open('out.csv','w+') as o:
	o.writelines("Customerid,Num_accounts,Tot_balance\n")
	for cid in dataDict:
		o.writelines(cid + "," + str(dataDict[cid]['n_ac']) + "," + str(dataDict[cid]['bal']) + "\n" )

print "out.csv generated"