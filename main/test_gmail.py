import time

from config.configuration import TestConfig
from page_object.compose_page import ComposePage
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.mail_page import MailPage
from page_object.sent_page import SentPage
from utilties.basepage import BaseClass


class TestMain(BaseClass):

    def test_gmail(self, params):
        # Code from Implicit wait of 5 second
        self.driver.implicitly_wait(10)

        login_page = LoginPage(self.driver)

        # Enter the MailId
        check_email_input_box_present = login_page.is_email_id_present()
        if check_email_input_box_present:
            login_page.get_mailid_inpt().send_keys(params['email'])

        # click on next button
        self.element_wait_clickable(login_page.get_id_nxt_btn())
        login_page.get_id_nxt_btn().click()

        # Entering the password
        check_password_input_box_present = login_page.is_password_input_present()
        if check_password_input_box_present:
            login_page.get_pass_inpt().send_keys(params['password'])

        # click on next button
        self.element_wait_clickable(login_page.pass_nxt_btn)
        homepage = login_page.get_pass_nxt_btn()
        # time.sleep(2)
        # self.driver.switch_to.alert().dismiss()
        pop_up = homepage.is_popup_present()
        if pop_up:
            print("Going to close popup")
            homepage.close_popup()

        # click on profile button
        self.element_wait_presence(HomePage.profile_btn)
        homepage.get_profile_btn().click()

        # Switching to frame to get the log in ID
        self.driver.switch_to.frame('account')

        # get the name from the gmail profile and validate
        self.element_wait_presence(HomePage.name)

        assert homepage.get_profile_name().text == TestConfig.profile_name, "Profile name is incorrect"
        self.message_logging('Profile Name is validated')

        # get email-id from the gmail profile and validate
        self.element_wait_presence(HomePage.id)

        assert homepage.get_profile_id().text == TestConfig.profile_email_id, "Profile email is incorrect"
        self.message_logging('Profile Email-id is validated')

        self.driver.switch_to.default_content()

        # clicking on Compose button
        self.element_wait_clickable(HomePage.compose_btn)
        homepage.get_compose_btn()

        # create compose page object
        compose_page = homepage.compose_page_obj()

        # Send a mail and add email-id in the input field
        self.element_wait_presence(ComposePage.to_input)
        compose_page.get_to_input().send_keys(TestConfig.profile_email_id)

        # Add subject to the mail
        self.element_wait_presence(ComposePage.subject_input)
        compose_page.get_subject_input().send_keys('Gmail Automation using pytest')
        #

        # sending input to body field
        self.element_wait_presence(ComposePage.body_input)
        for i in range(0, 50):
            compose_page.get_body_input().send_keys('Hello World ')
        self.message_logging('hello world is printed 50 times')

        # Clicking on send Button
        self.element_wait_clickable(ComposePage.send_btn)
        compose_page.get_send_btn()

        # create sent page object
        sent_page = compose_page.sent_page_obj()

        # Waiting to send the message
        time.sleep(5)

        # Clicking on sent Option
        self.element_wait_clickable(SentPage.sent_btn)
        sent_page.get_sent_btn().click()

        # Getting all the mails of sent page
        self.element_wait_presence(SentPage.sent_mails)
        sent_mails = sent_page.get_sent_mails()
        time.sleep(2)  # Mandatory
        self.element_wait_presence(SentPage.sent_mails)
        time.sleep(5)
        # Clicking on the sendmail
        sent_mails[0].click()

        self.driver.get_screenshot_as_file('SentMailScreenshot.png')
        time.sleep(2)  # waiting to take screenshot

        # Clicking on the inbox option
        self.element_wait_clickable(SentPage.inbox_btn)
        sent_page.get_inbox_btn().click()
        #
        # Getting all the inbox messages
        self.element_wait_presence(HomePage.all_mail_titles)
        mailpage = homepage.get_all_mail_titles()

        # getting the title of received mail
        self.element_wait_presence(MailPage.rec_mail_title)
        rec_mail_title = mailpage.get_rec_mail_title().text
        self.message_logging(rec_mail_title)
        print(rec_mail_title)

        # Check whether send mail and received mail is same or not
        assert rec_mail_title == 'Gmail Automation using pytest'

        # Clicking on More Option
        self.element_wait_clickable(MailPage.more_option_btn)
        mailpage.get_more_option_btn().click()

        # Clicking on reply option
        self.element_wait_clickable(MailPage.reply_option)
        mailpage.get_reply_option().click()

        # Clicking on Discard button
        self.element_wait_clickable(MailPage.discard_btn)
        mailpage.get_discard_btn().click()

        # Clicking on profile button to sign out
        self.element_wait_clickable(HomePage.profile_btn)
        homepage.get_profile_btn().click()

        # switch to the frame and click sign-out button
        self.driver.switch_to.frame('account')

        self.element_wait_clickable(MailPage.sign_out_btn)
        google_page = mailpage.get_sign_out_btn()
        self.driver.switch_to.default_content()

        # Going to Google.com website
        self.driver.get('https://www.google.com/')

        # Getting the signin text from that page
        sign_in_text = google_page.get_sign_out_option_text().text

        # Checking whether sent option is available or not
        assert sign_in_text == 'Sign in'

        print(" ...............Executed Successfully.................")
