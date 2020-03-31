

# read the file
# get count of lines in file
# get 50 random data
# hit zipcode api
# save data and difference in separate file

from random import randint
import requests

unique_random_int_list = []
api_key = "uwLFPdNIJDD2yVWKJpfrYkdnKHxhO548Yp91WcKlorhxv11hcw5g3k83yJCXLxjk"

with open('out_v3.csv') as f:
	n_lines = sum(1 for _ in f)
	# generate 50 unique random numbers
	while len(unique_random_int_list) < 50:
		random_int = randint(1, n_lines)
		if random_int not in unique_random_int_list:
			unique_random_int_list.append(random_int)
	# print unique_random_int_list
with open('out_v3.csv') as f:	
	for i, line in enumerate(f):
		# print i
		if i in unique_random_int_list:
			# hit zipcode api
			zip_list = line.replace("\n","").split(",")
			print(zip_list)
			r = requests.get("https://www.zipcodeapi.com/rest/" + api_key + "/distance.json/" + zip_list[0] + "/" + zip_list[1] + "/mile")
			write_this = ""
			diff = "N/A"
			if not "error_code" in r.json():
				write_this = r.json()["distance"]
				diff = float(zip_list[2]) - write_this
			else:
				write_this = r.json()["error_msg"]
			with open("verify_data_v3.csv", "a") as outfile:
				outfile.write(str(zip_list[0]) + "," + str(zip_list[1]) + "," + str(zip_list[2]) + "," + str(write_this) + "," + str(diff) + "\n")
			print(str(zip_list[0]) + "," + str(zip_list[1]) + "," + str(zip_list[2]) + "," + str(write_this) + "," + str(diff) + "\n")

print("DONE")