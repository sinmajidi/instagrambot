from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import seed
from random import randint
import time
def getRandomTime():
        randTime = randint(3, 5)
        return randTime

username = "***"
password = "****"
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com/")
print(driver.title)
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log In')]").click()
time.sleep(getRandomTime())
driver.find_element_by_xpath("//a[contains(@href,'/')]").click()
driver.find_element_by_xpath("//button[contains(.,'Not Now')]").click()
# driver.close()
