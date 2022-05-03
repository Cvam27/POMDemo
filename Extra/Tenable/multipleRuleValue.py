import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://cloud.tenable.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(50)
driver.maximize_window()
action = ActionChains(driver)


class addFilterInTagRule():
    def login(self):
        driver.get(url)
        driver.find_element(By.XPATH, "//input[@class = 'required login-username']").send_keys("")
        driver.find_element(By.XPATH, "//input[@class = 'required login-password']").send_keys("")
        driver.find_element(By.ID, "sign-in").click()

    def navigationBar(self):
        driver.find_element(By.XPATH, "//*[@id='main-app-container']/div[1]/button").click()
        driver.find_element(By.XPATH,
                            "//*[@id='main-app-navigation']/div[1]/div[1]/div[2]/div/div/div/div[6]/div/div").click()

    def clickTagging(self):
        driver.find_element(By.XPATH, "//*[@id='page-content-body-content']/div/div[2]/div/div[2]/div").click()
        time.sleep(5)

    def createTagClick(self):
        driver.find_element(By.XPATH, "//*[@id='template-header']/div/div[3]/div/button").click()
        time.sleep(10)

    def ruleToggle(self):
        driver.find_element_by_xpath(
            "//*[@id='template-content']/div/div[3]/div/div/form/fieldset[2]/legend/div/div[2]/div/div/div/div/div/div/div").click()
        time.sleep(5)

    def addFilterRule(self):
        dropdown = driver.find_element_by_xpath("//div[@data-e2e='tagging.filterRules.option.select']")
        action.move_to_element(dropdown).click().perform()

        ipv4 = driver.find_element_by_xpath("//div[contains(text(), 'IPv4 Address')]")
        action.move_to_element(ipv4).click().perform()


ff = addFilterInTagRule()
ff.login()
ff.navigationBar()
ff.clickTagging()
ff.createTagClick()
ff.ruleToggle()
ff.addFilterRule()
