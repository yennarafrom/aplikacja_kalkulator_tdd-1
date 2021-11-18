import pytest


@pytest.mark.skip('Feature is not implemented yet')
@pytest.mark.smoke
def test_div__positive_int_values(calculator):
    assert calculator.div(6, 3) == 2


@pytest.mark.skip('Feature is not implemented yet')
@pytest.mark.smoke
def test_div__negative_int_values(calculator):
    assert calculator.div(-6, -3) == 2


@pytest.mark.skip('Feature is not implemented yet')
@pytest.mark.regression
def test_div__mixed_int_values(calculator):
    assert calculator.div(6, -3) == -2


@pytest.mark.skip('Feature is not implemented yet')
@pytest.mark.smoke
def test_div__positive_float_values(calculator):
    assert calculator.div(7.5, 3) == 2.5


@pytest.mark.skip('Feature is not implemented yet')
@pytest.mark.smoke
def test_div__negative_float_values(calculator):
    assert calculator.div(-7.5, -3) == 2.5


@pytest.mark.skip('Feature is not implemented yet')
@pytest.mark.regression
def test_div__mixed_float_values(calculator):
    assert calculator.div(-7.5, 3) == -2.5


@pytest.mark.skip('Feature is not implemented yet')
@pytest.mark.regression
def test_div__value_zero(calculator):
    with pytest.raises(ValueError):
        assert calculator.div(8, 0)
