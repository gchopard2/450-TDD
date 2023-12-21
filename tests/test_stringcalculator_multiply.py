from src.stringcalculator import StringCalculator
import pytest


def test_multiply_return_0():
    # arrange
    mon_param = ""
    mon_result = 0
    #act
    multiply = StringCalculator.multiply(mon_param)
    #assert
    assert multiply == mon_result