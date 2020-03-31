import pickle

zip_coords_dict = pickle.load(open("zip_coords_dict_2.p", "rb"))

for k in zip_coords_dict:
	if "long" in zip_coords_dict[k]:
		zip_coords_dict[k]["lng"] = zip_coords_dict[k]["long"]

pickle.dump(zip_coords_dict,open("zip_coords_dict_3.p","wb"))		