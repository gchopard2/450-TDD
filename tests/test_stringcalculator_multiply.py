from src.stringcalculator import StringCalculator
import pytest

@pytest.mark.parametrize("mon_param, mon_resultat", [
    ("", 1),             # test case 1
    ("5", 5),            # test case 2
    ("8;7", 56),         # test case 3
    ("8;NOTANUMBER", 8), # test case 4
    ("102;1002", 102),   # test case 5
    ("0.3;0.2", 0.3*0.2),# test case 6
])

def test_multiply_plusieursNombres(mon_param, mon_resultat):
    # Arrange
    mon_param = mon_param
    mon_resultat = mon_resultat
    # Act
    result = StringCalculator.multiply(mon_param)
    # Assert
    assert result == mon_resultat





