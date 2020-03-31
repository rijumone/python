import time
import subprocess

print('Starting to capture in 20 seconds')
time.sleep(20)
while True:
	print('Capturing...')
	
	cmd = [
		'adb',
		'shell',
		'input',
		'tap',
		'543',
		'1832',
		]
	print(' '.join(cmd))
	subprocess.call(cmd)

	print('Sleeping for 31 seconds...')
	time.sleep(31)


	cmd = [
		'adb',
		'shell',
		'input',
		'tap',
		'957',
		'1861',
		]
	print(' '.join(cmd))
	subprocess.call(cmd)

	print('Sleeping for 0.5 seconds...')
	time.sleep(0.5)

	cmd = [
		'adb',
		'shell',
		'input',
		'keyevent',
		'KEYCODE_BACK',
		]
	print(' '.join(cmd))
	subprocess.call(cmd)

	print('Sleeping for 0.5 seconds...')
	time.sleep(0.5)