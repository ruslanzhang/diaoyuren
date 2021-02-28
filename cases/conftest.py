import pytest
from appium import webdriver
import time
from pages.pages_action import PagesAction


@pytest.fixture(scope="session")
def handler():
    caps = {"platformName": "Android",
            "platformVersion": "5",
            "deviceName": "127.0.0.1:21503",
            "appPackage": "com.lchr.diaoyu",
            "appActivity": "com.lchr.diaoyu.SplashActivity",
            "noReset": True,
            "newCommandTimeout": 6000,
            "skipServerInstallation": True,
            "automationName": "UiAutomator2",
            "ensureWebviewsHavePages": True
            }

    url = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(url, caps)
    pa = PagesAction(driver)
    time.sleep(6)
    yield driver, pa
    driver.quit()


def pytest_configure(config):
    markers = ['smoke', 'last']
    for mark in markers:
        config.addinivalue_line('markers', mark)