import re

ctr = 0
letters_regex = re.compile('[a-zA-Z]+')

with open("raw_data.csv") as f:
	for i, line in enumerate(f):
		if i > 0 and i < 28000:
			zipc = line.replace("\n","")
			if letters_regex.match(zipc) is None : # zip should not contain letters
				zipc = re.sub("\D", "", zipc)
				if len(zipc) >= 5:
					with open("clean_zips.csv", "a") as outfile:
						outfile.write(str(zipc)[:5] + "\n")
			print("ctr:" + str(ctr))
			print("line number:" + str(i))