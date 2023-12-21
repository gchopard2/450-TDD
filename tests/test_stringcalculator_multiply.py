from src.stringcalculator import StringCalculator
import pytest


def test_multiply():
    # arrange
    mon_param = ""
    mon_result = 0
    #act
    multiply = StringCalculator.multiply(mon_param)
    #assert
    assert multiply == mon_result