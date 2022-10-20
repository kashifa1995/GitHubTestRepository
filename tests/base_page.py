class BasePage:
     def __init__(self,driver):
         self.driver = driver
         self.url = None

     def go(self):
         self.driver.get("self.url")

