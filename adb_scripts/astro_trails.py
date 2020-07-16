import time
import subprocess
from loguru import logger

logger.add('astro.log')

logger.info('Starting to capture in 10 seconds')
time.sleep(20)
ctr = 0
while True:
	ctr += 1
	logger.info('Capturing {}...'.format(ctr))
	
	cmd = [
		'adb',
		'shell',
		'input',
		'tap',
		'543',
		'1832',
		]
	logger.info(' '.join(cmd))
	subprocess.call(cmd)

	logger.info('Sleeping for 31 seconds...')
	time.sleep(31)


	cmd = [
		'adb',
		'shell',
		'input',
		'tap',
		'957',
		'1861',
		]
	logger.info(' '.join(cmd))
	subprocess.call(cmd)

	logger.info('Sleeping for 0.5 seconds...')
	time.sleep(0.5)

	cmd = [
		'adb',
		'shell',
		'input',
		'keyevent',
		'KEYCODE_BACK',
		]
	logger.info(' '.join(cmd))
	subprocess.call(cmd)

	logger.info('Sleeping for 0.5 seconds...')
	time.sleep(0.5)
