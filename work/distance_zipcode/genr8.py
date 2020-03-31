import re
from subprocess import call,check_output
import requests

# call(["ls", "-l"]) # this is how to call system commands
api_key = "ujtZhtxIZku2ny8Cn3gXZGaumtnAvy3nWRyayiem83PTp1vcATGHwBnDhY1kCDpF"
ctr = 0
letters_regex = re.compile('[a-zA-Z]+')
# digits_only_regex = re.compile('^[0-9]+$')
# digits_only_regex = re.compile('[^\0-9\.]')
# digits_only_regex = re.compile('\D')

zips_compiled_dict = {}
with open("sample_csv.csv") as f:
	for i, line in enumerate(f):
		if i > 734 and i < 200000:
			zip_list = line.replace("\n","").split(",")
			if "," in line and len(zip_list) == 2 and letters_regex.match(zip_list[0]) is None and letters_regex.match(zip_list[1]) is None: # must have exactly 2 zips, neither of the zips containing letters
				a = re.sub("\D", "", zip_list[0])
				b = re.sub("\D", "", zip_list[1])
				if len(a) >= 5 and len(b) >= 5:
					# distance = check_output(["python", "calcul8.py", a[:5] , b[:5]])
					# with open("out.csv", "a") as outfile:
					# 	outfile.write(str(a) + "," + str(b) + "," + str(distance).strip() + "\n")
					if not str(b) in zips_compiled_dict:
						zips_compiled_dict[str(b)] = []
					zips_compiled_dict[str(b)].append({"a":str(a),"b":str(b)})
					# print  str(a) + "," + str(b) + "," + str(distance)
					ctr += 1
					# print ctr

# print zips_compiled_dict

for k in zips_compiled_dict:
	get_url = "https://www.zipcodeapi.com/rest/" + api_key + "/multi-distance.json/"
	print zips_compiled_dict[k]
	print k
	get_url += k + "/";
	for l in zips_compiled_dict[k]:
		# print l
		get_url += l["a"] + ","
	get_url = get_url[:-1] + "/mile"
	print get_url
	r = requests.get(get_url)
#	r = requests.get("https://www.zipcodeapi.com/rest/ujtZhtxIZku2ny8Cn3gXZGaumtnAvy3nWRyayiem83PTp1vcATGHwBnDhY1kCDpF/multi-distance.json/78723/33608,98448/mile")
	
	write_data = ""	

	if not "error_code" in r.json():
		save_json = r.json()["distances"]
		print save_json
		for m in save_json:
			write_data += k + "," + m + "," + str(save_json[m]) + "\n"
		print write_data
		with open("out.csv", "a") as outfile:
			outfile.write(write_data)
	else:
		save_json = r.json()["error_msg"]


	print save_json

