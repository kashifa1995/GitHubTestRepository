from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage


class LogInPage(BasePage):
    url = 'https://www.freecharge.in/'

    @property
    def log_in_button(self):
        locator = (By.XPATH, "//div/span[@class='login-btn']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def mobile_input(self):
        locator = (By.ID, "mobile")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def proceed_button(self):
        locator = (By.XPATH, "//div/button[.='proceed']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def mobile_recharge_button(self):
        locator = (By.XPATH, "//li/div[.='Mobile Recharge']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def input_mobile_no(self):
        locator = (By.NAME, "Enter Mobile Number")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def operator(self):
        locator = (By.NAME, "Operator")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def airtel_prepaid(self):
        locator = (By.XPATH, "//ul/li[.='Airtel Prepaid']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def circle(self):
        locator = (By.XPATH, "//div/input[@name='Circle']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def delhi_region(self):
        locator = (By.XPATH, "//ul/li[.='Delhi']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def next_button(self):
        locator = (By.XPATH, "//div/button[.='NEXT']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def inter_roaming(self):
        locator = (By.XPATH, "(//div[.='International Roaming'])[2]")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def pack8999(self):
        locator = (By.XPATH, "//div[contains(.,'8999')]/parent::div[contains(@class,'plans-features')]/following-sibling::button")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def submit_button(self):
        locator = (By.XPATH, "//div/button[.='submit']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def add_new_card_select(self):
        locator = (By.XPATH, "//label/img[@alt='Unchecked Option']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def enter_card_no(self):
        locator = (By.ID, "cardNumber")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def enter_month_year(self):
        locator = (By.ID, "expiryDate")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def enter_cvv(self):
        locator = (By.ID, "cvv")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def pay_now_button(self):
        locator = (By.XPATH, "//button[.='Pay Now']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def payment_interrupted(self):
        locator = (By.XPATH, "//div/p[.='Payment Interrupted']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])














