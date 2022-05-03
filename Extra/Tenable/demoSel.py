import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:/Users/shivam_acharya/Downloads/chromedriver_win32/chromedriver.exe")
#s= Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s)
driver.implicitly_wait(10)

driver.get("https://phptravels.com/demo/")

un= driver.find_element(By.NAME, 'username')
pw= driver.find_element(By.NAME, 'password')
lg_btn = driver.find_element(By.CLASS_NAME, 'checkbox-styles__CheckboxElement-sc-1s7ocnd-0 imPkqO')


un.send_keys("admin@vm1.testing")
pw.send_keys("Tenable@1234")
time.sleep(2)
lg_btn.click()
time.sleep(2)