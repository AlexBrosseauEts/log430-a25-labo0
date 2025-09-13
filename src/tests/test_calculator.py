"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import pytest
from calculator import Calculator
def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition_ok():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5

@pytest.mark.xfail(reason="Test volontairement faux pour la demo")
def test_addition_fail_demo():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 2) == 5

def test_subtraction_ok():
    my_calculator = Calculator()
    assert my_calculator.subtraction(2, 3) == -1

@pytest.mark.xfail(reason="Test volontairement faux pour la demo")
def test_subtraction_fail_demo():
    my_calculator = Calculator()
    assert my_calculator.subtraction(2, 2) == 5

def test_multiplication_ok():
    my_calculator = Calculator()
    assert my_calculator.multiplication(2, 3) == 6

@pytest.mark.xfail(reason="Test volontairement faux pour la demo")
def test_multiplication_fail_demo():
    my_calculator = Calculator()
    assert my_calculator.multiplication(2, 2) == 5

def test_division_ok():
    my_calculator = Calculator()
    assert my_calculator.division(2, 2) == 1

@pytest.mark.xfail(reason="Test volontairement faux pour la demo")
def test_division_fail_demo():
    my_calculator = Calculator()
    assert my_calculator.division(2, 2) == 2