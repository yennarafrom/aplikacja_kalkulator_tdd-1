import pytest


@pytest.mark.smoke
def test_add__positive_int_values(calculator):
    assert calculator.add(1, 3) == 4


@pytest.mark.smoke
def test_add__positive_float_values(calculator):
    assert calculator.add(1.1, 3.5) == 4.6


@pytest.mark.smoke
def test_add__negative_int_values(calculator):
    assert calculator.add(-2, -3) == -5


@pytest.mark.smoke
def test_add__negative_float_values(calculator):
    assert calculator.add(-0.5, -2) == -2.5


@pytest.mark.regression
def test_add__mixed_int_values(calculator):
    assert calculator.add(1, -3) == -2
    assert calculator.add(-4, 3) == -1


@pytest.mark.regression
def test_add__mixed_float_values(calculator):
    assert round(calculator.add(1.4, -3.1), 1) == -1.7
    assert calculator.add(-2.5, 1.1) == -1.4
