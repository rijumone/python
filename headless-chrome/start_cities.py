import os  
import sys
import time
import random
import logging
import traceback
import pytesseract
from PIL import Image
import logging.handlers
from scipy.misc import imread
from scipy.linalg import norm
from scipy import sum, average
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def compare_images(img1, img2):
    # normalize to compensate for exposure difference
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng



started_timestamp = time.time()
instance_compare_file = "{0}.png".format(str(int(started_timestamp)))

# build sys.argv dict
args_dict = {}
for arg in sys.argv:
    if "--" in arg and "=" in arg:
        args_dict[arg.split("=")[0].replace("--","")] = arg.split("=")[1]

# get logging level
loglevel = args_dict["loglevel"] if "loglevel" in args_dict else "DEBUG"

# logging basic configuration   
root = logging.getLogger()

# adding handler to stdout as well
ch = logging.StreamHandler(sys.stdout)
# adding rotation
handler = logging.handlers.RotatingFileHandler(filename="/{1}/log/TinAuto/start_{0}.log".format(args_dict["instance"], args_dict["loglocation"]), maxBytes=1024*1024*3, backupCount=99)
# defining the format
formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s','%m/%d/%Y %H:%M:%S')
ch.setFormatter(formatter)
handler.setFormatter(formatter)
root.setLevel(loglevel)
ch.setLevel(loglevel)
root.addHandler(ch)
root.addHandler(handler)

logging.info("Start!")
# logging.info("Creating instance_compare_file")

out_of_swipes = False
n_swipe_in_city_ctr = 0
n_swipe_total = 0
cities_lst = []
with open("cities.txt") as cities_txt:
    cities_lst = cities_txt.read().split("\n")

# logging.info(cities_lst)
# exit()
chrome_options = Options()  
# chrome_options.add_argument("--headless")  # toggle this for headless
# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),chrome_options=chrome_options)  
driver.get("https://www.facebook.com")
# driver.save_screenshot("facebook.png")

# launch facebook to login

email_field = driver.find_element_by_id("email")
email_field.clear()  
email_field.send_keys("rijumone")

password_field = driver.find_element_by_id("pass")
password_field.clear()  
with open("pass.txt") as pass_txt:
    # logging.info(pass_txt.read())
    password_field.send_keys(pass_txt.read())

email_field.send_keys(Keys.RETURN)
# driver.save_screenshot("facebook_login_enter.png")

# launch tinder
driver.get("https://www.tinder.com")
# driver.save_screenshot("tinder.png")
# driver.set_window_size(1024, 768)

