from src.stringcalculator import StringCalculator
import pytest

def test_add_param_vide_return_zero():
    # Arrange
    mon_param = ""
    mon_resultat = 0
    # Act
    result = StringCalculator.add(mon_param)
    # Assert
    assert result == mon_resultat

def test_add_param_5_return_5():
    # Arrange
    mon_param = "5"
    mon_resultat = 5
    # Act
    result = StringCalculator.add(mon_param)
    # Assert
    assert result == mon_resultat
def test_add_param_7_8_return_15():
    # Arrange
    mon_param = "7;8"
    mon_resultat = 15
    # Act
    result = StringCalculator.add(mon_param)
    # Assert
    assert result == mon_resultat

@pytest.mark.parametrize("mon_param, mon_resultat", [
    ("1;2;3", 6), # test case 4
    ("1;2;3;4", 10), # test case 5
    ("1;2;5", 8), # test case 6
    ("1;2;0", 3), # test case 7
    ("1;2;1000", 1003), # test case 8
    ("1;2;1001", 3), # test case 9
])
def test_Add_plusieursNombres(mon_param, mon_resultat):
    # act
    somme = StringCalculator.add(mon_param)
    # assert
    assert somme == mon_resultat