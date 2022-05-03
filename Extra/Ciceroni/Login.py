from selenium import webdriver

driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.implicitly_wait(0)
driver.get("https://www.ciceroni.in/")
driver.find_element_by_xpath("//button[@class='btn btnHover name d-none loginShow']").click()
