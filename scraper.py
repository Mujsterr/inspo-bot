import requests
import selenium
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions


def img_url_grabber(): 
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
   # chrome_options.add_argument("--proxy-server='direct://'")
   # chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.headless = True
            
    driver = webdriver.Chrome(options = chrome_options, executable_path = os.environ.get("CHROMEDRIVER_PATH"))
    driver.get('https://www.inspirobot.me')

    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/div[2]').click()

    #image_src = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/img")))
    time.sleep(2)
    image_src = driver.find_element_by_xpath( "/html/body/div[2]/div[1]/div[1]/div[1]/img").get_attribute('src')
    
    #image_src.get_attribute('src')
    driver.quit()
    
    return (image_src)



