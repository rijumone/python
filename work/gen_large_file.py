#!/usr/bin/env python

"""
generates a humongous csv file taking in number of lines as sys.argv
"""

__author__ = "Riju"
__credits__ = ["Sandeep"]
__maintainer__ = "Riju"
__email__ = "rijumone.choudhuri@decision-tree.com"
__status__ = "Prototype"

import sys
import time
from random import randint
import math

started_timestamp = time.time()
sys_argv_dict = {}


def generate_file(n_lines, file_name):
	""" generate the file and save it line by line """
	with open(file_name, "w") as tmp:
		randint99 = randint(0, 99)
		randint999 = randint(0, 999)
		randint9999 = randint(0, 9999)
		for k in range(1):
			for x in range(math.ceil(n_lines/1)):
				# print("-- iteration: {0}".format(x))
				tmp.write("{0},{1},{2}\n".format(randint99, randint999, randint9999))
	

if __name__ == "__main__":
	# get n_lines from sys.argv
	for sys_argv in sys.argv:
		# print(sys_argv)
		if "=" in sys_argv :
			sys_argv_dict[sys_argv.split("=")[0].replace("--","")] = sys_argv.split("=")[1]
	generate_file(int(sys_argv_dict["n_lines"]), "/media/rijumone/A29659EE9659C387/logs/large.csv")

print("total time: {0} seconds".format(int(time.time() - started_timestamp)))