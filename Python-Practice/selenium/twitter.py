import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

id = driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
id.send_keys('9849757131')
passw = driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
passw.send_keys('')
login = driver.find_element(By.XPATH,'//*[@id="page-container"]/div/div[1]/form/div[2]/button')
login.click()
el = driver.find_element_by_id('tweet-box-home-timeline')
el.send_keys("KEYS")


