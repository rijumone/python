# phonebook2.py
__author__ = 'Riju'
__email__ = 'rijumone@live.com'

import os
import re
import csv
import time
import pickle
# from pprint import pprint
from loguru import logger
from abc import ABCMeta, abstractmethod
logger.add("log.log", compression="zip", rotation="10 MB")
PHONE_NUMBER_PATTERN = '^(\+0?1\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'

class PhonebookEntry:
	'''class to emulate phonebook entry'''
	state = None
	last_name = None
	first_name = None
	phone_number = None

	def __init__(self, first_name, last_name, state, phone_number):
		self.state = state
		self.last_name = last_name
		self.first_name = first_name
		self.phone_number = self._transform_phone_number(phone_number)

	def __repr__(self):
		return '<PhonebookEntry({}, {}, {}, {}>'.format(
			self.first_name, 
			self.last_name, 
			self.state, 
			self.phone_number,
			)

	def _transform_phone_number(self, phone_number):
		''' return phone number as string
		in the format: (917) 958-1191 '''
		phone_number = phone_number.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
		_tmp = '(' + phone_number[:3] + ') ' + phone_number[3:6] + '-' + phone_number[6:]
		return _tmp
		


class Phonebook:
	phonebook = None
	

	def __init__(self):
		self.phonebook = {}

	def insert(self, row):
		# attempt to identify row's format
		key = None
		state = None
		last_name = None
		first_name = None
		phone_number = None

		
		if len(row) < 3 or len(row) > 4:
			return
		

	
		pattern_matched = False
		for child_class in RowMatcher.__subclasses__():
			if child_class.condition():
				pattern_matched = True
				child_class.action()
				break
		if not pattern_matched:
			raise Exception('unable to parse row'.format(str(row)))
		key = child_class.key
		first_name = child_class.first_name
		last_name = child_class.last_name
		phone_number = child_class.phone_number
		state = child_class.state
			

		if key is not None:
			if key not in self.phonebook:
				self.phonebook[key] = []
			self.phonebook[key].append(PhonebookEntry(first_name, last_name, state, phone_number))

	def search(self, search_key):
		search_key_l = search_key.lower()
		return self.phonebook[search_key_l] if search_key_l in self.phonebook else None

	def __repr__(self):
		return '<Phonebook(phonebook={})>'.format(self.phonebook)

class RowMatcher(metaclass=ABCMeta):
	row, key, first_name, last_name, phone_number, state = None, None, None, None, None, None
	@abstractmethod
	def condition(self):
		pass
	@abstractmethod
	def action(self):
		pass

class Pattern1(RowMatcher):
	def condition(self, row):
		self.row = row
		# if there are only 3 items in the line, it is of format: Firstname Lastname, 9179581191, New York
		if len(row) == 3:
			return True
	def action(self):
		self.key = row[0].split(' ')[1].lower()
		self.first_name = row[0].split(' ')[0].strip()
		self.last_name = row[0].split(' ')[1].strip()
		self.phone_number = row[1].strip()
		self.state = row[2].strip()

class Pattern2(RowMatcher):
	def condition(self, row):
		self.row = row
		# if third value matches phone number
		if re.match(PHONE_NUMBER_PATTERN, row[2].strip()):
			return True
	def action(self):
		self.key = row[1].strip().lower()
		self.first_name = row[0].strip()
		self.last_name = row[1].strip()
		self.phone_number = row[2].strip()
		self.state = row[3].strip()

class Pattern3(RowMatcher):
	def condition(self):
		self.row = row
		# if fourth value matches phone number
		if re.match(PHONE_NUMBER_PATTERN, row[3].strip()):
			return True
	def action(self):
		self.key = row[0].strip().lower()
		self.first_name = row[1].strip()
		self.last_name = row[0].strip()
		self.phone_number = row[3].strip()
		self.state = row[2].strip()

def search_and_print(cleaned_line, pb_obj):
	search_results = pb_obj.search(cleaned_line)
	print('Matches for {}'.format(cleaned_line))
	if search_results is None:
		print('No results found')
	else:
		ctr = 0
		for result in search_results:
			ctr += 1
			print('Result {ctr}: {last_name}, {first_name}, {state}, {phone}'.format(
				ctr=ctr,
				last_name=result.last_name,
				first_name=result.first_name,
				state=result.state,
				phone=result.phone_number,
				))


def main():

	if os.path.isfile('pb_obj.pickle') and os.path.getmtime('phone_dataset.csv') <= os.path.getmtime('pb_obj.pickle'):
		# pickle can be used
		with open('pb_obj.pickle', 'rb') as pickle_file_obj:
			pb_obj = pickle.load(pickle_file_obj)
	else:
		with open('phone_dataset.csv') as in_file:
			pb_obj = Phonebook()
			reader = csv.reader(in_file)
			for row in reader:
				pb_obj.insert(row)

		# write pickle to file here
		with open('pb_obj.pickle', 'wb') as pickle_file_obj:
			pickle.dump(pb_obj, pickle_file_obj) 

	with open('query.txt') as query_file:
		for line in query_file.readlines():
			search_and_print(line.strip(), pb_obj)
			


if __name__ == '__main__':
	main()
	
"""
foo,abc,999999
foo,abc2,999999
foo,abc1,999999
foo,abc5,999999

{
    abc: {foo,abc,999999}
}


search_files/
    /a
        /bc5.txt
        foo,abc5,999999

        /bc.txt
        foo,abc,999999


trie

a
\
 --

aaron
"""