from appium.webdriver.common.appium_service import AppiumService
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

class MyObservatoryTest:
    def __init__(self, device_name):
        desired_caps = {
            "platformName": "Android",
            "deviceName": device_name,
            "appPackage": "hko.MyObservatory_v1_0",
            "appActivity": "hko.homepage3.HomepageActivity",
            "automationName": "UiAutomator2",
            "autoGrantPermissions": True,
            "noReset": True
        }

        # startup
        # self.appium_service = AppiumService()
        # self.appium_service.start()
        self.driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
        self.wait = WebDriverWait(self.driver, 10)

    def click_burger(self):
        burger_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Navigate up")) # According to appium inspector can't find anything better
        )
        burger_button.click()

    def click_forecast_expand(self):
        forecast_expand_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Forecast & Warning Services")'))
        )
        forecast_expand_button.click()

    def click_ninedayforecast(self):
        ninedayforecast_button = self.wait.until(
            EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("9-Day Forecast")'))
        )
        ninedayforecast_button.click()

    def get_tmr_date(self):
        forecast_dayafter = self.wait.until(
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionMatches("\\d{1,2} \\w{3}")'))
        )
        return forecast_dayafter.text

    def close(self):
        self.driver.quit()
