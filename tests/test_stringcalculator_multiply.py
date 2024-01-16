from src.stringcalculator import StringCalculator
import pytest


def test_multiply_param_7_8_return_56():
    # Arrange
    mon_param = "7;8"
    mon_resultat = 56
    # Act
    result = StringCalculator.multiply(mon_param)
    # Assert
    assert result == mon_resultat





