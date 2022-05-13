from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


# driver = webdriver.Chrome(executable_path=r'C:\WebDriver\geckodriver.exe')

driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

driver.get('http://www.seleniumframework.com/Practiceform/')

driver.find_element(By.CSS_SELECTOR, '#alert')
alert_button = driver.find_element(By.CSS_SELECTOR, '#alert')
alert_button.click()

alert = driver.switch_to.alert
sleep(5)
alert.accept()