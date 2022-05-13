from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

driver.get('http://automationpractice.com/index.php')

# driver.find_element(By.XPATH, "//[text()='Contact us']")
# element = driver.find_element(By.XPATH, "//[text()='Contact us']")
# element.click()
# sleep(15)

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Contact Us']"))
    )
except TimeoutException:
    print('Waited for 15 sec, could not locate the element')
else:
    element.click()
    print('Clicked on the element')

print('next step')
    
