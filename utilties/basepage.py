import pytest
import logging
import inspect
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:
    def element_wait_clickable(self, path):
        """
        explicit wait till the web element is clickable
        :param path: takes the locater of the element
        :return: None
        """
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable(path))

    def element_wait_presence(self, path):
        """
        explicit wait till the web element is present
        :param path: takes the locater of the element
        :return: None
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(path))

    def message_logging(self, message):
        """
        send message in a logfile
        :param message: message defined for user understanding
        :return: None
        """
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)
