import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://www.google.com')
elem = driver.find_element(By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
#elem = driver.find_element_by_tag_name('html')
#elem.send_keys(Keys.END)
#time.sleep(1)
#elem.send_keys(Keys.HOME)
#elem = driver.find_element_by_link_text()
time.sleep(1)
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)
time.sleep(1)
driver.refresh()
driver.back()
time.sleep(1)
driver.forward()
print(driver.current_url)
