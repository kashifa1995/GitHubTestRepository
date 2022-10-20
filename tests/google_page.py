from tests.base_page import BasePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executablepath=ChromeDriverManager().install())

driver.find_element_by_xpath()



