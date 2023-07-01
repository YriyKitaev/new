# Отображение страницы товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# account = driver.find_element_by_link_text('My Account')
# account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('jackie@jackie.com')
# password = driver.find_element_by_id('password')
# password.send_keys('triptrip123!@#')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# book = driver.find_element_by_tag_name('[alt="Mastering HTML5 Forms"]')
# book.click()
# book_title = driver.find_element_by_tag_name('[itemprop="name"]').text
# print(book_title)
# if book_title == "HTML5 Forms":
#     print('OK')
# else:
#     print('Not')

# Количество товаров в категории
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# account = driver.find_element_by_link_text('My Account')
# account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('jackie@jackie.com')
# password = driver.find_element_by_id('password')
# password.send_keys('triptrip123!@#')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# html_title = driver.find_element_by_link_text('HTML')
# html_title.click()
# product_shop = driver.find_elements_by_css_selector('#content > ul > li')
# if len(product_shop) == 3:
#     print('В корзине 3 товара')
# else:
#     print('Количество товаров в корзине: ' + str(len(product_shop)))

# Сортировка товаров
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# account = driver.find_element_by_link_text('My Account')
# account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('jackie@jackie.com')
# password = driver.find_element_by_id('password')
# password.send_keys('triptrip123!@#')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# selector = driver.find_element_by_tag_name('[value="menu_order"]')
# selector_text = selector.text
# print(selector_text)
# if selector_text == 'Default sorting':
#     print('Ok')
# else:
#     print('Not')
# selector = driver.find_element_by_tag_name('[value="menu_order"]')
# selector.click()
# orderby = driver.find_element_by_tag_name('[value="price-desc"]')
# orderby.click()
# orderby = driver.find_element_by_tag_name('[value="price-desc"]')
# orderby_text = orderby.text
# print(orderby_text)
# if orderby_text == 'Sort by price: high to low':
#     print('Ok')
# else:
#     print('Not')

# Отображение, скидка товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# account = driver.find_element_by_link_text('My Account')
# account.click()
# username = driver.find_element_by_id('username')
# username.send_keys('jackie@jackie.com')
# password = driver.find_element_by_id('password')
# password.send_keys('triptrip123!@#')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# android = driver.find_element_by_class_name('woocommerce-LoopProduct-link')
# android.click()
# old_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span')
# old_price_text = old_price.text
# print(old_price_text)
# assert old_price_text == '₹600.00'
# new_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span')
# new_price_text = new_price.text
# print(new_price_text)
# assert new_price_text == '₹450.00'
# android_img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169 > div.images > a > img")))
# android_img.click()
# close_img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_img.click()

# Проверка цены в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# driver.execute_script("window.scrollBy(0, 400);")
# to_basket = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# to_basket.click()
# time.sleep(1)
# cartcontents = driver.find_element_by_class_name('cartcontents')
# cartcontents_text = cartcontents.text
# print(cartcontents_text)
# assert cartcontents_text == '1 Item'
# time.sleep(1)
# amount = driver.find_element_by_class_name('amount')
# amount_text = amount.text
# print(amount_text)
# assert amount_text == '₹180.00'
# wpmenucart_contents = driver.find_element_by_class_name('wpmenucart-contents')
# wpmenucart_contents.click()
# subtotal = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td"), "₹180.00"))
# print(subtotal)
# assert subtotal == True
# total = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td"), "₹183.60"))
# print(total)
# assert total == True

# Работа в корзине
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_html = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# book_html.click()
# time.sleep(1)
# book_js = driver.find_element_by_css_selector('#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# book_js.click()
# cartcontents = driver.find_element_by_class_name('cartcontents')
# cartcontents.click()
# time.sleep(1)
# del_book = driver.find_element_by_tag_name('[data-product_id="182"]')
# del_book.click()
# undo = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div.woocommerce-message > a')
# undo.click()
# quantity = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
# quantity.clear()
# quantity.send_keys(3)
# update_cart = driver.find_element_by_name('update_cart')
# update_cart.click()
# quantity = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
# quantity_value = quantity.get_attribute('value')
# print(quantity_value)
# assert quantity_value == '3'
# time.sleep(2)
# apply_coupon = driver.find_element_by_name('apply_coupon')
# apply_coupon.click()
# coupon_code = driver.find_element_by_class_name('woocommerce-error')
# assert coupon_code.text == 'Please enter a coupon code.'

# Покупка товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_html = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
# book_html.click()
# time.sleep(1)
# cartcontents = driver.find_element_by_class_name('cartcontents')
# cartcontents.click()
# checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > div > a")))
# checkout.click()
# billing_first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
# billing_first_name.send_keys("Kyrie")
# billing_last_name = driver.find_element_by_id('billing_last_name')
# billing_last_name.send_keys('Irving')
# billing_email = driver.find_element_by_id('billing_email')
# billing_email.send_keys('Kyrie@Irving.com')
# billing_phone = driver.find_element_by_id('billing_phone')
# billing_phone.send_keys('456456456456')
# s2id_billing_country = driver.find_element_by_id('s2id_billing_country')
# s2id_billing_country.click()
# s2id_autogen1_search = driver.find_element_by_id('s2id_autogen1_search')
# s2id_autogen1_search.send_keys('Australia')
# country = driver.find_element_by_class_name('select2-match')
# country.click()
# billing_address_1 = driver.find_element_by_id('billing_address_1')
# billing_address_1.send_keys('street')
# billing_city = driver.find_element_by_id('billing_city')
# billing_city.send_keys('Suburb')
# select2_chosen_2 = driver.find_element_by_id('s2id_billing_state')
# select2_chosen_2.click()
# queensland = driver.find_element_by_id('s2id_autogen2_search')
# queensland.send_keys('Queensland')
# state = driver.find_element_by_class_name('select2-match')
# state.click()
# billing_postcode = driver.find_element_by_id('billing_postcode')
# billing_postcode.send_keys('123123123')
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# check = driver.find_element_by_tag_name('[value="cheque"]')
# check.click()
# place_order = driver.find_element_by_id('place_order')
# place_order.click()
# message = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# assert message == True
# payment = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
# assert payment == True