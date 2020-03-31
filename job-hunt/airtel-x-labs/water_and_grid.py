"""
There is a place in the form of M x N grid where each cell has either a tower
built on it or is empty. Each cell is a square of unit area and each tower
has height of 1 unit.

You are required to estimate the volume of water that could be trapped in 
between the towers.
- Water will be trapped only if it does not reach to the edges and flows out
- The towers are not porous i.e. water can not flow through the towers

INPUT
The first line will contain two integers M and N
The following M lines will contain a string each of length N denoting a 
grid of size M x N where * denotes that cell has a tower built on it 
and . denotes that it is empty

OUTPUT
Output would contain the volume of water trapped

Sample input                                    Sample output
4 4                                             3
.**.                                            
*.*.
*..*
****
"""

from pprint import pprint

def _gautam():
	def is_enclosed(test_matrix, enclosed_points, open_points, is_calculated, point):
	    # Terminating conditions first
	    # print(point)
	    is_calculated.add(point)
	    if point in open_points:
	        return False

	    if test_matrix[point[0]][point[1]] == '*':
	        return True

	    enclosed = True
	    # Check the down
	    if point[1]+1 < len(test_matrix[0]) and not is_enclosed(test_matrix, enclosed_points, open_points, is_calculated, (point[0], point[1]+1)):
	        enclosed = False
	    # Check the right
	    if point[0]+1 < len(test_matrix[0]) and not is_enclosed(test_matrix, enclosed_points, open_points, is_calculated, (point[0]+1, point[1])):
	        enclosed = False

	    if enclosed:
	        enclosed_points.add(point)
	    else:
	        open_points.add(point)

	    return enclosed

	enclosed_points = set()

	is_calculated = set()
	open_points = set()

	test_matrix = [
	    ['.', '*', '*', '.', '*'],
	    ['*', '.', '*', '.', '*'],
	    ['*', '.', '.', '*', '*'],
	    ['*', '.', '*', '*', '*'],
	    ['*', '*', '*', '*', '*'],
	]

	# With assumption that it will be a square matrix
	size_row = len(test_matrix[0])

	for row_number in range(0, size_row, size_row-1):
	    for column in range(0, size_row):
	        if test_matrix[column][row_number] == '.':
	            open_points.add((column, row_number))

	        if test_matrix[row_number][column] == '.':
	            open_points.add((row_number, column))

	for i in range(size_row):
	    for j in range(size_row):
	        if (i, j) in is_calculated:
	            continue
	        else:
	            is_enclosed(test_matrix, enclosed_points, open_points, is_calculated, (i, j))


	print("Enclosed area is :- ", len(enclosed_points), "Units")

def _riju():
	
	class Unit():
		# up, down, left, right = None, None, None, None
		row, column = None, None
		is_tower = None


		def __init__(self, **kwargs):
			# self.up = kwargs.get('up', None)
			# self.down = kwargs.get('down', None)
			# self.left = kwargs.get('left', None)
			# self.right = kwargs.get('right', None)
			self.row = kwargs.get('row', None)
			self.column = kwargs.get('column', None)
			self.is_tower = kwargs.get('is_tower', False)

		def get_address(self):
			return self.row, self.column

		def __repr__(self):
			# return '<Unit up={}, down={}, left={}, right={}, is_tower={}, row={}, column={}>'.format(
			return '<Unit is_tower={}, row={}, column={}>'.format(
				# self.up,
				# self.down,
				# self.left,
				# self.right,
				self.is_tower,
				self.row,
				self.column,
				)


	lst = []
	n_rows, n_columns = tuple([int(_) for _ in input().split(' ')])
	for row in range(n_rows):
		column = 0
		for _input in input():
			# print(_input)
			if _input == '.':
				lst.append(Unit(
					row=row,
					column=column,
					))
			else:
				lst.append(Unit(
					is_tower=True,
					row=row,
					column=column,
					))
			column += 1

	# pprint(lst)
	# now set up neighbours
	"""
	for unit in lst:
		print(unit.get_address())

		# print('up address should be:')
		# print((unit.row)-1, unit.column)
		if (unit.row)-1 >= 0:
			unit.up = [_ for _ in lst if _.row == (unit.row)-1 and _.column == unit.column][0]
		if (unit.row)+1 <= n_rows-1:
			unit.down = [_ for _ in lst if _.row == (unit.row)+1 and _.column == unit.column][0]
		print(unit)
		print('==============')

		
	"""
	total_blocked_units = 0
	for unit in lst:
		if unit.is_tower:
			continue
		# check neighbors
		found_block_ctr = 0
		# up
		for check_unit in lst:
			if check_unit.column == unit.column:	
				if check_unit.row < unit.row:
					if check_unit.is_tower:
						found_block_ctr += 1
						break
		# down
		for check_unit in lst:
			if check_unit.column == unit.column:	
				if check_unit.row > unit.row:
					if check_unit.is_tower:
						found_block_ctr += 1
						break

		# left
		for check_unit in lst:
			if check_unit.row == unit.row:	
				if check_unit.column < unit.column:
					if check_unit.is_tower:
						found_block_ctr += 1
						break
		# right
		for check_unit in lst:
			if check_unit.row == unit.row:	
				if check_unit.column > unit.column:
					if check_unit.is_tower:
						found_block_ctr += 1
						break

		if found_block_ctr == 4:
			total_blocked_units += 1
		
	print(total_blocked_units)


if __name__ == '__main__':
	# _gautam()
	_riju()