import requests
import selenium
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

def img_url_grabber():
    IMG_XPATH = '//*[@id="top"]/div[1]/div[1]/img'
    BTN_XPATH = '//*[@id="top"]/div[1]/div[2]/div/div[2]'
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('--disable-extensions')    
    chrome_options.headless = True
            
    driver = webdriver.Chrome(options = chrome_options, executable_path = os.environ.get("CHROMEDRIVER_PATH"))
    driver.get('https://www.inspirobot.me')

    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, BTN_XPATH))).click()

    image_src = WebDriverWait(driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, IMG_XPATH))).get_attribute('src')
     
    driver.quit()
    
    return (image_src)
