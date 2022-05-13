from selenium import webdriver
from selenium.webdriver.common.by import By


# driver=webdriver.Firefox()
# driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

driver = webdriver.Chrome(executable_path=r'C:\WebDriver\geckodriver.exe')

driver.get('http://automationpractice.com/index.php')

# driver.find_element(By.LINK_TEXT,'Sign in').click()

# key_word = 'RetreivE'

# driver.find_element(By.LINK_TEXT,'Forgot your password?').click()
# print(key_word.lower() in driver.page_source.lower())

# driver.find_element(By.LINK_TEXT,'DRESSES').click()

# print('There are 5 products' in driver.page_source)

# add_buttons = driver.find_elements(By.XPATH,"//span[text()='Add to cart']")

# add_buttons = driver.find_elements(By. CLASS_NAME,"product-container")


# print(f'There are {len(add_buttons)} products displayed')

# add_buttons[0].click()

# driver.find_element(By.NAME,"SUBMIT").click()

# print('There is 1 item in your cart' in driver.page_source)


