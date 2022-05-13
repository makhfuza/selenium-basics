from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Firefox()

driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')

driver.get('https://www.saucedemo.com/')

# driver.find_element(By.ID, 'user-name').send_keys('problem_user')
# driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
# # driver.fine_element(By.CLASS_NAME, 'submit-button').click()

# login_button = driver.find_element(By.CLASS_NAME, 'submit-button')
# login_button.click()

# def test_add_item_to_cart():
#     # product_names=driver.find_element(By. CLASS_NAME,'Inventory_item_name')
#     # product_names[0].click()
#     product_names=driver.find_element(By. ID,'add-to-cart-sauce-backpack').click()

# test_add_item_to_cart()

# element = driver.find_element(By. CLASS_NAME,'shopping_cart_badge')
# print(element.text =='1')

# checkout=driver.find_element(By.CSS_SELECTOR,'#checkout').click()

# driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('Natalia')
# driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys('Test')
# driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('45039')

# driver.find_element(By.CSS_SELE
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver=webdriver.Firefox()

# driver.get('https://www.saucedemo.com/')

# username=driver.find_element(By.ID,'user-name')

# password=driver.find_element(By.NAME,'password')

# login_button=driver.find_element(By.CLASS_NAME,'submit-button')

# username.send_keys('performance_glitch_user')

# password.send_keys('secret_sauce')

# login_button.click()

# driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
# element=driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge")
# print(element.text=='1')
# driver.find_element(By.CSS_SELECTOR,'.shopping_cart_link').click()

# price_element=driver.find_element(By.CSS_SELECTOR,'.inventory_item_price')
# print(price_element.text)

# checkout=driver.find_element(By.
# From Ana Ciobanu to Everyone 08:08 PM
# driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('45039')
# From Ana Ciobanu to Everyone 08:18 PM
# driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys('Test')
# driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('45039')
# driver.find_element(By.CSS_SELECTOR,'#continue').click()
# From Nuriya Suliev to Everyone 08:18 PM
# driver.find_element(By.CSS_SELECTOR,'#continue').click()


from selenium import webdriver
from selenium.webdriver.common.by import By



driver.get('https://www.saucedemo.com/')

username=driver.find_element(By.ID,'user-name')

password=driver.find_element(By.NAME,'password')

login_button=driver.find_element(By.CLASS_NAME,'submit-button')

username.send_keys('performance_glitch_user')

password.send_keys('secret_sauce')

login_button.click()

driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack").click()
element=driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge")
print(element.text=='1')
driver.find_element(By.CSS_SELECTOR,'.shopping_cart_link').click()

price_element=driver.find_element(By.CSS_SELECTOR,'.inventory_item_price')
print(price_element.text)

checkout=driver.find_element(By.CSS_SELECTOR,'#checkout').click()

driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys('Natalia')
driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys('Test')
driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys('45039')
driver.find_element(By.CSS_SELECTOR,'#continue').click()
driver.find_element(By.CSS_SELECTOR,'#finish').click()
driver.find_element(By.CSS_SELECTOR,'.complete-header').click()

element=driver.find_element(By.CSS_SELECTOR,'.complete-header')
# print(element.text=='THANK YOU FOR YOUR ORDER')
# driver.close()