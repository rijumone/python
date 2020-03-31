# list_files.py

import os
import sys
import glob
import time
import shutil
import subprocess

start_time = int(time.time())

SOURCE_DIR = '/home/riju/Kitchen/DataChannel'
DESTINATION_DIR = '/home/ubuntu/Kitchen/DataChannel'
SKIP_DIR_LiST = [
'.git',
'.pyc',
'facebook-python-ads-sdk-master',
]

def sync_dir_contents(source, destination, action_lst):
	for f in os.listdir(source):
		source_file_name = os.path.join(source, f)

		if 1 in action_lst:
			dest_file_name = source_file_name.replace(DESTINATION_DIR, SOURCE_DIR)
		else:
			dest_file_name = source_file_name.replace(SOURCE_DIR, DESTINATION_DIR)

		skip_found = False
		for skip_dir in SKIP_DIR_LiST:
			if skip_dir in source_file_name:
				skip_found = True
				break
		if not skip_found:		
			if os.path.isfile(source_file_name):
				if 0 in action_lst and 2 in action_lst:
					if (os.path.isfile(dest_file_name) and os.path.getsize(source_file_name) != os.path.getsize(dest_file_name)) or not os.path.isfile(dest_file_name):
						subprocess.call(['mkdir', '-p', '/'.join(dest_file_name.split('/')[:-1])])
						shutil.copy2(source_file_name, dest_file_name)
						subprocess.call(['chown', '-R', 'riju:riju', '/'.join(dest_file_name.split('/')[:-1])])
				if 1 in action_lst:
					if os.path.isfile(source_file_name) and not os.path.isfile(dest_file_name):
						os.remove(source_file_name)
				
			else:
				sync_dir_contents(source_file_name, destination, action_lst)

# case 0: file exists in SOURCE but not in DESTINATION, new file added, cp file
# case 2: file exists in both, check size, if different; copy
sync_dir_contents(SOURCE_DIR, DESTINATION_DIR, [0, 2, ], )



# case 1: file exists in DESTINATION but not in SOURCE, file deleted, rm file
sync_dir_contents(DESTINATION_DIR, SOURCE_DIR, [1, ])


end_time = int(time.time())
# print(end_time - start_time)