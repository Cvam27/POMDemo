import random
import time
import  string

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

url = "https://cloud.tenable.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()


class addFilterInTagRule():
    def login(self):
        driver.get(url)
        time.sleep(10)
        driver.find_element(By.XPATH, "//input[@name= 'username']").send_keys("data@lumin2.testing")
        driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("Tenable@123!")
        driver.find_element(By.XPATH, "//div[@role='checkbox']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()


    def navigationBar(self):
        driver.find_element(By.XPATH, "//button[@class='menu-styles__HamburgerButton-sc-auehwg-0 iqsqzI global-nav-hamburger']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[contains(text(),'Settings')]").click()

    def clickTagging(self):
        driver.find_element(By.XPATH, "//h2[normalize-space()='Tagging']").click()
        time.sleep(5)

    def createTagClick(self):
        driver.find_element(By.XPATH, "//span[normalize-space()='Create Tag']").click()
        time.sleep(5)

    def addTagDetails(self):
        driver.find_element(By.XPATH,"//div[@role='button']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='Add New Category']" ).send_keys("Auto_tag")
        driver.find_element(By.XPATH, "//div[@class='select-styles__Option-sc-19e9nzq-12 jQmzLs react-select-option React-select__option-new ']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='Create Value']").send_keys(f"{''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}")

    def ruleToggle(self):
        driver.find_element(By.XPATH,"//div[@data-e2e='rules-section-toggle']").click()
        time.sleep(5)


    def clickAddFilter(self):
        driver.find_element(By.XPATH, "//span[normalize-space()='Select Filters']").click()
        driver.find_element(By.XPATH, "//div[contains(text(),'IPv4 Address')]").click()
        driver.find_element(By.XPATH,"//fieldset[2]").click()
        driver.find_element(By.XPATH, "//div[@class='chip-styles__ChipText-sc-qskxe6-0 klSvJp']").click()
        driver.find_element(By.XPATH, "//textarea[@placeholder='192.168.1.2, 172.16.2.1-172.16.2.100, 10.100.5.0/24']").send_keys("1.1.1.1")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@type='button'][normalize-space()='Save']").click()

    def saveTag(self):
        driver.find_element(By.XPATH,"//button[@type='submit']").click()





ff = addFilterInTagRule()
ff.login()
ff.navigationBar()
ff.clickTagging()
ff.createTagClick()
ff.addTagDetails()
ff.ruleToggle()
ff.clickAddFilter()
ff.saveTag()
