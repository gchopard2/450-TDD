from src.stringcalculator import StringCalculator
import pytest


def test_multiply_return_5():
    # arrange
    mon_param = "5"
    mon_result = 5
    #act
    multiply = StringCalculator.multiply(mon_param)
    #assert
    assert multiply == mon_result