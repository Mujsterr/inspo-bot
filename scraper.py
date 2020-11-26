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
    DRIVER_PATH = 'D:/chromedriver/chromedriver.exe' 
    IMG_XPATH = './html/body/div[2]/div[1]/div[1]/div[1]/img'
    BTN_XPATH = '/html/body/div[2]/div[1]/div[1]/div[2]/div/div[2]'
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")    
    chrome_options.headless = True
            
    driver = webdriver.Chrome(options = chrome_options, executable_path = DRIVER_PATH )#os.environ.get("CHROMEDRIVER_PATH"))
    driver.get('https://www.inspirobot.me')

    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, BTN_XPATH)))
    driver.find_element_by_xpath(BTN_XPATH).click()
    
    WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, IMG_XPATH)))                                  
    image_src = driver.find_element_by_xpath(IMG_XPATH).get_attribute('src')
    
    driver.quit()
    
    return (image_src)


print(img_url_grabber())
