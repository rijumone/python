# start_ultd_simple.py

import os
import time
from random import randint, uniform
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()  
# chrome_options.add_argument("--headless")  # toggle this for headless
# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),chrome_options=chrome_options)  
driver.get("https://www.tinder.com")

print('press Enter to continue')
input()

while True:
	time.sleep(uniform(0.2, 0.5))
	if os.path.exists(os.path.abspath("k.s")):
		driver.find_element_by_tag_name('body').send_keys(Keys.RIGHT) 
