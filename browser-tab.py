from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


# driver = webdriver.Chrome(executable_path=r'C:\WebDriver\geckodriver.exe')

driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

driver.get('http://www.seleniumframework.com/Practiceform/')

driver.find_element(By.XPATH, "//*[text()='New Browser Tab']").click()

new_tab_button = driver.find_element(By.XPATH, "//*[text()='New Browser Tab']")
new_tab_button.click()
sleep(10)

print(len(driver.window_handles))

first_tab = driver.window_handles[0]
second_tab = driver.window_handles[1]
driver.switch_to.window(second_tab)
driver.close()
sleep(5)
driver.switch_to.window(first_tab)
driver.close()


# driver.find_element(By.XPATH, "//a[text()='Contact us']").click()

# select = Select(driver.find_element(By.TAG_NAME, 'select'))
# select.select_by_visible_text('Customer service')

# driver.find_element(By.CSS_SELECTOR, '#email').send_keys('team@skillrill.com')

# driver.find_element(By.CSS_SELECTOR, '#id_order').send_keys(1)

# driver.find_element(By.XPATH, "//*[@id='fileUpload']").send_keys(r'C:\selenium-basics\test.txt')

# choose_file = driver.find_element(By.XPATH, "//*[@id='fileUpload']")
# file_path = r'C:\selenium-basics\test.txt'
# choose_file.send_keys(file_path)

# driver.find_element(By.CSS_SELECTOR, '#message').send_keys('test')
# driver.find_element(By.XPATH, "//*[@id='submitMessage']").click()

# if driver.find_element_by_xpath("//*[text()='Your message has been successfully sent to our team'] "):
#     print(True)
    

