# init.py

import sys
import subprocess

def init():
	subprocess.check_output([
		"python3", 
		"start_cities.py",
		"--loglevel=INFO",
		"--instance={0}".format(sys.argv[2]),
		"--loglocation={0}".format(sys.argv[1]),
		])
while True:
	try:
		init()
	except:
		init()