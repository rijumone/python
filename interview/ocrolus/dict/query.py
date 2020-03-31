# query.py
import json

def query(query_type, q):
	if query_type not in ('count', ):
		print('query type not yet supported')
		return None
	count = 0
	for _class in data['classes']:
		for student in _class['students']:
			if student['name'].lower() == q.lower():
				count += 1

	return count


def group_by_name(class_name):
	return_this = {}
	for _class in data['classes']:
		if _class['name'] != class_name:
			continue
		for student in _class['students']:
			student_name = student['name']
			if student_name not in return_this:
				return_this[student_name] = 0
			return_this[student_name] += 1
		break

	return return_this




if __name__ == '__main__':
	data = None
	with open('in.json') as json_obj:
		data = json.loads(json_obj.read())
	print(json.dumps(data, indent=2))
	# input_lst = ['Riju']
	input_lst = ['I', 'II', 'III']
	for q in input_lst:
		# print(query('count', q))
		print(group_by_name(q))