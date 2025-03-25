import pytest
import sys
import os
from datetime import datetime, timedelta
from appium.webdriver.common.appium_service import AppiumService
from appium.webdriver.common.mobileby import MobileBy

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from tasks.task_02 import MyObservatoryTest

@pytest.fixture(scope="module")
def appium_service(): # make sure appium is running for the test
    appiumserv = AppiumService()
    appiumserv.start()
    print(Appium should be running...)
    yield appiumserv
    appiumserv.stop()

@pytest.fixture(scope="module")
def MyObs(appium_service):
    device_id = os.getenv("DEVICE_ID", "RFCW615VCFA")  # Not sure if this works, can't test it
    MyObs_instance = MyObservatoryTest(device_id)
    yield MyObs_instance
    MyObs_instance.close()

def test_verify_forecast_date(MyObs):
    MyObs.click_burger()
    MyObs.click_forecast_expand()
    MyObs.click_ninedayforecast()

    expected_date = (datetime.now() + timedelta(days=1)).strftime("%d %b") 

    displayed_date = MyObs.get_tmr_date()

    # Verify the displayed date is correct
    assert displayed_date == expected_date, f"Wrong date"
