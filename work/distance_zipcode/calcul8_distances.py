import math
import pickle
 
def distance_on_unit_sphere(lat1, long1, lat2, long2):
	 
	# Convert latitude and longitude to
	# spherical coordinates in radians.
	degrees_to_radians = math.pi/180.0
	 
	# phi = 90 - latitude
	phi1 = (90.0 - lat1)*degrees_to_radians
	phi2 = (90.0 - lat2)*degrees_to_radians
	 
	# theta = longitude
	theta1 = long1*degrees_to_radians
	theta2 = long2*degrees_to_radians
	 
	# Compute spherical distance from spherical coordinates.
	 
	# For two locations in spherical coordinates
	# (1, theta, phi) and (1, theta', phi')
	# cosine( arc length ) =
	# sin phi sin phi' cos(theta-theta') + cos phi cos phi'
	# distance = rho * arc length
	 
	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
	math.cos(phi1)*math.cos(phi2))
	try:
	# Remember to multiply arc by the radius of the earth
	# in your favorite set of units to get length.
		distance = 3959 * math.acos(cos)  # this is arc
	except Exception as e:
		return "Exception!"
	
	 
	return distance

# print distance_on_unit_sphere(42.9024331,-76.5719414,29.84299339999999,-81.931657)*3959 #miles

zip_coords_dict = pickle.load(open("zip_coords_dict_4.p", "rb"))

with open("clean_values.csv") as f:
	for i, line in enumerate(f):
		if i >= 0 and i < 42000:
			zip_list = line.replace("\n","").split(",")
			for k in zip_list:
				if k in zip_coords_dict and "long" in zip_coords_dict[k]:
					print k
					zip_coords_dict[k]["lng"] = zip_coords_dict[k]["long"]
			if zip_list[0] != zip_list[1] and zip_list[0] in zip_coords_dict and zip_list[1] in zip_coords_dict and zip_coords_dict[zip_list[0]]["lat"] != "null" and zip_coords_dict[zip_list[0]]["lng"] != "null" and zip_coords_dict[zip_list[1]]["lat"] != "null" and zip_coords_dict[zip_list[1]]["lng"] != "null":
				print zip_list[0] + "," + zip_list[1]
				print zip_coords_dict[zip_list[0]]["lng"]
				lat1 = zip_coords_dict[zip_list[0]]["lat"]
				lng1 = zip_coords_dict[zip_list[0]]["lng"]
				lat2 = zip_coords_dict[zip_list[1]]["lat"]
				lng2 = zip_coords_dict[zip_list[1]]["lng"]
				distance = distance_on_unit_sphere(float(lat1),float(lng1),float(lat2),float(lng2))
				with open("out_v3.csv", "a") as outfile:
					outfile.write(str(zip_list[0]) + "," + str(zip_list[1]) + "," + str(distance) + "\n")