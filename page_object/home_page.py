from selenium.webdriver.common.by import By

from page_object.compose_page import ComposePage
from page_object.mail_page import MailPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    profile_btn = (By.CSS_SELECTOR, "header .gb_la img")
    name = (By.XPATH, "//div[@class='znj3je NB6Lnc']")
    id = (By.XPATH, "//div[@class='Wdz6e ZnExKf']")
    compose_btn = (By.CSS_SELECTOR, "div[class='T-I T-I-KE L3']")
    all_mail_titles = (By.CSS_SELECTOR, "tbody tr td:nth-child(4)")
    popup = (By.XPATH, "//button[@class='bja J-I']")

    def is_popup_present(self) -> bool:
        """
        This function for checking popup present or not
        :return: True if popup is present
        """
        popup = self.driver.find_elements(*HomePage.popup)
        present = False
        if len(popup) >= 1:
            print("PopUp is present")
            present = True
        return present

    def close_popup(self):
        """
        This function is for Closing PopUp
        :return: None
        """
        self.driver.find_element(By.XPATH, "//button[@class='bja J-I']").click()

    def get_profile_btn(self):
        return self.driver.find_element(*HomePage.profile_btn)

    def get_profile_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_profile_id(self):
        return self.driver.find_element(*HomePage.id)

    def get_compose_btn(self):
        """
        click the compose button
        :return: None
        """
        self.driver.find_element(*HomePage.compose_btn).click()

    def compose_page_obj(self):
        compose_page = ComposePage(self.driver)
        return compose_page

    def get_all_mail_titles(self):
        all_mails = self.driver.find_elements(*HomePage.all_mail_titles)
        all_mails[0].click()
        mail_page = MailPage(self.driver)
        return mail_page
