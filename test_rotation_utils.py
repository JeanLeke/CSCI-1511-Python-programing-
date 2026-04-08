"""
Program Name: Testing the adjust_rotation() Function:
Author: Jean Lekefua Fombindia
Purpose: is to write a complete pytest test suite in test_rotation_utils.py 
that verifies the adjust_rotation function from rotation_utils.py is working correctly.
Date: April 7, 2026

"""
import pytest 
from rotation_utils import adjust_rotation

def test_1():
    assert adjust_rotation(100) == 100

def test_2():
    assert adjust_rotation(460) == 100

def test_3():
    assert adjust_rotation(820) == 100

def test_4():
    assert adjust_rotation(-100) == 260

def test_5():
    assert adjust_rotation(-460) == 260

def test_6():
    assert adjust_rotation(-820) == 260

def test_non_numeric_input_7():
    with pytest.raises(TypeError):
        adjust_rotation("abc") 

