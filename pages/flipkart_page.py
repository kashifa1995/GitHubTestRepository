from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.base_element import BaseElement
from selenium.webdriver.common.action_chains import ActionChains


class Flipkart(BasePage):

    url = 'https://www.flipkart.com/'

    @property
    def login_button(self):
        locator = (By.XPATH, "//div/a[.='Login']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def email_input(self):
        locator = (By.XPATH, "//div/label[.='Enter Email/Mobile number']/ancestor::div[@class='IiD88i _351hSN']/input[@type='text']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def email_label(self):
        locator = (By.XPATH, "//div/label[.='Enter Email/Mobile number']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def pwd_input(self):
        locator = (By.XPATH, "//div/label[.='Enter Password']/ancestor::div[contains(@class,'IiD88i _351hSN')]/input")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def log_in_modal_button(self):
        locator = (By.XPATH, "//button/span[.='Login']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def electronics(self):
        locator = (By.XPATH, "(//div[.='Electronics'])[4]")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def audio(self):
        locator = (By.XPATH, "//div/a[.='Audio']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def tablets(self):
        locator = (By.XPATH, "//div/a[.='Tablets']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def x_button(self):
        locator = (By.XPATH, "//button[.='✕']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def tablets_with_call_facility_button(self):
        locator = (By.XPATH, "//div/a[@title='Tablets with Call Facility']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def min_dropdown(self):
        locator = (By.XPATH, "//select/option[@value='Min']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def amount_15000_from_dropdown(self):
        locator = (By.XPATH, "//select/option[@value='15000']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def brand_option(self):
        locator = (By.XPATH, "(//div[.='Brand'])[1]")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def apple_brand(self):
        locator = (By.XPATH, "//div[@title='APPLE']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])



