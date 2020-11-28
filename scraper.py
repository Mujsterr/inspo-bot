import requests
import selenium
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def img_url_grabber():
    chrome_options = Options()
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')    
    chrome_options.headless = True
            
    driver = webdriver.Chrome(options = chrome_options, executable_path = os.environ.get("CHROMEDRIVER_PATH"))
    driver.get('https://www.inspirobot.me')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/div'))).click()
    image_src = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="top"]/div[1]/div[1]/img'))).get_attribute('src')
     
    driver.quit()
    
    return (image_src)
