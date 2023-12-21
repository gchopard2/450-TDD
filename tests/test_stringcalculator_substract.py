from src.stringcalculator import StringCalculator
import pytest

@pytest.mark.parametrize("mon_param, mon_resultat", [
    ("", 0), # test case 1
])
def test_substract_plusieursNombres(mon_param, mon_resultat):
    # Arrange
    mon_param = mon_param
    mon_resultat = mon_resultat
    # Act
    result = StringCalculator.substract(mon_param)
    # Assert
    assert result == mon_resultat