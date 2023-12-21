from src.stringcalculator import StringCalculator
import pytest

def test_substract_param_vide_return_zero():
    # Arrange
    mon_param = ""
    mon_resultat = 0
    # Act
    result = StringCalculator.substract(mon_param)
    # Assert
    assert result == mon_resultat