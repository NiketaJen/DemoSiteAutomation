from ssqatest.src.pages.locators import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ssqatest.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedOut(MyAccountSignedOutLocator):
    # pass the driver object into function
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # create functions for all actions that need to be done on the page
    def go_to_my_account(self):
        pass

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
      self.sl.wait_and_click(self.LOGIN_BTN)
