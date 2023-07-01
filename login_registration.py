# Регистрация аккаунта
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://practice.automationtesting.in/")
account = driver.find_element_by_link_text('My Account')
account.click()
reg_email = driver.find_element_by_id('reg_email')
reg_email.send_keys('jackie@jackie.com')
reg_password = driver.find_element_by_id('reg_password')
reg_password.send_keys('triptrip123!@#')
register = driver.find_element_by_name('register')
register.click()

# Логин в систему
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://practice.automationtesting.in/")
account = driver.find_element_by_link_text('My Account')
account.click()
username = driver.find_element_by_id('username')
username.send_keys('jackie@jackie.com')
password = driver.find_element_by_id('password')
password.send_keys('triptrip123!@#')
login = driver.find_element_by_name('login')
login.click()
logout = driver.find_element_by_link_text('Logout')
logout_text = logout.text
print(logout_text)
if logout_text == 'Logout':
    print('Ok')
else:
    print('Not')
