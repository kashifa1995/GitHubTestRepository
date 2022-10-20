from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, by, value,):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator),
            message=f'Timeout while waiting for visibility {self.locator=}'
        )
        self.web_element = element
        return None

    def click(self):
        self.web_element.click()

    def send_keys(self, value):
        self.web_element.send_keys(value)

    def hover(self):
        ActionChains(self.driver).move_to_element(self.web_element).perform()

    def scroll(self):
        ActionChains(self.driver).w3c_actions(self.web_element).perform()









