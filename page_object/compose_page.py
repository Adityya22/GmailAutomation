from selenium.webdriver.common.by import By

from page_object.sent_page import SentPage


class ComposePage:

    def __init__(self, driver):
        self.driver = driver
    '''locators'''
    to_input = (By.CSS_SELECTOR, "div[class='wO nr l1'] textarea")
    subject_input = (By.CSS_SELECTOR, "input[class='aoT']")
    body_input = (By.CSS_SELECTOR, "div[class='Am Al editable LW-avf tS-tW']")
    send_btn = (By.CSS_SELECTOR, "div[class='T-I J-J5-Ji aoO v7 T-I-atl L3']")

    def get_to_input(self):
        return self.driver.find_element(*ComposePage.to_input)

    def get_subject_input(self):
        return self.driver.find_element(*ComposePage.subject_input)

    def get_body_input(self):
        return self.driver.find_element(*ComposePage.body_input)

    def get_send_btn(self):
        # click sent button
        self.driver.find_element(*ComposePage.send_btn).click()

    # create a sent_page object
    def sent_page_obj(self):
        sent_page = SentPage(self.driver)
        return sent_page



