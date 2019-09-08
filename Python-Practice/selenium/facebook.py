import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get('http://www.facebook.com')
elem = driver.find_element(By.XPATH,'//*[@id="email"]')
elem.send_keys('9849757131')
elem = driver.find_element(By.XPATH,'//*[@id="pass"]')
elem.send_keys('9876suru12345')
elem = driver.find_element(By.XPATH,'//*[@id="loginbutton"]')
elem.click()

status = driver.find_element(By.XPATH,'//*[@name="xhpc_message"]')
status.send_keys('Sakriya')
print("after name")
#post = driver.find_element_by_css_selector('button[data-testid="react-composer-post-button"]')
#post.click()
time.sleep(5)
buttons = driver.find_elements_by_tag_name("button")
for button in buttons:
    if button.text == "Post":
        print("INSIDE post")
        webdriver.ActionChains(driver).move_to_element(button ).click(button ).perform()
print("finished")
