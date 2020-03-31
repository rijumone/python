with open("pseudo_data.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

# print(content)

f = open('final_report.csv', 'w')

# for d_cid in distint_list:

	
line2write = "mobileNum,cookieID\n"

for line in content:
	temp = line.split(":")
	# print(temp)
	
	if temp[0]=="mobileNum":
		line2write = line2write + temp[1]
	if temp[0]=="cookieID":

		line2write = line2write + "," + temp[1]
		# print(line2write)
		f.write(line2write + '\n')
		line2write = ""
	

f.close()
