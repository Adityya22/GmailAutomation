from selenium.webdriver.common.by import By


class SentPage:
    def __init__(self, driver):
        self.driver = driver

    # sent_btn = (By.XPATH, "//*[@id=':kr']/div/div[2]/span/a")
    sent_btn = (By.XPATH, "(//div[@class='aio UKr6le'])[4]")
    sent_mails = (By.CSS_SELECTOR, "tbody tr")
    # inbox_btn = (By.XPATH, "//*[@id=':kn']/div/div[2]")
    inbox_btn = (By.XPATH, "(//div[@class='aio UKr6le'])[1]")
    sent_mail_title = (By.CSS_SELECTOR, "tbody tr td:nth-child(5) span:nth-child(1) span")

    def get_sent_btn(self):
        return self.driver.find_element(*SentPage.sent_btn)

    def get_sent_mails(self):
        return self.driver.find_elements(*SentPage.sent_mails)

    def get_inbox_btn(self):
        return self.driver.find_element(*SentPage.inbox_btn)

    def get_sent_mail_title(self):
        return self.driver.find_element(*SentPage.sent_mail_title)
