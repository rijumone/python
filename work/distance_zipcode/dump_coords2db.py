import MySQLdb
import pickle
import traceback
import requests
import json

db = MySQLdb.connect("localhost","root","root","travel") # connect
cursor = db.cursor() # cursor


with open("clean_zips.csv") as f:
	for i,zipc in enumerate(f):	 # read new file line by line
		if i >= 10386: 
			sql = ("SELECT id,zip,status FROM zip_coords WHERE zip = %s;" %(zipc))
			cursor.execute(sql)
			results = cursor.fetchone()
			if results is None or (results is not None and results[2] == "OVER_QUERY_LIMIT"):	# zip doesn't exist in db
				api_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + zipc + "&key=AIzaSyBtszFihQ01dI9qWysKMETx41B4bnk7mdI"
				print("requesting coords from google api for zip: " + zipc)
				r = requests.get(api_url)
				print(r.json())
				with open("google_api_response.log","a") as log_file:
					print("writing last zip to file")
					log_file.write(zipc + "\n")
				if r.json()['status'] == "OK":
					lat = r.json()['results'][0]['geometry']['location']['lat']
					lng = r.json()['results'][0]['geometry']['location']['lng']
				else:
					lat = "0"
					lng = "0"
				sql = ("INSERT INTO `zip_coords` (`zip`, `lat`, `lng`, `source`, `status`, `response`) VALUES ('%s', '%s', '%s', 'google', '%s', '%s');" %(zipc, lat, lng, r.json()['status'], str(json.dumps(r.json())).replace("'","")))
				try:
				   	# Execute the SQL command
			   		cursor.execute(sql)
					# Commit your changes in the database
			   		db.commit()
				except:
				   # Rollback in case there is any error
				   	print "EXCEPTION!"
				   	print(traceback.format_exc())
				   	with open("google_api_response.log","a") as log_file:
						print("writing exception to file")
						log_file.write(str(traceback.format_exc()) + "\n")
				   	db.rollback()
			print("========================================= " + str(i) + " =========================================")
