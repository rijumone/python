with open("cookies_with_transaction_after_17_which_had_cross_raw.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 

# print(content)

# f = open('cookies_with_transaction_after_17.txt', 'w')

mobileList = []

# line2write = "mobileNum,cookieID\n"

for line in content:
	if not line in mobileList:
		mobileList.append(line)

# print(mobileList)
# print(len(mobileList))

for num in mobileList:
	print(num)

# f.close()