to_click_btns = (
    {"name":"login_btn","x_path": '//*[@id="modal-manager"]/div/div/div[2]/div[1]/div/div[3]/button[1]'},
    {"name":"next","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div[1]/div[1]/div/button'},
    {"name":"get_started","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div/main/div/button'},
    {"name":"great_btn","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]'},
    {"name":"ok_got_it","x_path": '//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]'},
)
"""
magnifying_glass = driver.find_element_by_id("js-open-icon")  
magnifying_glass = driver.find_element_by_class_name("button__text")  
profile
//*[@id="content"]/div/span/div/div[1]/div/aside/div/a
tinder + 
//*[@id="content"]/div/span/div/div[1]/div/aside/nav/div/div/div/div/div/div/div[1]/a
current location
//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[2]/section[1]/div[1]/div/div[2]/a
search a location
//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[5]/div/div/span[2]/div/div[1]/input
first result
//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[5]/div/div/span[2]/div/div[2]/div[1]
location on map
//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[2]/div[3]
"""
try:
    for btn in to_click_btns:
        logging.info(btn["name"])
        # logging.info(to_click_btns[btn])
        # driver.save_screenshot("{0}.png".format(btn["name"]))
        btn_to_click = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, btn["x_path"]))
        )
        btn_to_click.click()  
        time.sleep(2)
        # driver.save_screenshot("{0}_after.png".format(btn["name"]))
    # time.sleep(99999)
    while not out_of_swipes:
        for city in cities_lst:
            time.sleep(random.uniform(2.758, 3.058))
            driver.find_element_by_tag_name('body').send_keys(Keys.RIGHT) 
            n_swipe_in_city_ctr += 1
            n_swipe_total += 1
            logging.info("n_swipe city: {0}".format(n_swipe_in_city_ctr))
            logging.info("n_swipe total: {0}".format(n_swipe_total))
            driver.save_screenshot("{0}_swipe.png".format(instance_compare_file.replace(".png","")))
            img = Image.open("{0}_swipe.png".format(instance_compare_file.replace(".png","")))
            # check if out of likes; obsolete in tinder gold
            # img2 = img.crop((420, 120, 620, 160))
            # img2.save("{0}_swipe_cropped.png".format(instance_compare_file))
            # dump = pytesseract.image_to_string(Image.open("{0}_swipe_cropped.png".format(instance_compare_file)))
            # if "out of likes" in dump:
            #     out_of_swipes = True
            # now check if there is anyone around
            img2 = img.crop((632, 140, 732, 240))
            img2.save(instance_compare_file)
            try:
                img1 = to_grayscale(imread("a.png").astype(float))
                img2 = to_grayscale(imread(instance_compare_file).astype(float))
                # compare
                n_m, n_0 = compare_images(img1, img2)
            except:
                logging.error("Exception in image compare: {0}".format(str(traceback.format_exc())))
                exit()
            # logging.debug("Manhattan norm: {0} / per pixel: {1}".format(n_m, n_m/img1.size))
            
            if abs(n_m/img1.size) < 30:
                logging.info("changing city to {0}".format(city))
                logging.info("open profile")
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/aside/div/a'))).click()
                logging.info("tinder+")
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/aside/nav/div/div/div/div/div/div/div[1]/a'))).click()
                logging.info("current location")
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[2]/section[1]/div[1]/div/div[2]/a'))).click()
                logging.info("search a location")
                time.sleep(2)
                # print(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.passport__locationMarker__info > div.Heading > h3.Heading__title'))).text)
                previous_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.passport__locationMarker__info > div.Heading > h3.Heading__title'))).text
                previous_result_text = previous_result
                # logging.info(previous_result.text)
                
                search_field = driver.find_element_by_xpath('//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[5]/div/div/span[2]/div/div[1]/input')
                search_field.clear()
                search_field.send_keys(city)
                logging.info("first result")
                time.sleep(2)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[5]/div/div/span[2]/div/div[2]/div[1]'))).click()
                # 
                # current_result = driver.find_element_by_xpath('//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[2]/div[2]/div/h3')
                # print(current_result.text())
                # exit()
                logging.info("result on map")
                time.sleep(2)
                if previous_result_text == driver.find_element_by_css_selector('div.passport__locationMarker__info > div.Heading > h3.Heading__title').text and previous_result_text != "Gurugram":
                    logging.info("prev city: {0}".format(previous_result_text))
                    logging.info("current city: {0}".format(driver.find_element_by_css_selector('div.passport__locationMarker__info > div.Heading > h3.Heading__title').text))
                    exit()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/span/div/div[1]/div/main/div[1]/div/div/div[2]/div[3]'))).click()
                logging.info("let it breathe")
                n_swipe_in_city_ctr = 0
                time.sleep(random.uniform(14.0058, 15.9058))
                

            # logging.info("checking if page is stuck")
            img3 = img.crop((470, 361, 894, 461))
            img3.save("{0}_is_page_alive.png".format(instance_compare_file.replace(".png","")))
            try:
                img1 = to_grayscale(imread("is_page_alive.png").astype(float))
                img2 = to_grayscale(imread("{0}_is_page_alive.png".format(instance_compare_file.replace(".png",""))).astype(float))
                # compare
                n_m, n_0 = compare_images(img1, img2)
            except:
                logging.error("Exception in image compare: {0}".format(str(traceback.format_exc())))
                # exit()
                break

            page_stuck_diff = abs(n_m/img1.size)
            if page_stuck_diff > 40:
                logging.info("page stuck, difference: {}, exiting!".format(page_stuck_diff))
                exit()
    # driver.set_window_size(1224, 768)
    # great_btn = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/span/div/div[2]/div/div/div[1]/div/div/div[4]/button[1]'))
    # )
    # great_btn.click()  
finally:
    driver.quit()
    # pass


logging.info("Completed")
logging.info("total time: " + str(int(time.time() - started_timestamp)) + " seconds")

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