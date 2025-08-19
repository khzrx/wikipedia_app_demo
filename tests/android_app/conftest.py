import pytest
from appium import webdriver
from selene import browser
from config import to_driver_options
from wikipedia_app_demo import utils


@pytest.fixture
def context(request):
    return request.config.getoption('--context')

@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    utils.allure.attach_screenshot()
    utils.allure.attach_xml()
    session_id = browser.driver.session_id

    browser.quit()

    if context == 'bstack':
        utils.allure.attach_bstack_video(session_id)

