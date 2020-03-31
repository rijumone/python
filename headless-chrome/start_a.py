import os  
import time
import random
import traceback
import pytesseract
from PIL import Image
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


out_of_swipes = False

chrome_options = Options()  
# chrome_options.add_argument("--headless")  # toggle this for headless
# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),chrome_options=chrome_options)  
driver.get("https://www.facebook.com")
driver.save_screenshot("facebook.png")

# launch facebook to login

email_field = driver.find_element_by_id("email")
email_field.clear()  
email_field.send_keys("neter.sagar")

password_field = driver.find_element_by_id("pass")
password_field.clear()  
with open("pass.txt") as pass_txt:
    # print(pass_txt.read())
    password_field.send_keys(pass_txt.read())

login_field = driver.find_element_by_id("loginbutton")
login_field.click
print("waiting for 10 secondss")
time.sleep(10)
driver.save_screenshot("facebook_login_enter.png")
#browser.switch_to_window(main_window)
# launch tinder
driver.get("https://www.tinder.com")
driver.save_screenshot("tinder.png")
# driver.set_window_size(1024, 768)

to_click_btns = (
    {"name":"login_btn","x_path": '//*[@id="modal-manager"]/div/div/div[2]/div[1]/div/div[3]/button[1]'},
    {"name":"next","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div[1]/div[1]/div/button'},
    {"name":"get_started","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div/main/div/button'},
    {"name":"great_btn","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]'},
    {"name":"ok_got_it","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]'},
)
# 
# magnifying_glass = driver.find_element_by_id("js-open-icon")  
# magnifying_glass = driver.find_element_by_class_name("button__text")  

try:
    for btn in to_click_btns:
        print(btn["name"])
        # print(to_click_btns[btn])
        driver.save_screenshot("{0}.png".format(btn["name"]))
        btn_to_click = WebDriverWait(driver, 10).until(
 #           EC.presence_of_element_located((By.XPATH, btn["x_path"]))
        )
        btn_to_click.click()  
        time.sleep(2)
        driver.save_screenshot("{0}_after.png".format(btn["name"]))
    # time.sleep(99999)
    while not out_of_swipes:
        driver.find_element_by_tag_name('body').send_keys(Keys.RIGHT) 
        time.sleep(random.uniform(0.578, 1.1058))
        driver.save_screenshot("swipe.png")
        img = Image.open("swipe.png")
        img2 = img.crop((420, 120, 620, 160))
        img2.save("swipe_cropped.png")
        dump = pytesseract.image_to_string(Image.open("swipe_cropped.png"))
        if "out of likes" in dump:
            out_of_swipes = True
    # driver.set_window_size(1224, 768)
    # great_btn = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]'))
    # )
    # great_btn.click()  
finally:
    driver.quit()
    # pass


# exit()

"""
if login_btn.is_displayed():  
  login_btn.click()  
else:  
  menu_button = driver.find_element_by_css_selector(".menu-trigger.local")  
  menu_button.click()

email_field = driver.find_element_by_id("email")  
# search_field = driver.find_element_by_id("site-search")  
search_field.clear()  
search_field.send_keys("Olabode")  
search_field.send_keys(Keys.RETURN)  
assert "Looking Back at Android Security in 2016" in driver.page_source
driver.close()
"""
