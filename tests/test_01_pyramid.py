import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from tasks.task_01 import pyramid

# Test directly
def test_pyramid_5(capsys):
    pyramid(5)
    
    pyramid_output = capsys.readouterr().out
    
    # Test for the actual output
    expected_output = """    *
   ***
  *****
 *******
*********
"""
    # Assert equal
    assert pyramid_output == expected_output, f"Not the correct pyramid"