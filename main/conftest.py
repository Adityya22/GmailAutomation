import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.configuration import TestConfig


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--email", action="store", default="abcd@test.com")
    parser.addoption("--password", action="store", default="12345678")


@pytest.fixture(scope='class')
def setup(request):
    # Setup for Chrome Driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    s = Service(TestConfig.chrome_executable_path)
    driver = webdriver.Chrome(service=s, options=chrome_options)

    # Maximizing the window
    driver.maximize_window()

    # Opening the website
    driver.get(TestConfig.base_url)

    request.cls.driver = driver
    # yield
    # driver.close()


@pytest.fixture
def params(request):
    params = {'email': request.config.getoption('--email'),
              'password': request.config.getoption('--password')
              }

    if params['email'] is None and params['password'] is None:
        pytest.skip()

    return params
