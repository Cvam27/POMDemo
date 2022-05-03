
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)

driver.implicitly_wait(20)
driver.get("https://us-2b.svc.nessus.org/")
driver.maximize_window()

un = driver.find_element(By.XPATH, "//input[@name='username']")
pw = driver.find_element(By.XPATH, "//input[@name='password']")
login_btn = driver.find_element(By.XPATH, "//button[@type= 'submit']")

un_input = input("Enter username")
pw_input = input("Enter password")


def test_login(username, password):
    un_data = 'admin@sca-api-1.testing'
    pw_data = 'Tenable@123!'

    if un_input == un_data and pw_input == pw_data:
        un.send_keys(un_input)
        pw.send_keys(pw_input)
        login_btn.click()
        print("Login success")
        time.sleep(20)
    else:
        print("Invalid Username and/or password")
        driver.close()


test_login(un_input, pw_input)
