from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from LoginPage import LoginPage

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get('https://127.0.0.1/login/')
driver.save_screenshot('print.png')

loginpage = LoginPage(driver)
loginpage.login()

driver.save_screenshot('print1.png')

driver.quit()
