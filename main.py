from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)


driver.get("https://www.google.com/")
# e = driver.find_element_by_xpath("//div/a[.='Gmail']")
driver.find_element_by_css_selector('a[aria-label="Google apps"]').click()
iframe = driver.find_element_by_css_selector('iframe[name="app"]')

driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//li[.='Gmail']").click()
# A = ActionChains(driver)
# A.context_click(e).perform()
driver.quit()
