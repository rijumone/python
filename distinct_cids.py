with open("cIDs.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

distint_list = []

for cid in content :
	if not cid in distint_list:
		distint_list.append(cid)


# print(distint_list)

f = open('d_cids.txt', 'w')

for d_cid in distint_list:
	f.write(d_cid + '\n')  
	
f.close()