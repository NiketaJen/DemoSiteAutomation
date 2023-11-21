import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def init_driver(request):
    # Make a list of supported browsers that can be called by variables
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff']

    # os.environ is a dictionary, you get the value if it exists, if not it will return none
    browser = os.environ.get('BROWSER', None)
    # checks to see if it can find browser and if not raises an exception
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported." 
                          f"Supported are: {supported_browsers}")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    # request class driver
    request.cls.driver = driver
    yield
    driver.quit()