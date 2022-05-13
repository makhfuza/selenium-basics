from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Firefox()

driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('problem_user')
driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
# driver.fine_element(By.CLASS_NAME, 'submit-button').click()

login_button = driver.find_element(By.CLASS_NAME, 'submit-button')
login_button.click()

