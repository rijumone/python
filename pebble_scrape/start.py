# print("start.py

import time
import pyautogui

wait_time = 2
print("Starting in {0} seconds.".format(wait_time))
time.sleep(wait_time)

ctr = 0
while True:
	ctr += 1
	for item in [(807,319), (1024,319), (1221,319)]:
		print("click on item")
		pyautogui.click(x=item[0], y=item[1])
		print("breathe")
		time.sleep(2)
		print("scroll down to bottom of page")
		pyautogui.press('end')
		print("wait for page to reset")
		time.sleep(2)
		print("click on download link")
		pyautogui.click(x=1006, y=515)
		print("wait for download page to load and download popup to appear")
		time.sleep(2)
		print("press enter")
		pyautogui.press('enter')
		print("breathe")
		time.sleep(2)
		# print("get focus back on browser")
		# pyautogui.click(x=178, y=269)
		print("navigate back")
		pyautogui.hotkey('alt', 'left')
		print("breathe")
		time.sleep(2)
	print("scroll down to next row")
	for _ in range(3):
		pyautogui.press('down')
		print("breathe")
		time.sleep(0.2)
	if ctr > 12:
		print("end reached, going to next page")
		pyautogui.click(x=1076, y=620)
		print("breathe")
		time.sleep(5)
		ctr = 0