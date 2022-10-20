from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LogInPage
import tempfile

temp_dir = tempfile.mkdtemp()
options = Options()
options.add_argument('--headless')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
# options.add_argument(f'--user-data-dir={temp_dir}')
path = ChromeDriverManager().install()

driver = webdriver.Chrome(executable_path=path, options=options)
login_page = LogInPage(driver=driver)
import time


login_page.go()
# login_page.log_in_button.click()
# login_page.mobile_input.send_keys("6395977372")
# time.sleep(10)
# login_page.submit_button.click()
login_page.mobile_recharge_button.click()
login_page.input_mobile_no.send_keys("6395977372")
login_page.operator.click()
login_page.airtel_prepaid.click()
login_page.circle.click()
login_page.delhi_region.click()
login_page.next_button.click()
login_page.inter_roaming.click()
login_page.pack8999.hover()
login_page.pack8999.click()
# login_page.add_new_card_select.click()
# login_page.enter_card_no.click().send_keys("4242424242424242")




