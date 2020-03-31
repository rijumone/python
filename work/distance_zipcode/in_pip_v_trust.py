# from geopy.geocoders import Nominatim
import os
# from subprocess import call,check_output
import pickle
import requests


# favorite_color = { "lion": "yellow", "kitty": "red" }

# pickle.dump( favorite_color, open( "save.p", "wb" ) )

# geolocator = Nominatim()

# open clean_values.csv file first
if os.path.isfile("zip_coords_dict_4.p"):
	zip_coords_dict = pickle.load(open("zip_coords_dict_4.p", "rb"))
else:
	zip_coords_dict = {}


# def do_geocode(zipp):
# 	# from geopy.geocoders import Nominatim
#     try:
#         return geolocator.geocode(zipp)
#     except:
#         check_output(['python','in_pip_v_trust.py'])


print zip_coords_dict



with open("clean_values.csv") as f:
	for i, line in enumerate(f):
		if i >= 40310 and i < 42000:
			zip_list = line.replace("\n","").split(",")
			for k in zip_list:
				if not k in zip_coords_dict or zip_coords_dict[k]["lat"] == "null" or zip_coords_dict[k]["lng"] == "null" or ("status" in zip_coords_dict[k] and zip_coords_dict[k]["status"] is not "ZERO_RESULTS") : # make hit to save data in pickle dict
				# if k in zip_coords_dict and "status" in zip_coords_dict[k] and zip_coords_dict[k]["status"] == "OVER_QUERY_LIMIT":
					api_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + k + "&key=AIzaSyDDLMsko0p5Fe34l-sU-b7LZ5pvvclXNWM"
					r = requests.get(api_url)
					print k
					# print location.encode('ascii', 'ignore')
					if r.json()['status'] == "OK":
						print r.json()
						zip_coords_dict[k] = {"lat":r.json()['results'][0]['geometry']['location']['lat'],"lng":r.json()['results'][0]['geometry']['location']['lng'], "status": r.json()['status']}
					else:
						print "!!!!!!!!!!!!!!!!!!!!!!!"
						print "STATUS NOT OK"
						print "!!!!!!!!!!!!!!!!!!!!!!!"
						print r.json()['status']
						print "!!!!!!!!!!!!!!!!!!!!!!!"
						zip_coords_dict[k] = {"lat":"null", "lng": "null", "status": r.json()['status']}
						# break
					pickle.dump(zip_coords_dict,open("zip_coords_dict_4.p","wb"))

					print zip_coords_dict
					print "=========================="
					print r.json()['status']
					print "=========================="
					print i
					print "=========================="


					