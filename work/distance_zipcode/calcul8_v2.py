# import sys
import requests


api_key = "AIzaSyDjjm_CzfChp_BXFNVyzExYBtcYoPRA4UQ"

with open("clean_values.csv") as f:
	for i, line in enumerate(f):
		if i > 202 and i < 42000:
			zip_list = line.replace("\n","").split(",")
			r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + zip_list[0] + "&destinations=" + zip_list[1] + "&key=" + api_key)
			print zip_list
			if r.json()["status"] == "OK":
				if r.json()["rows"][0]["elements"][0]["status"] == "OK":
					write_this = str((float(r.json()["rows"][0]["elements"][0]["distance"]["value"])/1000) * 0.6213712)
				else:
					write_this = r.json()["rows"][0]["elements"][0]["status"]
				with open("out_v2.csv", "a") as outfile:
					outfile.write(str(zip_list[0]) + "," + str(zip_list[1]) + "," + write_this + "\n")
			else:
				print r.json()["status"]
				break
			print r.json()
