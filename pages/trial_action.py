import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.flipkart_page import Flipkart
from pages.login_page import LogInPage
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
flipkart_page = Flipkart(driver=driver)
flipkart_page.go()
