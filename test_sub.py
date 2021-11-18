import pytest


@pytest.mark.smoke
def test_sub__positive_int_values(calculator):
    assert calculator.sub(1, 3) == -2


@pytest.mark.smoke
def test_sub__positive_float_values(calculator):
    assert calculator.sub(1.1, 3.5) == -2.4


@pytest.mark.smoke
def test_sub__negative_int_values(calculator):
    assert calculator.sub(-2, -3) == 1


@pytest.mark.smoke
def test_sub__negative_float_values(calculator):
    assert calculator.sub(-0.5, -2) == 1.5


@pytest.mark.regression
def test_sub__mixed_int_values(calculator):
    assert calculator.sub(1, -3) == 4
    assert calculator.sub(-4, 3) == -7


@pytest.mark.regression
def test_sub__mixed_float_values(calculator):
    assert calculator.sub(1.4, -3.1) == 4.5
    assert calculator.sub(-2.5, 1.1) == -3.6
