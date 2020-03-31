import json


new_dict = {}

def get_keys(main_json1):
	# print main_json1
	for m in main_json1:
		# print m
		# print main_json1[m]
		# print len(main_json1[m])	
		# print type(main_json1[m])
		if type(main_json1[m]) is dict:
			# print("recurse")
			get_keys(main_json1[m])
			# print m
			# print main_json1[m]
		if " " in m:
			print m
			append_key = m.replace(" ","_")
		else:
			append_key = m
		# print append_key
		new_dict[append_key] = main_json1[m]

with open("Activities.txt") as in_file:
	main_json = json.loads(in_file.read())
	print type(main_json["activities_data"]) 
	for k in main_json["activities_data"]:
		# if(" " in k):
		# print main_json[k]	
		# print k
		get_keys(k)



print new_dict