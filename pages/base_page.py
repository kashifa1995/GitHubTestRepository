from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def go(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def scroll_to_bottom(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')



