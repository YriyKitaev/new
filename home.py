# Добавление комментария
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
book = driver.find_element_by_class_name('woocommerce-LoopProduct-link')
book.click()
reviews = driver.find_element_by_class_name('reviews_tab')
reviews.click()
stars = driver.find_element_by_class_name('star-5')
stars.click()
comment = driver.find_element_by_id('comment')
comment.send_keys('Nice book!')
author = driver.find_element_by_id('author')
author.send_keys('Jackie')
email = driver.find_element_by_id('email')
email.send_keys('jackie@jackie.com')
submit = driver.find_element_by_id('submit')
submit.click()