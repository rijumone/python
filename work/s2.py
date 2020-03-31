import json

def change_dict_naming_convention(d, convert_function):
    """
    Convert a nested dictionary from one convention to another.
    Args:
        d (dict): dictionary (nested or not) to be converted.
        convert_function (func): function that takes the string in one convention and returns it in the other one.
    Returns:
        Dictionary with the new keys.
    """
    new = {}
    for k, v in d.iteritems():
        new_v = v
        if isinstance(v, dict):
            new_v = change_dict_naming_convention(v, convert_function)
        elif isinstance(v, list):
            new_v = list()
            for x in v:
            	if type(x) is not int:
                	new_v.append(change_dict_naming_convention(x, convert_function))
        new[convert_function(k)] = new_v
    return new


def convert_function(str):
	return str.replace(" ","_")


with open("Activities.txt") as in_file:
	main_json = json.loads(in_file.read())
	with open("out.json","a") as out_file:
		out_file.write(json.dumps(change_dict_naming_convention(main_json,convert_function)))