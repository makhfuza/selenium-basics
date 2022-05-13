from selenium import webdriver
from selenium.webdriver.common.by import By


# driver=webdriver.Firefox()

driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

# driver.get('http://automationpractice.com/index.php')

driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('problem_user')
driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
driver.find_element(By.CLASS_NAME, 'submit-button').click()

# product_names = driver.find_elements(By. CLASS_NAME, 'inventory_item_name')
# product_names[0].click()

driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
# element=driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge")
# print(element.text=='1')
driver.find_element(By.CSS_SELECTOR,'.shopping_cart_link').click()

driver.find_element(By.CSS_SELECTOR,'.inventory_item_price')
driver.find_element(By.ID,"checkout").click()

# price_element=driver.find_element(By.CSS_SELECTOR,'.inventory_item_price')
# print(price_element.text)

# checkout=driver.find_element(By.CSS_SELECTOR,'#checkout').click()

# driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt").click()
# driver.find_element(By.CSS_SELECTOR,".shopping_cart_link")
# element=driver.find_element(By. CLASS_NAME, "shopping_cart_link")

# driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-fleece-jacket").click()
# driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()