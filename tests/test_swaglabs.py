from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pytest
from time import sleep
from get_excel import login_form_parameters




######################### COMMON FUNCTIONS ######################################################
def launch_swaglabs():
    global driver
    driver = webdriver.Firefox(executable_path=r'C:\WebDriver\geckodriver.exe')
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

def login_valid_credentials():
     driver.find_element(By.ID, 'user-name').send_keys('problem_user')
     driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
     driver.find_element(By.CLASS_NAME, 'submit-button').click()

def capture_evidence():
     image_name = fr"C:\selenium-basics\tests\evidence\image-{datetime.today().strftime('%m%d%y-%H%M%S')}.png"
     driver.save_screenshot(image_name)

def text_is_displayed(text):
     return text.lower() in driver.page_source.lower()

##########################  TEST CASES  ##########################################################

def test_launch_login_page():
    launch_swaglabs()
    assert driver.title == 'Swag Labs'
    capture_evidence()
    driver.quit()

# login_form_parameters = [
#      ('locked_out_user', 'secret_sauce',        'Sorry, this user has been locked out'),
#      ('test',            'test',                'Username and password do not match any user in this service'),
#      ('standard_user',   '',                    'Password is required'),
#      ('test',            'secret_sauce',        'Username and password do not match any user in this service'),
#      ('',                'secret_sauce',        'Username is required'),
#      ('standard_user',   'test',                'Username and password do not match any user in this service')
#      ]

@pytest.mark.parametrize("username, password, checkpoint", login_form_parameters)
     
def test_login_invalid_credentials(username, password, checkpoint):
     launch_swaglabs()
     driver.find_element(By.ID, 'user-name').send_keys(username)
     driver.find_element(By.NAME, 'password').send_keys(password)
     driver.find_element(By.CLASS_NAME, 'submit-button').click()
     assert checkpoint.lower() in driver.page_source.lower()
     capture_evidence()
     driver.quit()


####################### BELOW TEST CASES HAVE SETUP AND TEARDOWN #####################

@pytest.fixture()
def setup(request):
     # the following code runs before each test
     launch_swaglabs()
     login_valid_credentials()

     # the following code runs after each test
     def teardown():
          capture_evidence()
          driver.quit()
     request.addfinalizer(teardown)

def test_login_valid_credentials(setup):
     assert text_is_displayed('products') 
    

def test_view_product_details(setup):
     product_names = driver.find_elements(By. CLASS_NAME, 'inventory_item_name')
     product_names[0].click()
     assert text_is_displayed('back to products')
     
def test_add_item_to_cart(setup):
     driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt").click()
     driver.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
     assert text_is_displayed('your cart')
     

def test_checkout_item(setup):
    driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR,'.shopping_cart_link').click()
    driver.find_element(By.ID,"checkout").click()
    assert text_is_displayed('first name') 

