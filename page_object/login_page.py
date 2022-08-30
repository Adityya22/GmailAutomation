from selenium.webdriver.common.by import By
from utilties.basepage import BaseClass
from page_object.home_page import HomePage


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    mailid_inpt = (By.XPATH, "//*[@id='identifierId']")
    id_nxt_btn = (By.XPATH, "//div[@id='identifierNext']")
    # pass_inpt = (By.XPATH, "//input[@type='password']")
    pass_inpt = (By.XPATH, "//input[@aria-label='Enter your password']")
    pass_nxt_btn = (By.XPATH, "//div[@id='passwordNext']")

    def is_email_id_present(self) -> bool:
        """
        This function for checking email-id present or not
        :return: True if email-id is present
        """
        self.element_wait_presence(LoginPage.mailid_inpt)
        email = self.driver.find_elements(*LoginPage.mailid_inpt)
        present = False
        if len(email) >= 1:
            print("email-id text box is present")
            present = True
        return present

    def get_mailid_inpt(self):
        return self.driver.find_element(*LoginPage.mailid_inpt)

    def is_password_input_present(self) -> bool:
        """
        This function for checking password input box present or not
        :return: True if password input box is present
        """
        self.element_wait_presence(LoginPage.pass_inpt)   ##  doubt  hai *LoginPage.pass_inpt ==>> problem de rha hai
        passwrd = self.driver.find_elements(*LoginPage.pass_inpt)
        present = False
        if len(passwrd) >= 1:
            print("password input box is present")
            present = True
        return present

    def get_id_nxt_btn(self):
        return self.driver.find_element(*LoginPage.id_nxt_btn)

    def get_pass_inpt(self):
        return self.driver.find_element(*LoginPage.pass_inpt)

    def get_pass_nxt_btn(self):
        self.driver.find_element(*LoginPage.pass_nxt_btn).click()
        return HomePage(self.driver)
