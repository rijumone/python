# genr8_yahoo_gemini_fields.py
"""
[input]
	Field name1\n
	Field name2
[output]
	[
		{
			"field": "Field Name1"
		},
		{
			"field": "Field Name2"
		}
	]
"""
import json
raw_fields_lst = []
input_r = input()
while input_r != "":
	raw_fields_lst.append(input_r.strip("\n").strip("\t").strip(" "))
	input_r = input()
	# print(raw_fields_lst)

output_lst = []

# print()

for raw_field in raw_fields_lst:	
	output_lst.append({
		"field": ' '.join(s[:1].upper() + s[1:] for s in raw_field.split(' '))
		})

print(json.dumps(output_lst,indent=2))