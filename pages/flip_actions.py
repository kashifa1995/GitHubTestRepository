import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.flipkart_page import Flipkart
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

flipkart_page = Flipkart(driver=driver)

flipkart_page.go()
# flipkart_page.login_button.click()
# flipkart_page.email_input.send_keys("kashifamansoor1995@gmail.com")
# flipkart_page.pwd_input.send_keys("kashifaa")
# flipkart_page.log_in_modal_button.click()
flipkart_page.x_button.click()
flipkart_page.electronics.hover()
flipkart_page.audio.hover()
flipkart_page.tablets.hover()
flipkart_page.tablets.click()
flipkart_page.tablets_with_call_facility_button.click()
time.sleep(2)
flipkart_page.min_dropdown.click()
flipkart_page.amount_15000_from_dropdown.click()
time.sleep(2)
flipkart_page.brand_option.click()
flipkart_page.apple_brand.click()
