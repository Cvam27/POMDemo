import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(20)
driver.get("https://cloud.tenable.com")
loginTitle = driver.title
userName = driver.find_element(By.XPATH, "//input[@name='Username']")
password = driver.find_element(By.XPATH, "//input[@name='Password']")
loginButton = driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']")
remember_checkbox = driver.find_element(By.XPATH, "//div[@id='formItem9']")

userName.send_keys('Test Username')
password.send_keys("This is password")
remember_checkbox.click()
exp_wait = WebDriverWait.until(remember_checkbox.click())
loginButton.click()

time.sleep(50)
# driver.quit()
