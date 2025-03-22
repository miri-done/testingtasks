import sys
import os
import requests

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from tasks.task_03 import getTimeData

response = getTimeData()

def test_API():
    assert response.get("status_code") == 200, f"Failed API call"
    # actual_code = response.get("status_code")


def test_high_low():
    high_no = response.get("high")
    low_no = response.get("low")

    assert high_no > low_no, f"High value not greater than low value"
